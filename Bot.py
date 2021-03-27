import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
import random
import re
from random import choice, randrange
import json
import requests
import aiohttp
import io
import urllib
import datetime

noPerms = "s-sorry daddy... you are missing perms... >w<"

client = commands.Bot(command_prefix=">")

numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


@client.command()
async def rape(ctx, *, message=None):
    """Rape someone 😈"""
    sus = message.lower()
    await ctx.channel.send(f"{ctx.message.author.mention} raped {sus} 😈")


@client.command()
async def say(ctx, *, message=None):
    """Say something funny"""
    await ctx.send(message)


@client.command()
async def banner(ctx, *, message):
    """Emojify the text"""
    try:
        bigtext = map(
            lambda c: f":{numbers[c]}: " if (c.isdigit()) \
            else f":regional_indicator_{c.lower()}: " if (c.isalpha()) \
            else "  " if (c == " ") \
            else "",
            message,
        )
        await ctx.send("".join(bigtext)[:-1])
    except Exception as e:
        await ctx.send(e)


@client.command()
async def clap(ctx, *, message):
    """Make the bot say whatever you want with claps!"""
    try:
        await ctx.send(re.sub(r"\s+", " :clap: ", message) + " :clap: ")
    except Exception as e:
        await ctx.send(e)


@client.command(aliases=["8ball", "question"])
async def _8ball(ctx, *, question):
    """Ask fta your questions"""
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "O̴̡͉̓̆̉̿̅̇̋͘͝͠͝ṷ̴̡̢̨͔͔̘̱͍͓̺͎́̕ṱ̸̙̆͌̎̄̃̈͆̀̎̂͜l̵̛͕̍͊́̌̐͒̓̊̀̚͝o̵͍̖̠̜̝̹̤͋̀̉̄͑͗͜͝͝o̵̧̲̺̲̻̝͗̍̓̋̂̄̈́͗̕k̶̡̡͔̦̹̬̩̥̐́̈́ͅ ̵̡̧̩̟͈͓̰͉̰̹̬̜̰͓͓̔̅͑̌̐̊̔͘n̴̲̟̙̣̖̮͖̔́͌̾́̎͗͂̽͐͠o̷̭͖̦̠̥̒̿͐ţ̸̹̞͕̫̩͙͍͖̓̈́̀̎̀́̓̾̎̃͌͘̕̕͜͜͝ ̸̨̨̹̲͍̪̯̥͖͙̈́̌̌̊́̋̅͑̑͠͠s̶̨̡͔̰̘̻̣̞͈̯̮̺̪̫͌̈̈́̅͐̓͝o̷̧̜̥͔̳̯͈̿ ̸̢̛̬͙̲͕̲͇͙̝̯̺͙̈̋̿̓̓͂̂̋͝ǧ̴̢̱̥͙͇́̄́̽͒͒̓̚ó̷͚͓̾́̀̅̎̆͑̍͑̓́͠͝ͅò̷̤̲͔̱͍̦͔̈́̆͘̕͠͝d̵̢̡̛̺̖͇͔͈̰̩̀.̷̧̡̮͕͖͍̳͎̜͔̭͊͋͐̅̽̋̂̋",
        "C̶̢̥̤͔͖̖̠͚̦̺̲̮̪̈́ͅa̶͇̣͍̩̭͕̪̰̼̭̣̰͉͚̔̊̄͊n̵̲̗̭̊́͊̌̀̎͗͆͘̚͠n̵̮̏̽̋̾͂̈́́̋̇̿̚͠ͅơ̶̧̨̫͎̩̳̬̤̊̈́͗́̐͑̂̕̕͠͝t̶̳͓̦̟̬̲͓̄̿͗̓̃̈́͑ͅ ̸̧͙̖̺̤̜̯̫̟̘̋̍̈́͘p̸̪͌͗̈́̂͆̂̊̐̚r̴̛̛̛̺̣̄͌̿̔̏̈́̂͌͋̔̆͝ė̶̢̢͕̪̼̙͈͕̼̏̌̒̈́͝d̸͔͕͖͓̭͙̯̗͚̱͕̫̰͚͖̉̎̓͛̓î̶̢̛̱͎̮͈͙̟̖̬̓̐̈́̄̿̔͌̓̏͝͝ͅͅc̸̫͈̣̜͈͚͚͚̘͚̞͔͉̋̂̈́͜ṫ̷̪͔̌͑̌̽̾̏̊̐ ̷̧̰̟̱͇̳̮̩͎̯̼̰̀̑̑́̍̅̅̀̀̀̐͠͝ǹ̵̨͔͎̣̰̹̭̎̀͊̒̓͐͛͑̓̏̔́͝o̶̭̬̥̘̪͔̲͎̹̓̑̂̒̄͂͊̔̈̽̈́̏̏͜w̷̰̯̪̬͇̻͛̌̏́̒́̈́̋̐̚.̶̠̙̒̄̀̀̔",
        "I̵̢̛͎̽̈́́̿͊̂̊̋̾̀̌t̷͖̺͔͎͕̞̙̿͂́̅͛͐̽̇̽̃̓͌́̈́͐ ̵̧̜̤̩͚̖͚̖̯̞̈́͛͑̈̐͐́͒́͛͘i̵̧̛͇̖̤̗͙͕̫̰̳͕̖̗̔̌̀̓s̶̤͌̀̄͊͊̾̆͊͒̐̍̃͜ ̶̨͈̤̮̙͙͕̖̮̑͂c̸̨̢̜̝͎̝̣͚̳͍̙͈͖̖͆̃͗̾̏̉̿͌̇̊͘̕ȩ̶̡̛͕͖̪̗̗̲̜̪̼̝͎̺̀̆̎͂̓̍̍̌̉̀͗͝ŕ̵̛̞̟̇̀̆t̷̳̣̮̻̹͈̗̦̣͊̀̈́̎ͅȧ̴̢͎̘̯̺̹̝̣͓̗̇̈́̾͌̔̐̈́͋̆̇͂̈́͝ḯ̷̩̬͎̯̙̙͙̩̦͇̣̘̰̱̼̊̀̅̊̀͒̀͘͝n̶̨̞̲̰̹͎̬̩̲̍̅̒̄͋̋͆̚͘.̸̮̅̀",
        "Cᔑリリ𝙹ℸ ̣  !¡∷ᒷ↸╎ᓵℸ ̣  リ𝙹∴.",
        "Aᓭꖌ ᔑ⊣ᔑ╎リ ꖎᔑℸ ̣ ᒷ∷.",
    ]
    try:
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
    except Exception as e:
        await ctx.send(e)


