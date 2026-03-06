# Get Recently Played Resources

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the recently played resources for the user.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of [`Resource`](resource.md) objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/recent/played
```

**Response**:

```json
{    
    "next": "/v1/me/recent/played?offset=10",
    "data": [
        {
            "id": "ra.1498157166",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498157166",
            "attributes": {
                "isLive": true,
                "name": "Apple Music Country",
                "mediaKind": "audio",
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Features114/v4/89/e2/66/89e266ee-454e-87e7-e108-dea53c54da6a/U0MtTVMtV1ctQU1fQ291bnRyeS5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "142234",
                    "textColor3": "3a412d",
                    "textColor4": "364354"
                },
                "editorialNotes": {
                    "name": "Apple Music Country",
                    "short": "Where it sounds like home.",
                    "tagline": "Where it sounds like home."
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "url": "https://music.apple.com/us/station/apple-music-country/ra.1498157166",
                "playParams": {
                    "id": "ra.1498157166",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoF7qCwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                }
            }
        },
        {
            "id": "1616728060",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1616728060",
            "attributes": {
                "copyright": "A 10 Summers/Interscope Records Release; ℗ 2022 10 Summers Records, LLC",
                "genreNames": [
                    "R&B/Soul",
                    "Music"
                ],
                "releaseDate": "2022-05-06",
                "isMasteredForItunes": true,
                "upc": "00602445790951",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music112/v4/03/45/19/034519dc-9ff9-7f63-3d02-23a101a0cc3a/22UMGIM01299.rgb.jpg/{w}x{h}bb.jpg",
                    "bgColor": "0b1b18",
                    "textColor1": "fc977a",
                    "textColor2": "ef5429",
                    "textColor3": "cc7e66",
                    "textColor4": "c14925"
                },
                "url": "https://music.apple.com/us/album/heart-on-my-sleeve/1616728060",
                "playParams": {
                    "id": "1616728060",
                    "kind": "album"
                },
                "recordLabel": "10 Summers/Interscope Records",
                "trackCount": 15,
                "isCompilation": false,
                "isSingle": false,
                "name": "Heart On My Sleeve",
                "artistName": "Ella Mai",
                "contentRating": "explicit",
                "editorialNotes": {
                    "standard": "Ella Mai knows her way around a love song. We've known that for years—certainly since her 2017 single “Boo'd Up” proved a breakout sensation—but her second album cements her as one of R&B's preeminent heart healers. <i>Heart on My Sleeve</i> is filled with the kind of desperate pleas and resolute statements of adoration that could soften even the hardest of hearts. With a voice made of satin and honey, she sings of love in the way so many wish to feel it—vulnerable and terrified yet thoroughly convinced it's worth it.\n\nThe lead singles, “DFMU” (which stands for “don't fuck me up”) and “Leave You Alone” (“I can't leave you alone,” goes the staccato and Auto-Tune hook), were the perfect appetizers for what proves to be a buffet of tender devotion intertwined with blind infatuation. On the gorgeous “Break My Heart,” Mai welcomes the heartache if it means feeling the rush for even a second: “Face my fears, ’cause if I had to choose who could break my heart, baby, it would be you,” she confesses on the hook. “Fallen Angel” literally invokes the heavens with a cameo from a Kirk Franklin-led choir that slides seamlessly into the lament of “How,” which, despite its grievances, still manages an optimistic bent. Elsewhere, tracks like “Pieces” and “A Mess” are about leaning into a person and the feelings they stir up, even when it doesn't necessarily make sense.\n\nThe songs here aren't naive to the problems or immune to the pain, but instead reflect someone choosing love again and again. It's far too easy to keep our walls up—and in a voice note at the end of “Sink or Swim,” Mary J. Blige in fact implores us to “guard that heart” from those who don't deserve us—but <i>Heart on My Sleeve</i> also reminds us of the potential rewards that await on the other side.",
                    "short": "The singer dazzles with her second LP, a collection of lush, heartfelt R&B."
                },
                "isComplete": true
            }
        },
        {
            "id": "1613321261",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1613321261",
            "attributes": {
                "copyright": "A Polydor Records Release; ℗ 2022 Universal Music Operations Limited",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2022-05-13",
                "isMasteredForItunes": true,
                "upc": "00602445676569",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/93/ce/c5/93cec50d-bb01-3a42-364a-54af31cd73c7/22UMGIM23127.rgb.jpg/{w}x{h}bb.jpg",
                    "bgColor": "13140f",
                    "textColor1": "edcbc9",
                    "textColor2": "d4ba69",
                    "textColor3": "c1a6a3",
                    "textColor4": "ad9957"
                },
                "url": "https://music.apple.com/us/album/dance-fever/1613321261",
                "playParams": {
                    "id": "1613321261",
                    "kind": "album"
                },
                "recordLabel": "Polydor Records",
                "trackCount": 14,
                "isCompilation": false,
                "isSingle": false,
                "name": "Dance Fever",
                "artistName": "Florence + the Machine",
                "editorialNotes": {
                    "standard": "“When I make records, I make them with the idea that no one else will hear them,” Florence Welch tells Apple Music’s Zane Lowe. “When you get to the realization that this private dialogue is going to be completely public, it’s like I’ve tricked myself again.” On her band’s fifth album <i>Dance Fever</i>, such private dialogues include rejecting real love (“Girls Against God”), dance as the greatest form of release (the anxious synth-folk of “Free”), embracing less healthy coping mechanisms in her past (“Morning Elvis”), and the push-pull between a creative career and the possible desire to start a family. “I am no mother, I am no bride, I am king,” Welch declares in baritone on “King,” in which she ponders one of <i>Dance Fever</i>’s most prominent themes: her complicated relationship with her own artistry. “A lot of it is questioning what it gives to me as well, and being like, ‘Why do I need this so much, sometimes at the cost of more sustainable forms of intimacy or more stable relationships?’” she says. “I think this record is questioning, ‘How committed am I to my own loneliness? How committed am I to my sense of a tragic figure?’” \n\nWork on the album had begun alongside producer Jack Antonoff in New York in early 2020 before the pandemic forced Welch back to London, where her creativity was stifled for six long months. <i>Dance Fever</i>, then, also covers writer’s block (the cathartic “My Love,” a track intended to help shake off Welch’s blues, and our own) and her despair of what was lost in a locked-down world. Her lyrics occasionally poke fun at the image she has created of herself (“I think there's a humor also in self-knowledge that runs through this record that I've actually found really liberating,” says Welch), but they are often as strikingly vulnerable as on 2018’s <i>High as Hope</i>. And even if the singer admits on “King” that she is “never satisfied,” her band’s fifth album has brought her rare peace. “I feel like I managed to take everything that I learned in the last 15 years and consolidate it into this record, into this art, into the videos,” she says. “I felt like, if I had to prove something to myself, somehow I did it on this record.” Read on as Welch talks us through a selection of tracks on <i>Dance Fever</i>.\n\n<b>“King”</b>\n“Sometimes songs just arrive fully formed, and it's always when you think you'll never write a song again. I felt like my creative abilities were finally at the peak of how I understood myself as an artist and what I wanted to do. But if I wanted to have a family, there was this sense that suddenly I was being irresponsible with my time by choosing this thing that I've known my whole life, which is performance, which is making songs, which is striving to be the best performer that I can be. Somehow, it would be your fault if you miss the boat. I think that scream at the end of ‘King,’ it's just one of frustration, and confusion as well. I was thinking about Nick Cave and Leonard Cohen. I was thinking about how they can commit their body entirely to the stage. I was like, ‘Oh my god, I'm not going to be able to do that. I'm going to have to make choices.’ It's a statement of confidence, but also of humor that the album has, of ‘If I'm going to sacrifice these other things in my life, I have to be the best.’ I was like, ‘Why not me? Why can't I be king?’” \n\n<b>“Free”</b> \n“I think out of all the Florence + the Machine songs, it's sort of the purest sentiment of why I do it, distilled into why music is so important to me, why I need it, why performance is so important to me. Sometimes you just know a song is working: When we started playing it before it had even come out, just this ripple started in the audience of people catching onto the chorus and starting to move. And it was one of those moments where I was like, ‘Oh, this is a special one. This is really hitting something in people.’ And that's so magical for me. That's when the celebration starts.” \n\n<b>“Daffodil”</b>\n“I thought I'd lost my mind, because I remember coming home and being like, ‘Okay, I wrote a song today. It might be the most Florence + the Machine thing I've ever done. We're a year into the pandemic, I think maybe I'm losing it. The chorus is just “daffodil” over and over again.’ I was like, ‘Can you do that? That's a crazy thing to do.’ There were so many moments where I had nearly gave up on this record. There were so many moments where I nearly went, ‘It just feels like the way that the world is, this is just too hard to finish.’” \n\n<b>“The Bomb”</b>\n“There's a lot of nods, I think, to the previous records. All three of them are in this album, which is nice. Because I feel like somehow I'm bridging the gaps between all of them on this record, like all the things I've been interested in. This song is nodding to what I was thinking about, in terms of unavailability in people, in <i>High as Hope</i> in songs like ‘Big God,’ with like the obsession of someone who'll never text you back. Why is the person who creates the most space and gives you nothing the most appealing person? And really that's because if you're a songwriter, they give you the most enormous space for fantasy and you can write anything you want because they don't really exist. Every time I think in my life I've been in a stable place, something or someone will come up and be like, ‘How do you feel about blowing all this up?’ It's also a fear of growing up and a fear of getting older, because if you regenerate yourself constantly through other people by blowing up, changing everything, you never have to face aging or death.” \n\n<b>“Morning Elvis”</b> \n“I'm obsessed with Nick Cave as a performer, but the performer he's obsessed with is Elvis. So that's how it feeds back to me. I was at home and stuck and there was an Elvis documentary. It made me remember us, when we were on tour in New Orleans, it would have maybe been on the second record. The wheels were really coming off for me, in terms of drinking and partying. I just got very in the spirit of New Orleans and was at a party and just went, 'You all leave without me, I'm staying at this party.' I ended up with my dress completely shredded, because I'm always wearing these vintage things that basically just disintegrate: If you’re on a rager, you will come back with nothing. You would've thought things were going so well for me. What was it about me that had such a death wish? I had such little care for myself. It didn't matter what I had done the night before, or the week before, or what chaos I had created, I knew if I got to the stage, something there would save me and that I would be absolved. And that song is about that feeling, but also a testament to all the performers I've seen turn pain into something so beautiful.” ",
                    "short": "“If I had to prove something to myself, somehow I did it on this record.”"
                },
                "isComplete": true
            }
        },
        {
            "id": "1620064449",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1620064449",
            "attributes": {
                "copyright": "℗ 2022 Kemosabe Records/RCA Records",
                "genreNames": [
                    "Latin",
                    "Music",
                    "Pop"
                ],
                "releaseDate": "2022-05-13",
                "isMasteredForItunes": true,
                "upc": "196589071002",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music122/v4/8c/f6/88/8cf68811-49f1-80b7-0422-df4e2effac75/196589071002.jpg/{w}x{h}bb.jpg",
                    "bgColor": "130c2e",
                    "textColor1": "f5f7f4",
                    "textColor2": "f7e6f4",
                    "textColor3": "c8c8cc",
                    "textColor4": "c9bacc"
                },
                "url": "https://music.apple.com/us/album/esquemas/1620064449",
                "playParams": {
                    "id": "1620064449",
                    "kind": "album"
                },
                "recordLabel": "Kemosabe Records/RCA Records",
                "trackCount": 14,
                "isCompilation": false,
                "isSingle": false,
                "name": "ESQUEMAS",
                "artistName": "Becky G.",
                "contentRating": "explicit",
                "editorialNotes": {
                    "standard": "Whether making hits in English or Spanish, Becky G. has been at the fore of global pop for the better part of a decade now. The rapid and undeniable success of her 2022 single “MAMIII” with KAROL G set the stage for the Mexican American star to return with her second studio album. Coming more than two years after <i>MALA SANTA</i>, a noteworthy record that aligned her with several other Latin hitmakers, <i>ESQUEMAS</i> allows fans to bear witness to the growth of her artistry. Compared with its predecessor, the quantity of features is fairly limited here, though the femme-forward Natti Natasha team-up “RAM PAM PAM” and the Dominican-dembow-infused “FULANITO” with El Alfa leave strong impressions. But even without the aid of flashy and fashionable guests, she proves repeatedly that she is a musical force to be reckoned with. There is both diversity and complexity in her craft, evident in the dawn confessional “BAILÉ CON MI EX” and the playfully nostalgic “FLASHBACK” as well as her select reggaetón permutations, such as “GUAPA” and “KILL BILL.”",
                    "short": "Becky G. remains a force to be reckoned with. Listen in Spatial Audio."
                },
                "isComplete": true
            }
        },
        {
            "id": "1607593873",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1607593873",
            "attributes": {
                "copyright": "℗ 2022 Columbia Records, a Division of Sony Music Entertainment",
                "genreNames": [
                    "Country",
                    "Music",
                    "Rock"
                ],
                "releaseDate": "2022-04-08",
                "isMasteredForItunes": false,
                "upc": "886449873302",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music116/v4/6d/de/02/6dde02ae-a9fe-f96e-e81f-4f18ad13d2f9/886449873302.jpg/{w}x{h}bb.jpg",
                    "bgColor": "090708",
                    "textColor1": "e4b986",
                    "textColor2": "d3a975",
                    "textColor3": "b8966d",
                    "textColor4": "ab885f"
                },
                "url": "https://music.apple.com/us/album/bronco/1607593873",
                "playParams": {
                    "id": "1607593873",
                    "kind": "album"
                },
                "recordLabel": "Columbia",
                "trackCount": 15,
                "isCompilation": false,
                "isSingle": false,
                "name": "Bronco",
                "artistName": "Orville Peck",
                "editorialNotes": {
                    "standard": "After releasing his 2019 Sub Pop debut, <i>Pony</i>, the mysterious masked troubadour Orville Peck made the unprecedented leap from DIY-country darling to Sony-supported Shania Twain duet partner in just over a year. But even as his star was on a seemingly unstoppable ascent—in the midst of a pandemic, no less—Peck admits that his signature fringed veil was often concealing sunken eyes and a frown. “When COVID happened, it made me look at my life for the first time and realize that my personal life was kind of a mess,” Peck tells Apple Music. “I had been escaping all my personal problems by just relying on the fact that I had this insanely busy schedule. I fell into a period for about three months where I was deeply, deeply depressed. It was actually the most unhappy I’ve ever been in my life. I kind of considered not ever making any more music.”\n \nBut in his darkest hour, Peck found the will to write and sing his way through the pain—and, before long, the songs started pouring out like a ruptured water main. The result is <i>Bronco</i>, a grandiose, 15-song tour de force recorded with Peck’s <i>Pony</i>-era touring band but given a big-screen production boost by Nashville studio ace Jay Joyce and an added ’60s-pop shimmer courtesy of former indie phenom-turned-Adele song doctor Tobias Jesso Jr., who co-wrote a couple of tracks. Yet for all its added glitz, <i>Bronco</i> does nothing to obscure Peck’s signature qualities: his commanding matinee-idol croon; his uncanny balance of heartache, humor, and homoeroticism; and his innate gift for twangy, tear-in-yer-beer serenades. Here, Peck gives us the stories behind some of the album’s instant country classics.\n \n<b>“Daytona Sand”</b>\n“This is about a cowboy I know who was born in Mississippi and grew up in Daytona, so I wanted to write this kind ode to Florida. And I was listening to a lot of Beach Boys, so I wanted to do my version of a country-surf song. But I wanted people to feel smacked in the face by the lyrics and the newfound confidence in the way that I present them. A lot of the songs on this album are upbeat and playful, but there’s sardonic humor in there because I’m talking about really dark and vulnerable stuff, and I wanted to show the different ways in which I could share that.”\n \n<b>“The Curse of the Blackened Eye”</b>\n“This is about that idea where, no matter what’s going on in your life, how much success you’re having, and how many people are around you at a party saying they love you, there’s always something in the corner kind of watching you or following you around that’s weighing on your mind—whether that’s depression or addiction or abuse. But I wanted to present that in a tongue-in-cheek way. I have a line in there about ‘wishing so many times that I would die,’ but I do it to a soundtrack of tiki-exotica country because I’ve been listening to a lot of ’60s exotica music.”\n \n<b>“C’mon Baby, Cry”</b>\n“Tobias and I wanted this to sound like glossy casino music meets a Bob Fosse musical, wrapped up in country. This song is me giving advice that I received at some point, because I used to find it hard to cry. And now I can’t stop, so I have to make other people join me.”\n \n<b>“Kalahari Down”</b>\n“Everyone thinks I’m Canadian because I lived in Canada for a long time, but I’m not. I was born in South Africa—I grew up in Johannesburg until I was 15. I never talked about where I was from only because I wanted to wait—obviously, I’m a man of mystery and I like to not give everyone everything all at once. I had actually written ‘Kalahari Down’ for <i>Pony</i>, and I decided to hold off on it because it wasn’t sounding the way I wanted it to—I envisioned it really grand, with strings. But I’m finally really excited to share a song about missing my home. There’s a sense of guilt and regret in the song about leaving somewhere that you don’t really want to leave because you have to go make your way in the world. I’m so proud to be South African. I go back there all the time.” \n \n<b>“Bronco”</b>\n“Obviously, I keep within the equestrian species for my album titles, and I only name them after the album is done. So, after I’d finished the first one, I decided to call it <i>Pony</i> because that album was about loneliness and I felt nervous putting myself out there, tentatively. That, to me, felt like a pony—kind of scared and shaking in the corner. And then the EP after that was <i>Show Pony</i> because I finally had this budget and this confidence, but I still felt scared. I was still the same pony, but I had ribbons in my hair, and I was on display. And then, with this album, I felt like I was able to be my true self, just untamed and unbothered, and so <i>Bronco</i> was a natural title. I already had this song written, but it wasn’t called ‘Bronco’ and the hook wasn’t there yet. So, after I decided on the album title, I pivoted this song to make it the title track.”\n \n<b>“Blush”</b>\n“This is about my time living in London. It’s my little homage to London as one of my many homes. There’s a little bit of that Beatles country era in there—like a <i>Help!</i>/‘I’ve Just Seen a Face’ vibe. I wanted to make my homage to that style—like, what would be England’s version of country music.”\n \n<b>“Let Me Drown”</b>\n“Each of these songs feels like getting something off my chest in a way, and I knew I had a song in me that would be about that big culmination of my depression during the pandemic and where I was at in my personal life. This might sound really dramatic and almost ridiculous, but I woke up in the middle of the night and I couldn’t sleep, and I had this melody in my head. And I was so frightened that I was going to forget it by morning that I walked into my studio and turned on my computer and just sang the melody in the microphone, and then went back to bed. And that’s what eventually became ‘Let Me Drown.’ It’s funny: I’m a trained singer, I’ve been singing my whole life, and I’ve sometimes held back on that because I’ve been worried about how it would come off, and felt insecure about it. But with this song, I just didn’t care anymore. I wanted to sing <i>big</i>.”\n \n<b>“Any Turn”</b>\n“I wanted to bring back the tradition of the patter song, like [Johnny Cash’s] ‘I’ve Been Everywhere’ or [R.E.M.’s] ‘It’s the End of the World As We Know It’ or [Billy Joel’s] ‘We Didn’t Start the Fire’ or [Bob Dylan’s] ‘Subterranean Homesick Blues.’ I love wordplay and witty lyrics, and there hasn’t been a patter song like those for a long time. So, I was like, ‘What could be the subject matter that’s frantic and manic and chaotic?’ And tour life was the obvious one. Every single word that I say in this song is a reference to an inside joke or a story or a crazy mishap that’s happened to us on tour.”\n \n<b>“All I Can Say”</b>\n“There’s definitely some Mazzy Star vibes on this one. I really wanted to get [bandmate] Bria [Salmena] on an official duet because we sing so much together in the live show. She’s such an incredible singer, and she’s got so much depth as a songwriter. So, I approached her and [guitarist] Duncan [Hay Jennings] about helping me write a duet. Bria and I were going through something similar in our personal lives, but separately. So, we decided on this concept of two people who are singing with each other about the same thing, but not <i>to</i> each other. It’s like we don’t even know that we’re singing with each other—that’s how we wrote it.”",
                    "short": "“I kind of considered not ever making any more music.” Listen in Spatial."
                },
                "isComplete": true
            }
        },
        {
            "id": "ra.1498155548",
            "type": "stations",
            "href": "/v1/catalog/us/stations/ra.1498155548",
            "attributes": {
                "isLive": true,
                "name": "Apple Music Hits",
                "mediaKind": "audio",
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Features114/v4/af/5f/6c/af5f6c79-5784-e57c-5202-531ece00e73b/U0MtTVMtV1ctQU1fSGl0cy5wbmc.png/{w}x{h}sr.jpg",
                    "bgColor": "f4f4f4",
                    "textColor1": "000000",
                    "textColor2": "10185f",
                    "textColor3": "292b34",
                    "textColor4": "323b7a"
                },
                "editorialNotes": {
                    "name": "Apple Music Hits",
                    "short": "Songs you know and love.",
                    "tagline": "Songs you know and love."
                },
                "supportedDrms": [
                    "fairplay",
                    "playready",
                    "widevine"
                ],
                "url": "https://music.apple.com/us/station/apple-music-hits/ra.1498155548",
                "playParams": {
                    "id": "ra.1498155548",
                    "kind": "radioStation",
                    "format": "stream",
                    "stationHash": "CgkIBRoFnJSwygUQBA",
                    "hasDrm": true,
                    "mediaType": 0
                }
            }
        }
    ]
}


```

## Endpoint

`GET https://api.music.apple.com/v1/me/recent/played`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The maximum number of recently played items to return.
- `offset` (string): The offset to use for a paginated request.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `types` ([string]) *(required)*

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.
- [Get Heavy Rotation Content](get-heavy-rotation-content.md)
  Fetch the resources in heavy rotation for the user.
- [Get Recently Played Tracks](get-v1-me-recent-played-tracks.md)
  Fetch the recently played tracks for the user.
- [Get Recently Played Stations](get-recently-played-stations.md)
  Fetch recently played radio stations for the user.
- [Get Recently Added Resources](get-recently-added-resources.md)
  Fetch the resources recently added to the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-recently-played-resources)*