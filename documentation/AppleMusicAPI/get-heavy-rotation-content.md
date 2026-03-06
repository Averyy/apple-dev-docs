# Get Heavy Rotation Content

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the resources in heavy rotation for the user.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of [`Resource`](resource.md) objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/history/heavy-rotation?limit=1
```

**Response**:

```json
{
    "data": [
        {
            "id": "1623447658",
            "type": "albums",
            "href": "/v1/catalog/us/albums/1623447658",
            "attributes": {
                "copyright": "A Polydor Records Release; ℗ 2022 Universal Music Operations Limited",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "releaseDate": "2022-05-13",
                "isMasteredForItunes": true,
                "upc": "00602445960248",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music122/v4/48/15/69/48156938-386b-b9f0-bb88-5fffbc686b15/22UMGIM23127.rgb.jpg/{w}x{h}bb.jpg",
                    "bgColor": "13140f",
                    "textColor1": "edcbc9",
                    "textColor2": "d4ba69",
                    "textColor3": "c1a6a3",
                    "textColor4": "ad9957"
                },
                "playParams": {
                    "id": "1623447658",
                    "kind": "album"
                },
                "url": "https://music.apple.com/us/album/dance-fever-apple-music-edition/1623447658",
                "recordLabel": "Polydor Records",
                "trackCount": 21,
                "isCompilation": false,
                "isSingle": false,
                "name": "Dance Fever (Apple Music Edition)",
                "artistName": "Florence + the Machine",
                "editorialNotes": {
                    "standard": "“When I make records, I make them with the idea that no one else will hear them,” Florence Welch tells Apple Music’s Zane Lowe. “When you get to the realization that this private dialogue is going to be completely public, it’s like I’ve tricked myself again.” On her band’s fifth album <i>Dance Fever</i>, such private dialogues include rejecting real love (“Girls Against God”), dance as the greatest form of release (the anxious synth-folk of “Free”), embracing less healthy coping mechanisms in her past (“Morning Elvis”), and the push-pull between a creative career and the possible desire to start a family. “I am no mother, I am no bride, I am king,” Welch declares in baritone on “King,” in which she ponders one of <i>Dance Fever</i>’s most prominent themes: her complicated relationship with her own artistry. “A lot of it is questioning what it gives to me as well, and being like, ‘Why do I need this so much, sometimes at the cost of more sustainable forms of intimacy or more stable relationships?’” she says. “I think this record is questioning, ‘How committed am I to my own loneliness? How committed am I to my sense of a tragic figure?’” \n\nWork on the album had begun alongside producer Jack Antonoff in New York in early 2020 before the pandemic forced Welch back to London, where her creativity was stifled for six long months. <i>Dance Fever</i>, then, also covers writer’s block (the cathartic “My Love,” a track intended to help shake off Welch’s blues, and our own) and her despair of what was lost in a locked-down world. Her lyrics occasionally poke fun at the image she has created of herself (“I think there's a humor also in self-knowledge that runs through this record that I've actually found really liberating,” says Welch), but they are often as strikingly vulnerable as on 2018’s <i>High as Hope</i>. And even if the singer admits on “King” that she is “never satisfied,” her band’s fifth album has brought her rare peace. “I feel like I managed to take everything that I learned in the last 15 years and consolidate it into this record, into this art, into the videos,” she says. “I felt like, if I had to prove something to myself, somehow I did it on this record.” Read on as Welch talks us through a selection of tracks on this special Apple Music edition of <i>Dance Fever</i>, which also contains three tracks reworked as affecting spoken-word moments.\n\n<b>“King”</b>\n“Sometimes songs just arrive fully formed, and it's always when you think you'll never write a song again. I felt like my creative abilities were finally at the peak of how I understood myself as an artist and what I wanted to do. But if I wanted to have a family, there was this sense that suddenly I was being irresponsible with my time by choosing this thing that I've known my whole life, which is performance, which is making songs, which is striving to be the best performer that I can be. Somehow, it would be your fault if you miss the boat. I think that scream at the end of ‘King,’ it's just one of frustration, and confusion as well. I was thinking about Nick Cave and Leonard Cohen. I was thinking about how they can commit their body entirely to the stage. I was like, ‘Oh my god, I'm not going to be able to do that. I'm going to have to make choices.’ It's a statement of confidence, but also of humor that the album has, of ‘If I'm going to sacrifice these other things in my life, I have to be the best.’ I was like, ‘Why not me? Why can't I be king?’” \n\n<b>“Free”</b> \n“I think out of all the Florence + the Machine songs, it's sort of the purest sentiment of why I do it, distilled into why music is so important to me, why I need it, why performance is so important to me. Sometimes you just know a song is working: When we started playing it before it had even come out, just this ripple started in the audience of people catching onto the chorus and starting to move. And it was one of those moments where I was like, ‘Oh, this is a special one. This is really hitting something in people.’ And that's so magical for me. That's when the celebration starts.” \n\n<b>“Daffodil”</b>\n“I thought I'd lost my mind, because I remember coming home and being like, ‘Okay, I wrote a song today. It might be the most Florence + the Machine thing I've ever done. We're a year into the pandemic, I think maybe I'm losing it. The chorus is just “daffodil” over and over again.’ I was like, ‘Can you do that? That's a crazy thing to do.’ There were so many moments where I had nearly gave up on this record. There were so many moments where I nearly went, ‘It just feels like the way that the world is, this is just too hard to finish.’” \n\n<b>“The Bomb”</b>\n“There's a lot of nods, I think, to the previous records. All three of them are in this album, which is nice. Because I feel like somehow I'm bridging the gaps between all of them on this record, like all the things I've been interested in. This song is nodding to what I was thinking about, in terms of unavailability in people, in <i>High as Hope</i> in songs like ‘Big God,’ with like the obsession of someone who'll never text you back. Why is the person who creates the most space and gives you nothing the most appealing person? And really that's because if you're a songwriter, they give you the most enormous space for fantasy and you can write anything you want because they don't really exist. Every time I think in my life I've been in a stable place, something or someone will come up and be like, ‘How do you feel about blowing all this up?’ It's also a fear of growing up and a fear of getting older, because if you regenerate yourself constantly through other people by blowing up, changing everything, you never have to face aging or death.” \n\n<b>“Morning Elvis”</b> \n“I'm obsessed with Nick Cave as a performer, but the performer he's obsessed with is Elvis. So that's how it feeds back to me. I was at home and stuck and there was an Elvis documentary. It made me remember us, when we were on tour in New Orleans, it would have maybe been on the second record. The wheels were really coming off for me, in terms of drinking and partying. I just got very in the spirit of New Orleans and was at a party and just went, 'You all leave without me, I'm staying at this party.' I ended up with my dress completely shredded, because I'm always wearing these vintage things that basically just disintegrate: If you’re on a rager, you will come back with nothing. You would've thought things were going so well for me. What was it about me that had such a death wish? I had such little care for myself. It didn't matter what I had done the night before, or the week before, or what chaos I had created, I knew if I got to the stage, something there would save me and that I would be absolved. And that song is about that feeling, but also a testament to all the performers I've seen turn pain into something so beautiful.” ",
                    "short": "“If I had to prove something to myself, somehow I did it on this record.”"
                },
                "isComplete": true
            }
        }
    ],
    "href": "/v1/me/history/heavy-rotation?limit=1",
    "next": "/v1/me/history/heavy-rotation?offset=1"
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/history/heavy-rotation`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The offset to use for a paginated request.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Resource](resource.md)
  A resource—such as an album, song, or playlist.
- [Get Recently Played Resources](get-recently-played-resources.md)
  Fetch the recently played resources for the user.
- [Get Recently Played Tracks](get-v1-me-recent-played-tracks.md)
  Fetch the recently played tracks for the user.
- [Get Recently Played Stations](get-recently-played-stations.md)
  Fetch recently played radio stations for the user.
- [Get Recently Added Resources](get-recently-added-resources.md)
  Fetch the resources recently added to the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-heavy-rotation-content)*