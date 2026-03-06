# Search for Catalog Resources

**Framework**: Apple Music API  
**Kind**: httpRequest

Search the catalog by using a query.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `results` contains a map of search results. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/search?types=songs,albums,artists&term=beach+bunny
```

**Response**:

```json
{
    "results": {
        "artists": {
            "href": "/v1/catalog/us/search?limit=5&term=beach+bunny&types=artists",
            "data": [
                {
                    "id": "1147783278",
                    "type": "artists",
                    "href": "/v1/catalog/us/artists/1147783278",
                    "attributes": {
                        "name": "Beach Bunny",
                        "genreNames": [
                            "Alternative"
                        ],
                        "artwork": {
                            "width": 2011,
                            "height": 2011,
                            "url": "https://is4-ssl.mzstatic.com/image/thumb/Music122/v4/ee/38/80/ee3880eb-e996-8b35-887f-c71c8ad800ac/pr_source.png/{w}x{h}bb.jpg",
                            "bgColor": "19160f",
                            "textColor1": "f3949b",
                            "textColor2": "b08ff2",
                            "textColor3": "c77b7f",
                            "textColor4": "9277c5"
                        },
                        "url": "https://music.apple.com/us/artist/beach-bunny/1147783278"
                    },
                    "relationships": {
                        "albums": {
                            "href": "/v1/catalog/us/artists/1147783278/albums",
                            "data": [
                                {
                                    "id": "1482041821",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1482041821"
                                },
                                {
                                    "id": "1613600183",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1613600183"
                                },
                                {
                                    "id": "1476463573",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1476463573"
                                },
                                {
                                    "id": "1476463541",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1476463541"
                                },
                                {
                                    "id": "1537898980",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1537898980"
                                },
                                {
                                    "id": "1147798746",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1147798746"
                                },
                                {
                                    "id": "1147782780",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1147782780"
                                },
                                {
                                    "id": "1445627459",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1445627459"
                                },
                                {
                                    "id": "1589473324",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1589473324"
                                },
                                {
                                    "id": "1509311498",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1509311498"
                                },
                                {
                                    "id": "1562419539",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1562419539"
                                },
                                {
                                    "id": "1243697430",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1243697430"
                                },
                                {
                                    "id": "1590556925",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1590556925"
                                },
                                {
                                    "id": "1596358408",
                                    "type": "albums",
                                    "href": "/v1/catalog/us/albums/1596358408"
                                }
                            ]
                        }
                    }
                }
            ]
        },
        "songs": {
            "href": "/v1/catalog/us/search?limit=5&term=beach+bunny&types=songs",
            "next": "/v1/catalog/us/search?offset=5&term=beach+bunny&types=songs",
            "data": [
                {
                    "id": "1482041830",
                    "type": "songs",
                    "href": "/v1/catalog/us/songs/1482041830",
                    "attributes": {
                        "albumName": "Honeymoon",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "trackNumber": 9,
                        "releaseDate": "2020-02-14",
                        "durationInMillis": 147351,
                        "isrc": "USQE91600054",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/0b/b2/52/0bb2524d-ecfc-1bae-9c1e-218c978d7072/Honeymoon_3K.jpg/{w}x{h}bb.jpg",
                            "bgColor": "fffaa9",
                            "textColor1": "030005",
                            "textColor2": "363240",
                            "textColor3": "353226",
                            "textColor4": "5e5a55"
                        },
                        "url": "https://music.apple.com/us/album/cloud-9/1482041821?i=1482041830",
                        "playParams": {
                            "id": "1482041830",
                            "kind": "song"
                        },
                        "discNumber": 1,
                        "isAppleDigitalMaster": false,
                        "hasLyrics": true,
                        "name": "Cloud 9",
                        "previews": [
                            {
                                "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/5b/98/32/5b9832bb-5337-cd4f-5a7e-063709c465cc/mzaf_8852412892959276575.plus.aac.p.m4a"
                            }
                        ],
                        "artistName": "Beach Bunny"
                    }
                },
                {
                    "id": "1476463574",
                    "type": "songs",
                    "href": "/v1/catalog/us/songs/1476463574",
                    "attributes": {
                        "albumName": "Prom Queen - EP",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "trackNumber": 1,
                        "durationInMillis": 136562,
                        "releaseDate": "2018-08-10",
                        "isrc": "QZDA71885746",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/d0/1b/9f/d01b9f8a-fd47-4428-ef15-e5f23860e988/Prom_Queen_Art.jpg/{w}x{h}bb.jpg",
                            "bgColor": "af7db8",
                            "textColor1": "080008",
                            "textColor2": "221424",
                            "textColor3": "29192b",
                            "textColor4": "3e2942"
                        },
                        "url": "https://music.apple.com/us/album/prom-queen/1476463573?i=1476463574",
                        "playParams": {
                            "id": "1476463574",
                            "kind": "song"
                        },
                        "discNumber": 1,
                        "isAppleDigitalMaster": false,
                        "hasLyrics": true,
                        "name": "Prom Queen",
                        "previews": [
                            {
                                "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/bd/d6/02/bdd60248-cad4-34a8-bb0d-d2e462dd8b12/mzaf_8931382300295146023.plus.aac.p.m4a"
                            }
                        ],
                        "artistName": "Beach Bunny"
                    }
                },
                {
                    "id": "1476463542",
                    "type": "songs",
                    "href": "/v1/catalog/us/songs/1476463542",
                    "attributes": {
                        "albumName": "Sports - Single",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "trackNumber": 1,
                        "releaseDate": "2018-01-01",
                        "durationInMillis": 164165,
                        "isrc": "QZAPG1780549",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/c6/82/63/c682635e-f2b6-6183-e4ce-c950f88dcf5a/Sports_Art.jpg/{w}x{h}bb.jpg",
                            "bgColor": "59c2c6",
                            "textColor1": "000808",
                            "textColor2": "33242f",
                            "textColor3": "122d2e",
                            "textColor4": "3a434d"
                        },
                        "url": "https://music.apple.com/us/album/sports/1476463541?i=1476463542",
                        "playParams": {
                            "id": "1476463542",
                            "kind": "song"
                        },
                        "discNumber": 1,
                        "hasLyrics": true,
                        "isAppleDigitalMaster": false,
                        "name": "Sports",
                        "previews": [
                            {
                                "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/b7/19/60/b71960e4-ef93-9d20-55f6-18111c3edaf0/mzaf_10496805436073509743.plus.aac.p.m4a"
                            }
                        ],
                        "artistName": "Beach Bunny"
                    }
                },
                {
                    "id": "1613600384",
                    "type": "songs",
                    "href": "/v1/catalog/us/songs/1613600384",
                    "attributes": {
                        "albumName": "Emotional Creature",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "trackNumber": 12,
                        "releaseDate": "2022-07-22",
                        "durationInMillis": 342693,
                        "isrc": "USQE92100268",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/df/4e/68/df4e6833-9828-51d7-cdeb-71ecf6d3a23d/810090090962.png/{w}x{h}bb.jpg",
                            "bgColor": "202020",
                            "textColor1": "aea6f6",
                            "textColor2": "b68ef6",
                            "textColor3": "918bcb",
                            "textColor4": "9878cb"
                        },
                        "composerName": "Anthony Vaccaro, Jon Alvarado, Lili Trifilio & Matt Henkels",
                        "playParams": {
                            "id": "1613600384",
                            "kind": "song"
                        },
                        "url": "https://music.apple.com/us/album/love-song/1613600183?i=1613600384",
                        "discNumber": 1,
                        "hasLyrics": true,
                        "isAppleDigitalMaster": true,
                        "name": "Love Song",
                        "previews": [
                            {
                                "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/56/1a/58/561a584f-7d1f-27c6-8cc3-cf02e5000fce/mzaf_3967919156577514157.plus.aac.p.m4a"
                            }
                        ],
                        "artistName": "Beach Bunny"
                    }
                },
                {
                    "id": "1613600377",
                    "type": "songs",
                    "href": "/v1/catalog/us/songs/1613600377",
                    "attributes": {
                        "albumName": "Emotional Creature",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "trackNumber": 8,
                        "releaseDate": "2022-07-22",
                        "durationInMillis": 95147,
                        "isrc": "USQE92100264",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/df/4e/68/df4e6833-9828-51d7-cdeb-71ecf6d3a23d/810090090962.png/{w}x{h}bb.jpg",
                            "bgColor": "202020",
                            "textColor1": "aea6f6",
                            "textColor2": "b68ef6",
                            "textColor3": "918bcb",
                            "textColor4": "9878cb"
                        },
                        "composerName": "Anthony Vaccaro, Jon Alvarado, Lili Trifilio & Matt Henkels",
                        "url": "https://music.apple.com/us/album/gravity/1613600183?i=1613600377",
                        "playParams": {
                            "id": "1613600377",
                            "kind": "song"
                        },
                        "discNumber": 1,
                        "hasLyrics": false,
                        "isAppleDigitalMaster": true,
                        "name": "Gravity",
                        "previews": [
                            {
                                "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/ad/3c/ff/ad3cff93-17aa-8ff2-5e1e-e0035dd9c074/mzaf_13538224288044086289.plus.aac.p.m4a"
                            }
                        ],
                        "artistName": "Beach Bunny"
                    }
                }
            ]
        },
        "albums": {
            "href": "/v1/catalog/us/search?limit=5&term=beach+bunny&types=albums",
            "next": "/v1/catalog/us/search?offset=5&term=beach+bunny&types=albums",
            "data": [
                {
                    "id": "1613600183",
                    "type": "albums",
                    "href": "/v1/catalog/us/albums/1613600183",
                    "attributes": {
                        "copyright": "℗ 2022 Mom+Pop",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "releaseDate": "2022-07-22",
                        "isMasteredForItunes": true,
                        "upc": "810090090962",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/df/4e/68/df4e6833-9828-51d7-cdeb-71ecf6d3a23d/810090090962.png/{w}x{h}bb.jpg",
                            "bgColor": "202020",
                            "textColor1": "aea6f6",
                            "textColor2": "b68ef6",
                            "textColor3": "918bcb",
                            "textColor4": "9878cb"
                        },
                        "url": "https://music.apple.com/us/album/emotional-creature/1613600183",
                        "playParams": {
                            "id": "1613600183",
                            "kind": "album"
                        },
                        "recordLabel": "Mom+Pop",
                        "trackCount": 12,
                        "isCompilation": false,
                        "isSingle": false,
                        "name": "Emotional Creature",
                        "artistName": "Beach Bunny",
                        "editorialNotes": {
                            "standard": "There’s something they don’t tell you about virality: It never seems to last. Beach Bunny, the Chicago-based indie-rock band fronted by Lili Trifilio, blew up on TikTok when the songs “Prom Queen” and “Cloud 9” (the latter from their 2020 debut LP, <i>Honeymoon</i>) made the rounds. But this is a band of pop songwriters—led by Trifilio’s undeniable ability to write a hook—and so, on Beach Bunny’s sophomore LP, they’re out to make a more permanent name for themselves.\n\nBacked by Fall Out Boy producer Sean O’Keefe, <i>Emotional Creature</i> is all “emotional experiences,” says Trifilio. “And viewing them in a positive, empowering light or feeling deeply shameful—it ties into a greater theme of how we, as humans, feel things,” and how social relationships influence those feelings, be it the Y2K Disney pop of “Entropy,” the rush of a crush on “Fire Escape,” or the proggy sci-fi synth detours of “Gravity” and “Scream.” “I hope it brings relatability,” Trifilio says of the album, “and maybe acts as a cathartic experience for people going through similar things as me. Music’s healing in that way, if you find tracks that resonate.” Below, Trifilio walks Apple Music through <i>Emotional Creature</i>, track by track.\n\n<b>“Entropy”</b>\n“There’s one Jonas Brothers song called ‘Burnin’ Up,’ and it has this transitional lead into the song. It kind of fades in, in a cool way. And with Kelly Clarkson and Avril or any of the big acts of the time, I think I was pulling from a vibe more than trying to mimic anything. The song has a late-’90s, early-2000s feel. I was leaning into that and trying things and seeing what worked and would fit that vibe.”\n\n<b>“Oxygen”</b> \n“I wanted to separate the verses and the choruses, and make the verses have that anxiety undertone—not just lyrically. I wanted the guitar riff a little more chaotic. The choruses are the breakthrough moment in this song where these reflections come together and it’s like, ‘OK, everything’s fine. Don’t stress out so much.’ It took me a while to write, just because it’s quite wordy. It was this ongoing poem, notes in my phone. Once it flowed, I was like, ‘OK, this is a pretty good song. We can put this on the album. It’s not just chaotic word vomit.’”\n\n<b>“Deadweight”</b>\n“‘Deadweight’ feels like a sequel to some <i>Honeymoon</i> tracks. It was 2019, and I was feeling very passionate. I wrote it in 10 minutes; it was super fast, like getting out my therapy session emotions. But I didn’t actually know how to end the song. I procrastinated till we got to the studio and then revealed to everyone that I didn’t have an ending. It reminds me of Vampire Weekend a little bit. And to fill you in on some Midwest history: There’s this place called the Wisconsin Dells, a chaotic water park land. It’s super corny, and they also love cheese. It’s just a really weird place. All of the resorts have really weird theme songs, and I feel like, listening back, we were like, ‘Oh my god, that sounds just like the Kalahari Resort’s theme song.’”\n\n<b>“Gone”</b>\n“The best time I write is if I’m feeling something pretty intense. It’s when, instead of journaling or calling my mom, I’m like, ‘All right, let’s try to get some lyrics out of this situation first.’ Other times, it’s just a bunch of notes on my phone that are all related. I just wanted it to sound aggressive, but also simple at the same time. It’s a straightforward punk song. I like that the chords have some dissonance to them. And the contents of the song are about being stuck in a situation and wanting out, not being sure what the right thing to do is.”\n\n<b>“Eventually”</b>\n“It’s about having panic attacks, but also finding love and how that can be so healing in those moments—to have loved ones. I think I wrote this right after having a panic attack, and I was like, ‘I don’t really know who to talk to about this, but I feel like I need to get this out of my system. I need to reflect on it somehow.’ There’s something bittersweet about it, this sad undertone.“\n\n<b>“Fire Escape”</b>\n“‘I was excited about a trip that was coming up in a couple weeks with my boyfriend. We were long-distance, and I was so excited for this trip that I wrote a fantasy song about what it would be like. I did add some lyrics after the trip, too, capturing the entire event. I’ve always loved New York, and it’s funny because Chicago is, in a lot of ways, similar. It’s not the craziest transition when I’m there, but it still has such a magical mysticism to it. Things were getting a little bit better in my personal life, and I just wanted to write something happy.”\n\n<b>“Weeds”</b>\n“‘Weeds’ was one of the first songs I wrote for the album. It is one of my favorite songs on the record because it deviates from a lot of the breakup-angled songs I have. Those are super self-deprecating, and this was written from the perspective of being my own best friend. It’s me giving myself an intervention, almost. And musically, I think I took a lot of risks—experimenting and trying synths, stuff that isn’t as common on Beach Bunny things.”\n\n<b>“Gravity”</b>\n“A lot of this interlude was improvised. Sean was like, ‘Yeah, you want to do that? OK. We’re going to go get Starbucks or something. We’ll be back in a sec. You work on that.’ With the theme of the album being this salute to old sci-fi, in my head, it’s a movie-soundtrack moment.“\n\n<b>“Scream”</b>\n“‘Scream’ was, by far, the hardest to write. The guitar was fleshed out, but it was very difficult to jam on. With my bandmates, if I bring them a song, we’ll do some trial and error. They just pick up on the vibe, and we know the direction of music. It usually works out pretty easily. But ‘Scream,’ for some reason, it felt like we were all very disjointed. It is so different from other Beach Bunny stuff; it was just difficult for everybody to figure out. Everyone saw that I was getting frustrated, so they left me alone with a bunch of synths, and I tried a bunch of stuff until it finally clicked. I don’t remember how long it took, but I remember after that day, everyone was exhausted and pissed but also happy that it was just done.”\n\n<b>“Infinity Room”</b>\n“There’s this UK artist. His name’s Tom Rosenthal. His songs make me cry all the time. They’re these really sweet, acoustic songs. He’s an amazing lyricist. And there was one song where he sampled bird sounds, and that blew my mind. I wrote it down long before I went to the studio. I was like, ‘I want to put birds on the record. I don’t know where, and I don’t know if that’s going to be weird, but I’m going to bring it up and see what people think.’ It ended up working really well. ‘Infinity Room’ reminds me of being in a greenhouse. It’s ambient nature vibes. The song’s lyrics, in themselves, are ethereal.”\n\n<b>“Karaoke”</b>\n“‘Karaoke’ was written early in the pandemic or right before the pandemic. I feel like that song is, in very simple terms, just about having a crush. It doesn’t have maybe that much depth to it, but it just has a lightheartedness about when you connect with someone cool. Sonically, it’s one of the more laidback songs on the record.”\n\n<b>“Love Song”</b>\n“As soon as this song was written, I was like, ‘OK, I want this album to have a happy ending.’ It really is just a sweet love song that I wanted to write with intention. It’s this big moment and that ties in all the themes. ‘Love Song’ feels like a reflection on all of the hard moments [in a relationship], but at the end, love perseveres and everything’s OK.”",
                            "short": "The indie rockers’ sophomore album is here in Spatial Audio."
                        },
                        "isComplete": true
                    }
                },
                {
                    "id": "1482041821",
                    "type": "albums",
                    "href": "/v1/catalog/us/albums/1482041821",
                    "attributes": {
                        "copyright": "℗ 2019 Mom+Pop",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "releaseDate": "2020-02-14",
                        "isMasteredForItunes": false,
                        "upc": "858275058666",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/0b/b2/52/0bb2524d-ecfc-1bae-9c1e-218c978d7072/Honeymoon_3K.jpg/{w}x{h}bb.jpg",
                            "bgColor": "fffaa9",
                            "textColor1": "030005",
                            "textColor2": "363240",
                            "textColor3": "353226",
                            "textColor4": "5e5a55"
                        },
                        "url": "https://music.apple.com/us/album/honeymoon/1482041821",
                        "playParams": {
                            "id": "1482041821",
                            "kind": "album"
                        },
                        "recordLabel": "Mom+Pop",
                        "trackCount": 9,
                        "isCompilation": false,
                        "isSingle": false,
                        "name": "Honeymoon",
                        "artistName": "Beach Bunny",
                        "editorialNotes": {
                            "standard": "With “Prom Queen”—the homespun breakthrough from her 2018 EP of the same name—Beach Bunny’s Lili Trifilio became a sort of Liz Phair for the TikTok generation, inspiring a wealth of fan-made videos that speak to the sheer relatability and emotional charge in every line, no matter how ordinary. (“Shut up, count your calories/I never looked good in mom jeans,” she sings, amid a grid of power chords. “Wish I was like you/Blue-eyed blondie, perfect body.”) On <i>Honeymoon</i>, her Chicago outfit’s first full-length, she sounds like a songwriter quickly coming into her own, even as her best songs capture what it is to feel forever inadequate. Trifilio has a natural way with melody, and everything here sparkles—from quiet-LOUD slow-burns (“Rearview”) to jangly love letters (“Dream Boy”) and well-disguised anthems (“Ms. California”). On the late highlight “Racetrack,” she sits alone at a Wurlitzer piano and offers quiet, definitive heartbreak: “Even the moon can’t maintain the same face/I always wind up in second place.” Here, she tells us the story behind every song on the album.<br />\n<b>Promises</b>\n“That song is interesting. It was supposed to be on this EP called <i>Crybaby</i>, which I released even before I had a band. I was going through a breakup at the time, so I couldn't play it live because it was super personal and it would just make me upset singing it. I had it in the back of my head and I was like, ‘I’m going to rework this later on,’ and I'm happy we waited—I think the song feels more complete. The lyrics are the most honest out of all the songs on the record, and it's definitely about a specific person at a specific time in my life—my first love, kind of breakup situation. When it was initially written, it was more slow-paced and I think what I'm trying to say in the song is a little more aggressive. Now, it's really fun to play live.”<br />\n<b>Cuffing Season</b>\n“[Cuffing] is getting into a relationship during the colder months of the year, like holiday season through Valentine's Day. And then in the summer you're like, ‘Oh, I want to be free.’ This song is about really experiencing doubt, when the rose-colored glasses kind of come off and you start seeing problems and you're not sure. It’s kind of similar to ‘Promises’ in the sense that it's like juggling two feelings and kind of feeling them at the same time. Pretty much all these songs are about the same boyfriend. It was like a breakup and then get back together and then a breakup again. I tried to organize the album in a way that kind of had sort of a really upsetting beginning.”<br />\n<b>April</b>\n“‘April’ was a super weird song, because originally, the first two verses I was trying to write like a sad Christmas song. The lyrics originally were like, ‘Christmastime, snow is falling/I wish you're under the tree with me.’ Some dumb shit. But I really liked the melody, so I kept it like in my back pocket. And then I was feeling pretty blue one day and I was like, ‘All right, let's just mess around on guitar with the same melody but change all the lyrics.’ There's no way I could have predicted this, but I wrote it probably like a year prior, but I did end up going through the breakup with this person last April. So it was kind of like while we were recording in my head I was like, ‘Great, this really relates to my life now. Didn't mean for it to.’ But I do think that ‘April’ has kind of a friendly connotation, the blooming in springtime and then October, especially in Chicago, is basically winter—and winter here is not the greatest.”<br />\n<b>Rearview</b>\n“I feel like it's less about the other person and more about an internal dialogue I was having with myself at the time, where I just didn't feel good enough or didn't feel worthy of love and was kind of beating myself up for it. And kind of needed some way to vent it. I think going through a breakup, my ego was not in the best place, and my self-esteem more so. Pretty much all the songs in our entire discography are me trying to process something and kind of using music as a healthy outlet. It’s great because usually after a song’s done I do feel better. But I also feel kind of less attached to a certain emotion—it really does help me let go of something. It's a little uncomfortable sometimes when people hear words you're writing about them, but it is what it is.”<br />\n<b>Ms. California</b>\n“I’ve always loved California—I honestly would love to move there one day. I wanted to use that perspective of California as this haven of greatness, as a metaphor for someone that's super, super appealing. The song’s about jealousy. So, getting upset that someone else who seemingly is better than you is a threat to your relationship. Like, ‘I’m just a Midwest girl. She's the California girl. Wish I was her.’ I guess I kind of romanticize California in my head a lot just because I don't live there. And it's warmer and there's cooler people there.”<br />\n<b>Colorblind</b>\n“My friend from college made this chill beats track and was like, ‘Hey, do you want to sing over this just for fun?’ Though we never put it out or did anything with it, I had those lyrics at the back of my head because they were kind of applicable to where I was at at that time. In a way, I think it's a little bit more of like a confidence check, where it's like, ‘Look, you're saying sorry, but I'm setting boundaries for myself. We're just not on good terms, and you need to accept that.’”<br />\n<b>Racetrack</b>\n“One of the most evil ones, for sure. This song was written in a very sad period of my life, kind of the breaking point of everything. And I guess the lyric's not really directly inspired, but the only thing that was kind of keeping me sane during that period—when I wasn't really sure if we were going to break up or not—was I would just go on really, really long jogs. And there are different phases of the moon. And no matter what, it's going to have to eventually alter to the next phase over the duration of a month. So that was a metaphor for, like, ‘I can only kind of keep pretending I'm okay for so long. Eventually, I'm going to crack.’”<br />\n<b>Dream Boy</b>\n“‘Dream Boy’ is a nice one, because it's sort of seeing the more positive aspects of things. Like, ‘All right, we have this shitty path and things aren't always good, but let's just move past that.’ But it's also demanding a little bit of a respect, and not being walked over. In a sense I feel like I wrote it during a period where that's kind of what I wanted to happen—it's almost like I was trying to manifest that. But looking back on it, it's kind of cool ’cause it's sort of like segues into new experiences with new people, too. I think the whole ‘Let's meet after midnight’ thing, I was just sort of borrowing from media and movies and just kind of like all those romcoms where you see someone holding a radio up by the window or throwing a rock at the window. And then she sees him and he serenades her or something like that.”<br />\n<b>Cloud 9</b>\n“I think ‘Cloud 9’ is unlike pretty much any other Beach Bunny song where they're sort of like a constant pattern of ‘I love you, but…’ This one is just straight-up a nice love song. Or maybe not even love song, but a crush song. Having feelings for someone and it's just kind of unapologetic and not overly analytical. Like, ‘This is how I feel when things are good.’ And I like that it ends on a positive note. I don't want people to leave the album crying. I mean, I guess you could listen to it from the bottom to the top and then it could get pretty bad. This just kind of feels like closing a chapter in my life, having this album. And it's going to be exciting to move on to different topics and hopefully more positive topics.”",
                            "short": "The Chicago indie outfit follows “Prom Queen” with a debut LP just as honest."
                        },
                        "isComplete": true
                    }
                },
                {
                    "id": "1476463573",
                    "type": "albums",
                    "href": "/v1/catalog/us/albums/1476463573",
                    "attributes": {
                        "copyright": "℗ 2019 Mom+Pop",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "releaseDate": "2018-08-10",
                        "isMasteredForItunes": false,
                        "upc": "858275058062",
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/d0/1b/9f/d01b9f8a-fd47-4428-ef15-e5f23860e988/Prom_Queen_Art.jpg/{w}x{h}bb.jpg",
                            "bgColor": "af7db8",
                            "textColor1": "080008",
                            "textColor2": "221424",
                            "textColor3": "29192b",
                            "textColor4": "3e2942"
                        },
                        "url": "https://music.apple.com/us/album/prom-queen-ep/1476463573",
                        "playParams": {
                            "id": "1476463573",
                            "kind": "album"
                        },
                        "recordLabel": "Mom+Pop",
                        "trackCount": 5,
                        "isCompilation": false,
                        "isSingle": false,
                        "name": "Prom Queen - EP",
                        "artistName": "Beach Bunny",
                        "isComplete": true
                    }
                },
                {
                    "id": "1537898980",
                    "type": "albums",
                    "href": "/v1/catalog/us/albums/1537898980",
                    "attributes": {
                        "copyright": "℗ 2020 Mom+Pop",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "releaseDate": "2021-01-15",
                        "upc": "858275061680",
                        "isMasteredForItunes": false,
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is5-ssl.mzstatic.com/image/thumb/Music124/v4/3d/6f/fd/3d6ffd53-bff6-ab67-c8f3-612a82754cf6/858275061680.png/{w}x{h}bb.jpg",
                            "bgColor": "2f40fb",
                            "textColor1": "feffff",
                            "textColor2": "fa9dc2",
                            "textColor3": "d4d8fe",
                            "textColor4": "d18bcd"
                        },
                        "url": "https://music.apple.com/us/album/blame-game-ep/1537898980",
                        "playParams": {
                            "id": "1537898980",
                            "kind": "album"
                        },
                        "recordLabel": "Mom+Pop",
                        "isCompilation": false,
                        "trackCount": 4,
                        "isSingle": false,
                        "name": "Blame Game - EP",
                        "contentRating": "explicit",
                        "artistName": "Beach Bunny",
                        "isComplete": true
                    }
                },
                {
                    "id": "1476463541",
                    "type": "albums",
                    "href": "/v1/catalog/us/albums/1476463541",
                    "attributes": {
                        "copyright": "℗ 2019 Mom+Pop",
                        "genreNames": [
                            "Alternative",
                            "Music"
                        ],
                        "releaseDate": "2018-01-01",
                        "upc": "858275058048",
                        "isMasteredForItunes": false,
                        "artwork": {
                            "width": 3000,
                            "height": 3000,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Music114/v4/c6/82/63/c682635e-f2b6-6183-e4ce-c950f88dcf5a/Sports_Art.jpg/{w}x{h}bb.jpg",
                            "bgColor": "59c2c6",
                            "textColor1": "000808",
                            "textColor2": "33242f",
                            "textColor3": "122d2e",
                            "textColor4": "3a434d"
                        },
                        "url": "https://music.apple.com/us/album/sports-single/1476463541",
                        "playParams": {
                            "id": "1476463541",
                            "kind": "album"
                        },
                        "recordLabel": "Mom+Pop",
                        "isCompilation": false,
                        "trackCount": 1,
                        "isSingle": true,
                        "name": "Sports - Single",
                        "artistName": "Beach Bunny",
                        "isComplete": true
                    }
                }
            ]
        }
    },
    "meta": {
        "results": {
            "order": [
                "artists",
                "songs",
                "albums"
            ],
            "rawOrder": [
                "artists",
                "songs",
                "albums"
            ]
        }
    }
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/search`

## Parameters

- `term` (string) *(required)*: The entered text for the search with ‘`+`’ characters between each word, to replace spaces (for example `term=james+br`).
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `types` ([string]) *(required)*: The list of the types of resources to include in the results.
- `with` ([string]): A list of modifications to apply to the request.

## See Also

- [object SearchResponse](searchresponse.md)
  The response to a search request.
- [Get Catalog Search Hints](get-catalog-search-hints.md)
  Fetch the search term results for a hint.
- [Get Catalog Search Suggestions](get-catalog-search-suggesions.md)
  Fetch the search suggestions for a provided term input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/search-for-catalog-resources-(by-type))*