# Get a Catalog Apple Curator's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an Apple curator’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `AppleCurator.Relationships` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/apple-curators/976439526/playlists
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artwork": {
                    "bgColor": "171717",
                    "height": 1080,
                    "textColor1": "fbfbfb",
                    "textColor2": "cfbaa6",
                    "textColor3": "cecece",
                    "textColor4": "aa9a89",
                    "url": "https://example.mzstatic.com/image/thumb/Features22/v4/f8/da/aa/f8daaa39-ed83-6f12-dab1-b881216d529d/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "The Swedish band wrap their sad love stories in sweet, effervescent pop-rock.",
                    "standard": "The Cardigans burst out of Sweden with some of the finest, sweetest pop-rock of the mid-'90s. But underneath that sugary coating sits an overwhelming sense of melancholy, even on the seemingly sanguine \"Lovefool\", in which Nina Persson coyly laments an unrequited love over bopping rhythms and a glimmering guitar. These dark inclinations seeped into the band's music too, with the electro-rock sizzle of \"My Favourite Game\" and the ghostly guitar of \"Hanging Around\" eventually leading them to explore country music's softer\u2014and sadder\u2014side in \"You're the Storm\"."
                },
                "lastModifiedDate": "2017-06-30T17:47:16Z",
                "name": "The Cardigans Essentials",
                "playParams": {
                    "id": "pl.c04d6e9934ea411684a082c1847bc3ae",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/the-cardigans-essentials/pl.c04d6e9934ea411684a082c1847bc3ae"
            },
            "href": "/v1/catalog/us/playlists/pl.c04d6e9934ea411684a082c1847bc3ae",
            "id": "pl.c04d6e9934ea411684a082c1847bc3ae",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "171717",
                    "height": 1080,
                    "textColor1": "fbfbfb",
                    "textColor2": "da995e",
                    "textColor3": "cecece",
                    "textColor4": "b37f50",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/f6/40/04/f640040b-84ad-5408-0652-4a4df9f510fc/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "The Palestinian-Canadian rapper packs his dark tracks with sink-into-the-couch vibes.",
                    "standard": "Although Ahmad \u201cBelly\u201d Balshe had been rapping for well over a decade in his adopted hometown of Ottawa, Canada\u2014even garnering a Juno Award in 2008 for Rap Recording of the Year for The Revolution\u2014it wasn't until 2015's mixtape Up for Days that the rest of the world started to take notice. On it, the Palestine-born rapper brought his effortlessly laidback, sink-into-the-couch flow to jams with The Weeknd (\u201cMight Not\u201d) and Travis Scott (\u201cWhite Girls\u201d). Writing a handful of songs for The Weeknd's Beauty Behind the Madness only galvanized Belly's growing impact; guests like Waka Flocka Flame, Juicy J, and Lil Wayne packed his 2016 mixtape Another Day in Paradise."
                },
                "lastModifiedDate": "2017-07-27T19:16:30Z",
                "name": "Belly Essentials",
                "playParams": {
                    "id": "pl.4c819db0531d4a8fbe2f49027f8c5c74",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/belly-essentials/pl.4c819db0531d4a8fbe2f49027f8c5c74"
            },
            "href": "/v1/catalog/us/playlists/pl.4c819db0531d4a8fbe2f49027f8c5c74",
            "id": "pl.4c819db0531d4a8fbe2f49027f8c5c74",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "3f58c4",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "8ed2f1",
                    "textColor3": "d8ddf3",
                    "textColor4": "7ebae8",
                    "url": "https://example.mzstatic.com/image/thumb/Features122/v4/94/35/a7/9435a73b-f9fe-e28d-86aa-ca0fe4a04f10/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "lastModifiedDate": "2017-04-04T21:07:50Z",
                "name": "Bush: Deep Cuts",
                "playParams": {
                    "id": "pl.14028dbd6c0148afb2572d99a0a93274",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/bush-deep-cuts/pl.14028dbd6c0148afb2572d99a0a93274"
            },
            "href": "/v1/catalog/us/playlists/pl.14028dbd6c0148afb2572d99a0a93274",
            "id": "pl.14028dbd6c0148afb2572d99a0a93274",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "3041c2",
                    "height": 1080,
                    "textColor1": "90f1dc",
                    "textColor2": "7ec4ed",
                    "textColor3": "7dced6",
                    "textColor4": "6eaae5",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/c1/d5/8a/c1d58a6a-51e5-67a7-ea44-de979245c393/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "Their pop craftsmanship never wavered over their epic career.",
                    "standard": "R.E.M. were the rare rock band whose craftsmanship never wavered over the course of a three-decade career. While the propulsive jangle of Murmur gem \u201cMoral Kiosk\u201d betrays the sheer depth of their early catalog, later-era singles show their pop instincts only got sharper over time: 2001's \u201cImitation of Life\u201d is an elating anthem, while 2011 swan song \u201cWe All Go Back to Where We Belong\u201d is a folky lullaby illuminated by Bacharachian brass."
                },
                "lastModifiedDate": "2017-08-08T18:01:49Z",
                "name": "R.E.M.: Deep Cuts",
                "playParams": {
                    "id": "pl.f94c6790c5684c92a17149e274cd44be",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/r-e-m-deep-cuts/pl.f94c6790c5684c92a17149e274cd44be"
            },
            "href": "/v1/catalog/us/playlists/pl.f94c6790c5684c92a17149e274cd44be",
            "id": "pl.f94c6790c5684c92a17149e274cd44be",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "dddddd",
                    "height": 1080,
                    "textColor1": "080808",
                    "textColor2": "392419",
                    "textColor3": "323232",
                    "textColor4": "594940",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/de/d8/c3/ded8c375-6f97-10f9-432b-f56645cded00/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "Moody atmospherics add depth and dimension to the artist's indie folk tunes.",
                    "standard": "Angel Olsen doesn't just sing\u2014she howls and murmurs, she wails and hums, she yodels and coos; at times, her voice echoes off her arrangements like a lioness' roar ricocheting off the crevices of her cave. Though the North Carolina-based troubadour initially traded in spare, tremulous folk songs, her palette has expanded over the years: Those skeletal strummed sketches are now accompanied by ragged, clattering rock rave-ups, primordial dirges, and haunting, reverb-heavy waltzes. The amped-up sonics could have dwarfed Olsen's vocals; instead, they've emboldened her."
                },
                "lastModifiedDate": "2017-09-28T21:45:44Z",
                "name": "Angel Olsen Essentials",
                "playParams": {
                    "id": "pl.31637c976b6d40f5a767903f71f8c688",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/angel-olsen-essentials/pl.31637c976b6d40f5a767903f71f8c688"
            },
            "href": "/v1/catalog/us/playlists/pl.31637c976b6d40f5a767903f71f8c688",
            "id": "pl.31637c976b6d40f5a767903f71f8c688",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "121212",
                    "height": 1080,
                    "textColor1": "fafafa",
                    "textColor2": "ccb288",
                    "textColor3": "cccccc",
                    "textColor4": "a69270",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/2a/12/22/2a122296-0fae-ae8b-bb13-4bf7918e64be/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "Roots-oriented Brooklyn rockers with a rustic, organic sensibility.",
                    "standard": "Woods may be from the mean streets of Brooklyn, but, as their name implies, the roots-oriented rockers have a rustic, organic sensibility. In the band's earliest incarnation, in the \u200bmid \u201800s, singer/guitarist Jeremy Earl used Woods to send crackly indie-folk transmissions\u2014part Alan Lomax field recording, part Microphones-style four-track reverie\u2014but as the project morphed and \u200bgrew, its sound shifted toward a \u200bshambling take\u200b on psychedelic roots-rock, with woolly, guitar-forward jams structured around judicious piano and percussion, and reedy vocals floating in a warmly analogue, pot-scented haze."
                },
                "lastModifiedDate": "2017-08-23T21:46:25Z",
                "name": "Woods Essentials",
                "playParams": {
                    "id": "pl.8cb70d7ee9b7496e969cc95f3d7b2af0",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/woods-essentials/pl.8cb70d7ee9b7496e969cc95f3d7b2af0"
            },
            "href": "/v1/catalog/us/playlists/pl.8cb70d7ee9b7496e969cc95f3d7b2af0",
            "id": "pl.8cb70d7ee9b7496e969cc95f3d7b2af0",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "121212",
                    "height": 1080,
                    "textColor1": "fafafa",
                    "textColor2": "cfcfcf",
                    "textColor3": "cccccc",
                    "textColor4": "a9a9a9",
                    "url": "https://example.mzstatic.com/image/thumb/Features118/v4/80/ca/04/80ca04ca-d32e-bf51-8da8-dc3716d05cc0/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "The kings of Brooklyn's indie scene.",
                    "standard": "Brooklyn singer-songwriter Edward Droste started Grizzly Bear as a offhand DIY solo project. But following the release of 2004's Horn of Plenty, Droste expanded it into a full band, adding drummer Christopher Bear, bassist Chris Taylor, and guitarist-singer Daniel Rossen to create a harmony-driven blend of modern electronics and '60s-style chamber pop. 2006's Yellow House and 2009's expansive Veckatimest brought the band from cult acclaim to the front line of the '10s indie scene. Fourth album Shields brought a new collaborative spirit to the band."
                },
                "lastModifiedDate": "2017-01-23T22:34:57Z",
                "name": "Grizzly Bear Essentials",
                "playParams": {
                    "id": "pl.744e5321e83c4841ad8377d6c41d4718",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/grizzly-bear-essentials/pl.744e5321e83c4841ad8377d6c41d4718"
            },
            "href": "/v1/catalog/us/playlists/pl.744e5321e83c4841ad8377d6c41d4718",
            "id": "pl.744e5321e83c4841ad8377d6c41d4718",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "171717",
                    "height": 1080,
                    "textColor1": "fbfbfb",
                    "textColor2": "d8d8d8",
                    "textColor3": "cecece",
                    "textColor4": "b1b1b1",
                    "url": "https://example.mzstatic.com/image/thumb/Features71/v4/3e/c7/d2/3ec7d2e8-9094-881b-44b4-89e96d8ac009/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "A minimalist power duo that's short on instruments but big on noise.",
                    "standard": "Toronto musicians Sebastien Grainger and Jesse F. Keeler know how to scare people. Equipped with a bass, drums, vintage keyboards, and a mean sense of humor, the pair created a veritable maelstrom of noise as Death from Above 1979. After two blistering EPs, the duo put out their debut LP, You're a Woman, I'm a Machine, on Vice Records, showcasing a tighter, more accessible sound\u2014although still incredibly noisy and brash by pop standards. The buzz surrounding the duo took them around the world, but internal strife brought them to a breaking point in 2006. Grainger went solo under his own name, and Keeler explored electronic avenues with MSTRKRFT before the two reunited in 2014. Their comeback album, The Physical World, proved that their noisy rock formula hadn't lost any of its power during their hiatus."
                },
                "lastModifiedDate": "2017-09-07T20:09:51Z",
                "name": "Death from Above 1979 Essentials",
                "playParams": {
                    "id": "pl.2b1d104452ba4d259f262344bab6901c",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/death-from-above-1979-essentials/pl.2b1d104452ba4d259f262344bab6901c"
            },
            "href": "/v1/catalog/us/playlists/pl.2b1d104452ba4d259f262344bab6901c",
            "id": "pl.2b1d104452ba4d259f262344bab6901c",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "dddddd",
                    "height": 1080,
                    "textColor1": "040404",
                    "textColor2": "1b1b1b",
                    "textColor3": "2f2f30",
                    "textColor4": "424242",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/7b/21/0e/7b210eaf-0a70-a18c-51f8-f4abc68182e5/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "standard": "Every song promises a burst of crafty guitar and sharp-tongued soul."
                },
                "lastModifiedDate": "2017-08-16T23:21:15Z",
                "name": "The Strokes: Next Steps",
                "playParams": {
                    "id": "pl.da36fb632a54479da661467b15dee177",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/the-strokes-next-steps/pl.da36fb632a54479da661467b15dee177"
            },
            "href": "/v1/catalog/us/playlists/pl.da36fb632a54479da661467b15dee177",
            "id": "pl.da36fb632a54479da661467b15dee177",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "dddddd",
                    "height": 1080,
                    "textColor1": "080808",
                    "textColor2": "2d2d2d",
                    "textColor3": "323232",
                    "textColor4": "505050",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/74/d6/a0/74d6a07a-fcc9-101a-a364-91c509acc654/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Alternative",
                "description": {
                    "short": "One of the most powerful voices in 21st century indie rock.",
                    "standard": "ANOHNI's music begins and ends with Antony Hegarty's voice. Operatic in range, emotionally compelling, and filled with drama, it's the talent that anchors the baroque pop group. Breaking out with the Mercury Music Prize-winning I Am a Bird Now in 2005, the album saw Hegarty channeling her affinity for gothic imagery into unconventional art-pop songs. She's since worked with avant-garde musicians like the experimental composer Nico Muhly, while also releasing a run of live projects that showcase the power of her vocals."
                },
                "lastModifiedDate": "2017-08-10T23:29:35Z",
                "name": "ANOHNI Essentials",
                "playParams": {
                    "id": "pl.aba94bd7963148de92b0ac961f3974ae",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/anohni-essentials/pl.aba94bd7963148de92b0ac961f3974ae"
            },
            "href": "/v1/catalog/us/playlists/pl.aba94bd7963148de92b0ac961f3974ae",
            "id": "pl.aba94bd7963148de92b0ac961f3974ae",
            "type": "playlists"
        }
    ],
    "next": "/v1/catalog/us/apple-curators/976439526/playlists?offset=10"
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/apple-curators/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned. The maximum limit is 25.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object AppleCurators](applecurators.md)
  A resource object that represents an Apple curator.
- [object AppleCuratorsResponse](applecuratorsresponse.md)
  The response to a request for Apple curators.
- [Get a Catalog Apple Curator](get-a-catalog-apple-curator.md)
  Fetch an Apple curator by using the curator’s identifier.
- [Get Multiple Catalog Apple Curators](get-multiple-catalog-apple-curators.md)
  Fetch one or more Apple curators by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-9aupk)*