@client.command()
@has_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    print("Kicked user")
    await member.send(
        f"you were kicked from the federal troll agency | {reason} | kicked by: {ctx.message.author}"
    )
    await member.kick(reason=f"{reason} - Responsible User | {ctx.message.author}")


@client.command()
async def nukecount(ctx):
    await ctx.send("fta has been nuked 7 tiems!11!1 :3")


@client.command()
@has_permissions(manage_messages=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    print("Kicked user")
    await ctx.send(f"FREE {member.name.upper()} HE DINDU NUFFIN")
    await member.send(
        f"you were banned from the federal troll agency | {reason} | banned by: {ctx.message.author}"
    )
    await member.ban(reason=f"{reason} - Responsible User | {ctx.message.author}")


@client.command()
@has_permissions(manage_messages=True)
async def addrole(ctx, *, rolename):
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    if not role:
        try:
            await ctx.guild.create_role(name=rolename)
            await ctx.channel.send(
                f"c-created role {rolename}... are you proud of me? UwU"
            )
        except MissingPermissions:
            await ctx.channel.send(noPerms)
    else:
        await ctx.channel.send("that role already exists silly x3")


@client.command()
async def createchannel(ctx, name):
    if ctx.message.author.id == 530876049983143945:
        await ctx.guild.create_text_channel(name)
        await ctx.channel.send(f"made channel {name}... enjoy... <3")


@client.command()
async def delchannel(ctx, name):
    if ctx.message.author.id == 530876049983143945:
        existing_channel = discord.utils.get(ctx.guild.channels, name=name)
        await existing_channel.delete()

@client.command(aliases=["define", "urb"])
async def _defines_whatever_you_want(ctx, *args):
    word = " ".join(args)
    r = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}", headers = {'User-agent': "your bot 0.1"})
    json = r.json()
    theList = json["list"]

    e = theList[0]

    definition = e["definition"]
    permalink = e["permalink"]
    thumbs_up = e["thumbs_up"]
    sound_urls = e["sound_urls"]
    author = e["author"]
    word = e["word"]
    defid = e["defid"]
    written_on = e["written_on"]
    example = e["example"]
    thumbs_down = e["thumbs_down"]

    embed = discord.Embed(
        title = word,
        colour = discord.Colour(client_hexcolor),
        url = permalink
    )
    embed.add_field(name="Definition:", value = definition, inline = False)
    embed.add_field(name="Example:", value = example, inline = False)

    embed.set_footer(text=f"{thumbs_up}🔼  |  {thumbs_down}🔽 - Created By {author} - {written_on}")
    await ctx.send(embed=embed)
    
