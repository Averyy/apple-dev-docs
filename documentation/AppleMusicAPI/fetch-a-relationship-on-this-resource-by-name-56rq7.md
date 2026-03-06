# Get a Catalog Song's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a song’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/songs/1613600188/albums
```

**Response**:

```json
{
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
                "upc": "810090090962",
                "isMasteredForItunes": true,
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
                "playParams": {
                    "id": "1613600183",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/emotional-creature/1613600183",
                "recordLabel": "Mom+Pop",
                "isCompilation": false,
                "trackCount": 12,
                "isSingle": false,
                "name": "Emotional Creature",
                "artistName": "Beach Bunny",
                "editorialNotes": {
                    "standard": "There’s something they don’t tell you about virality: It never seems to last. Beach Bunny, the Chicago-based indie-rock band fronted by Lili Trifilio, blew up on TikTok when the songs “Prom Queen” and “Cloud 9” (the latter from their 2020 debut LP, <i>Honeymoon</i>) made the rounds. But this is a band of pop songwriters—led by Trifilio’s undeniable ability to write a hook—and so, on Beach Bunny’s sophomore LP, they’re out to make a more permanent name for themselves.\n\nBacked by Fall Out Boy producer Sean O’Keefe, <i>Emotional Creature</i> is all “emotional experiences,” says Trifilio. “And viewing them in a positive, empowering light or feeling deeply shameful—it ties into a greater theme of how we, as humans, feel things,” and how social relationships influence those feelings, be it the Y2K Disney pop of “Entropy,” the rush of a crush on “Fire Escape,” or the proggy sci-fi synth detours of “Gravity” and “Scream.” “I hope it brings relatability,” Trifilio says of the album, “and maybe acts as a cathartic experience for people going through similar things as me. Music’s healing in that way, if you find tracks that resonate.” Below, Trifilio walks Apple Music through <i>Emotional Creature</i>, track by track.\n\n<b>“Entropy”</b>\n“There’s one Jonas Brothers song called ‘Burnin’ Up,’ and it has this transitional lead into the song. It kind of fades in, in a cool way. And with Kelly Clarkson and Avril or any of the big acts of the time, I think I was pulling from a vibe more than trying to mimic anything. The song has a late-’90s, early-2000s feel. I was leaning into that and trying things and seeing what worked and would fit that vibe.”\n\n<b>“Oxygen”</b> \n“I wanted to separate the verses and the choruses, and make the verses have that anxiety undertone—not just lyrically. I wanted the guitar riff a little more chaotic. The choruses are the breakthrough moment in this song where these reflections come together and it’s like, ‘OK, everything’s fine. Don’t stress out so much.’ It took me a while to write, just because it’s quite wordy. It was this ongoing poem, notes in my phone. Once it flowed, I was like, ‘OK, this is a pretty good song. We can put this on the album. It’s not just chaotic word vomit.’”\n\n<b>“Deadweight”</b>\n“‘Deadweight’ feels like a sequel to some <i>Honeymoon</i> tracks. It was 2019, and I was feeling very passionate. I wrote it in 10 minutes; it was super fast, like getting out my therapy session emotions. But I didn’t actually know how to end the song. I procrastinated till we got to the studio and then revealed to everyone that I didn’t have an ending. It reminds me of Vampire Weekend a little bit. And to fill you in on some Midwest history: There’s this place called the Wisconsin Dells, a chaotic water park land. It’s super corny, and they also love cheese. It’s just a really weird place. All of the resorts have really weird theme songs, and I feel like, listening back, we were like, ‘Oh my god, that sounds just like the Kalahari Resort’s theme song.’”\n\n<b>“Gone”</b>\n“The best time I write is if I’m feeling something pretty intense. It’s when, instead of journaling or calling my mom, I’m like, ‘All right, let’s try to get some lyrics out of this situation first.’ Other times, it’s just a bunch of notes on my phone that are all related. I just wanted it to sound aggressive, but also simple at the same time. It’s a straightforward punk song. I like that the chords have some dissonance to them. And the contents of the song are about being stuck in a situation and wanting out, not being sure what the right thing to do is.”\n\n<b>“Eventually”</b>\n“It’s about having panic attacks, but also finding love and how that can be so healing in those moments—to have loved ones. I think I wrote this right after having a panic attack, and I was like, ‘I don’t really know who to talk to about this, but I feel like I need to get this out of my system. I need to reflect on it somehow.’ There’s something bittersweet about it, this sad undertone.“\n\n<b>“Fire Escape”</b>\n“‘I was excited about a trip that was coming up in a couple weeks with my boyfriend. We were long-distance, and I was so excited for this trip that I wrote a fantasy song about what it would be like. I did add some lyrics after the trip, too, capturing the entire event. I’ve always loved New York, and it’s funny because Chicago is, in a lot of ways, similar. It’s not the craziest transition when I’m there, but it still has such a magical mysticism to it. Things were getting a little bit better in my personal life, and I just wanted to write something happy.”\n\n<b>“Weeds”</b>\n“‘Weeds’ was one of the first songs I wrote for the album. It is one of my favorite songs on the record because it deviates from a lot of the breakup-angled songs I have. Those are super self-deprecating, and this was written from the perspective of being my own best friend. It’s me giving myself an intervention, almost. And musically, I think I took a lot of risks—experimenting and trying synths, stuff that isn’t as common on Beach Bunny things.”\n\n<b>“Gravity”</b>\n“A lot of this interlude was improvised. Sean was like, ‘Yeah, you want to do that? OK. We’re going to go get Starbucks or something. We’ll be back in a sec. You work on that.’ With the theme of the album being this salute to old sci-fi, in my head, it’s a movie-soundtrack moment.“\n\n<b>“Scream”</b>\n“‘Scream’ was, by far, the hardest to write. The guitar was fleshed out, but it was very difficult to jam on. With my bandmates, if I bring them a song, we’ll do some trial and error. They just pick up on the vibe, and we know the direction of music. It usually works out pretty easily. But ‘Scream,’ for some reason, it felt like we were all very disjointed. It is so different from other Beach Bunny stuff; it was just difficult for everybody to figure out. Everyone saw that I was getting frustrated, so they left me alone with a bunch of synths, and I tried a bunch of stuff until it finally clicked. I don’t remember how long it took, but I remember after that day, everyone was exhausted and pissed but also happy that it was just done.”\n\n<b>“Infinity Room”</b>\n“There’s this UK artist. His name’s Tom Rosenthal. His songs make me cry all the time. They’re these really sweet, acoustic songs. He’s an amazing lyricist. And there was one song where he sampled bird sounds, and that blew my mind. I wrote it down long before I went to the studio. I was like, ‘I want to put birds on the record. I don’t know where, and I don’t know if that’s going to be weird, but I’m going to bring it up and see what people think.’ It ended up working really well. ‘Infinity Room’ reminds me of being in a greenhouse. It’s ambient nature vibes. The song’s lyrics, in themselves, are ethereal.”\n\n<b>“Karaoke”</b>\n“‘Karaoke’ was written early in the pandemic or right before the pandemic. I feel like that song is, in very simple terms, just about having a crush. It doesn’t have maybe that much depth to it, but it just has a lightheartedness about when you connect with someone cool. Sonically, it’s one of the more laidback songs on the record.”\n\n<b>“Love Song”</b>\n“As soon as this song was written, I was like, ‘OK, I want this album to have a happy ending.’ It really is just a sweet love song that I wanted to write with intention. It’s this big moment and that ties in all the themes. ‘Love Song’ feels like a reflection on all of the hard moments [in a relationship], but at the end, love perseveres and everything’s OK.”",
                    "short": "The indie rockers’ sophomore album is here in Spatial Audio."
                },
                "isComplete": true
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/songs/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Songs](songs.md)
  A resource object that represents a song.
- [object SongsResponse](songsresponse.md)
  The response to a songs request.
- [Get a Catalog Song](get-a-catalog-song.md)
  Fetch a song by using its identifier.
- [Get Multiple Catalog Songs by ID](get-multiple-catalog-songs-by-id.md)
  Fetch one or more songs by using their identifiers.
- [Get Multiple Catalog Songs by ISRC](get-multiple-catalog-songs-by-isrc.md)
  Fetch one or more songs by using their International Standard Recording Code (ISRC) values.
- [Get Equivalent Catalog Songs by ID](get-equivalent-ids-for-the-albums-3ce20.md)
  Fetch the equivalent, available content in the storefront for the provided songs’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-56rq7)*