@client.command()
async def banggang(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/823736494610972692/823756133704400956/rprifo34ef.gif"
    )


@client.command()
@has_permissions(manage_messages=True)
async def delrole(ctx, *, rolename):
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    if role:
        try:
            await role.delete()
            await ctx.channel.send(
                f"hey {ctx.message.author.mention}... i deleted the role {rolename}...  <3"
            )
        except MissingPermissions:
            await ctx.channel.send(noPerms)
    else:
        await ctx.channel.send("that role doesnt exist dummy!!")


@client.command()
async def attic(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/805610014814240818/823805119946686514/image0.png"
    )


@client.command()
@has_permissions(manage_messages=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.id) == (member.id):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"unbanned {user.mention}! i love you !! :3")
            return


@client.command()
async def kanye(ctx):
    res = requests.get("https://api.kanye.rest/")
    res = res.json()
    quote = res["quote"]
    embed = discord.Embed(description=f"{quote} -- Kanye West")
    embed.set_footer(text="random kanye west quote")
    await ctx.send(embed=embed)


@client.command(aliases=["yt"])
async def youtube(ctx, *, query):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://normal-api.ml/youtube/searchvideo?query={urllib.parse.urlencode(query)}"
        ) as r:
            response = await r.text()
            res = json.loads(response)
            if res["status"] != "200":
                await ctx.send("can't find video #sad")
                return
            url = res["url"]
            await ctx.send(f"{url}")


@client.command(aliases=["memes"])
async def meme(ctx):
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.request("GET", url)
    memedat = json.loads(response.text)
    postlink = memedat["postLink"]
    subreddit = memedat["subreddit"]
    title = memedat["title"]
    url = memedat["url"]

    embed = discord.Embed(title=f"{title}", url=f"{postlink}")
    embed.set_footer(text=f"r/{subreddit}")
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.guild)
async def neko(ctx):
    url = "https://waifu.pics/api/sfw/neko"
    res1 = requests.request("GET", url)
    res = json.loads(res1.text)
    link = res["url"]
    embed = discord.Embed(title="nyaa~", url=link)
    embed.set_image(url=link)
    await ctx.send(embed=embed)


@client.command(aliases=["w"])
@commands.cooldown(1, 30, commands.BucketType.guild)
async def waifu(ctx):
    url = "https://waifu.pics/api/sfw/waifu"
    res1 = requests.request("GET", url)
    res = json.loads(res1.text)
    waifu = res["url"]
    embed = discord.Embed(title="here's your waifu", url=waifu)
    embed.set_image(url=waifu)
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    """Check the bot's latency."""
    try:
        await ctx.send(f"Pong! {round(client.latency * 1000)} ms")
    except Exception as e:
        await ctx.send(e)


@client.command(aliases=["av"])
async def avatar(ctx, user: discord.Member = None):
    """Check someone's avatar"""
    try:
        if user == None:
            embed1 = discord.Embed(
                title=f"Here's the avatar of {ctx.author}",
                color=discord.Colour.blue(),
            )
            embed1.set_image(url=ctx.author.avatar_url)

            await ctx.send(embed=embed1)
            return True

        else:
            if isinstance(user, discord.member.Member):
                _embed = discord.Embed(
                    title=f" Here the avatar of {user}", color=discord.Colour.blue()
                )
                _embed.set_image(url=user.avatar_url)

                await ctx.send(embed=_embed)
                return True

            await ctx.send(f"Couldn't find the user as `{user}`")

    except Exception as e:
        await ctx.send(e)


@client.command()
async def wasted(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "wasted.png"))
            await wastedsession.close()


@client.command()
async def gay(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "gay.png"))
            await wastedsession.close()


@client.command()
async def triggered(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "triggered.gif"))
            await wastedsession.close()


@client.command()
async def hentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/waifu"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="owo", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command()
async def traphentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/trap"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="😳", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command()
async def bjhentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/blowjob"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="woag", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command()
async def nekohentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/neko"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="uwu", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command(aliases=["lrcs"])
async def lyrics(ctx, *, arg):
    """
    An Example of Lyrics Command using discord.py Calling SRA's Lyrics Endpoint.
    Usage : [command_prefix]lyrics <song name>
    """
    await ctx.trigger_typing()
    arg = arg.replace(" ", "+")

    lrcsession = aiohttp.ClientSession()
    async with lrcsession.get(
        f"https://some-random-api.ml/lyrics?title={urllib.parse.urlencode(arg)}"
    ) as lrcgetlnk:
        lrcdata = await lrcgetlnk.json()
    try:
        lyrrc = str(lrcdata["lyrics"])
        for chunk in [lyrrc[i : i + 2000] for i in range(0, len(lyrrc), 2000)]:
            embed = discord.Embed(
                title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
                description=chunk,
                color=0x000000,
            )
            embed.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.avatar_url,
            )
            await ctx.send(embed=embed)
    except discord.HTTPException:
        embe = discord.Embed(
            title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
            color=0x000000,
            description=chunk,
        )
        embe.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url,
        )
        embe.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embe)
    await lrcsession.close()
    # thanks 2 randomapi


@client.command()
async def ratio(ctx, *, arg):
    await ctx.send(
        f"{arg} has been ratioed by {ctx.author.mention} with the help of the Yang Gang! https://tenor.com/view/ratioed-yang-gang-andrew-yang-yang2020-congratulations-gif-14447592"
    )


@client.command()
async def credits(ctx):
    await ctx.send(
        "main bot developer: zokluke#4082. People that contributed to the bot are listed on github. Link to the github page: https://github.com/zokluke/FTABot"
    )


@client.command()
async def amogus(ctx):
    await ctx.send(
        "ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ red is sus! ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ"
    )


@client.command()
async def kendrick(ctx):
    await ctx.send("https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg")


@client.command()
async def ltc(ctx):
    """Generates a random person and info"""
    response = requests.request("GET", "https://randomuser.me/api")
    ruinfo = json.loads(response.text)[0]
    pname = (
        f"{ruinfo['name']['title']}. {ruinfo['name']['first']} {ruinfo['name']['last']}"
    )
    pbio = f"{ruinfo['dob']['age']} y.o. living in {ruinfo['location']['city']}, {ruinfo['location']['state']}, {ruinfo['location']['country']}"

    embed = discord.Embed(title=pname, description=pbio)
    embed.set_footer(text=f"LTC alt # {randrange(1, 1000000000)}")
    embed.set_image(url="https://thispersondoesnotexist.com/image")
    await ctx.send(embed=embed)

#thispersondoesnotexist
   
@client.command(aliases = ['tpdne'])
async def thispersondoesnotexist(ctx):
      """Send an AI generated image of a person."""
      try: 
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"}
  
        f = open('face.png', 'wb')
        img = urllib.request.urlopen(urllib.request.Request('https://thispersondoesnotexist.com/image', headers = headers))
        f.write(img.read())
        embed = discord.Embed(title = 'This person does not exist.', color=discord.Color.orange())
        embed.set_image(url = 'attachment://face.png')
        await ctx.send(file=discord.File('face.png'),embed = embed)
        f.close()
      except Exception as e:
        await ctx.send(e) 



@client.command()
async def stitchface(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/790800043338760192/813121531869003826/video0_40.mp4"
    )


@client.command()
async def dababy(ctx):
    await ctx.send(
        "picture of dababy: https://cdn.discordapp.com/attachments/805610014814240818/824186254361886760/Dababy_BabyOnBaby.png"
    )

client.run("")
