# Get a Catalog Activity's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an activity’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Activity.Relationships` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/activities/976439514/playlists
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artwork": {
                    "bgColor": "00062d",
                    "height": 1080,
                    "textColor1": "ff4bb4",
                    "textColor2": "ff0082",
                    "textColor3": "cb3d99",
                    "textColor4": "cb0170",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/7b/16/72/7b16722a-4ec5-b2e7-a020-dad398229872/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Pop",
                "description": {
                    "short": "Seismic chart-smashes for that long weekend of partying.",
                    "standard": "Seismic chart-smashes for that long weekend of partying. Our editors regularly update this playlist\u2014if you hear something you like, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T04:22:04Z",
                "name": "Friday Feeling",
                "playParams": {
                    "id": "pl.91bb14d8ee10414e8fda8fb71f56db03",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/friday-feeling/pl.91bb14d8ee10414e8fda8fb71f56db03"
            },
            "href": "/v1/catalog/us/playlists/pl.91bb14d8ee10414e8fda8fb71f56db03",
            "id": "pl.91bb14d8ee10414e8fda8fb71f56db03",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "07050a",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "d8d8d8",
                    "textColor3": "cdcccd",
                    "textColor4": "aeaeaf",
                    "url": "https://example.mzstatic.com/image/thumb/Features122/v4/e5/58/17/e5581768-35a7-8bc3-b529-0616626b39b7/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music",
                "description": {
                    "short": "Kick it off with uptempo indie, pop, and electronic.",
                    "standard": "Kick it off with uptempo indie, pop, and electronic. We update these tracks regularly. If you like something, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T07:48:55Z",
                "name": "Weekend Worthy",
                "playParams": {
                    "id": "pl.3baaa090b668436797672b2dfd43d9ce",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/weekend-worthy/pl.3baaa090b668436797672b2dfd43d9ce"
            },
            "href": "/v1/catalog/us/playlists/pl.3baaa090b668436797672b2dfd43d9ce",
            "id": "pl.3baaa090b668436797672b2dfd43d9ce",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "020216",
                    "height": 1080,
                    "textColor1": "1ff7ed",
                    "textColor2": "08b7de",
                    "textColor3": "19c6c2",
                    "textColor4": "0793b6",
                    "url": "https://example.mzstatic.com/image/thumb/Features117/v4/94/17/2e/94172e16-e5d7-2d2b-66ec-e72473988168/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Pop",
                "description": {
                    "short": "The tracks that we can't stop listening to.",
                    "standard": "After a long day of searching for the hottest songs in the world, these are the tracks we can't stop listening to. This playlist is updated regularly, so if you like a song, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T18:49:19Z",
                "name": "Today's Hits",
                "playParams": {
                    "id": "pl.f4d106fed2bd41149aaacabb233eb5eb",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/todays-hits/pl.f4d106fed2bd41149aaacabb233eb5eb"
            },
            "href": "/v1/catalog/us/playlists/pl.f4d106fed2bd41149aaacabb233eb5eb",
            "id": "pl.f4d106fed2bd41149aaacabb233eb5eb",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "363636",
                    "height": 1080,
                    "textColor1": "ff71ad",
                    "textColor2": "fd2773",
                    "textColor3": "d66595",
                    "textColor4": "d52a67",
                    "url": "https://example.mzstatic.com/image/thumb/Features128/v4/86/80/dc/8680dc8c-eb8d-4fe7-3cc2-4639e0a44930/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Hip-Hop",
                "description": {
                    "short": "Hip-hop and R&B for the club.",
                    "standard": "Hip-hop and R&B for the club. Our editors regularly update this playlist\u2014if you hear something you like, add it to your library."
                },
                "lastModifiedDate": "2017-09-25T19:35:51Z",
                "name": "It's Lit!!!",
                "playParams": {
                    "id": "pl.2d4d74790f074233b82d07bfae5c219c",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/its-lit/pl.2d4d74790f074233b82d07bfae5c219c"
            },
            "href": "/v1/catalog/us/playlists/pl.2d4d74790f074233b82d07bfae5c219c",
            "id": "pl.2d4d74790f074233b82d07bfae5c219c",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "ef73bf",
                    "height": 1080,
                    "textColor1": "0c000d",
                    "textColor2": "0c020d",
                    "textColor3": "3a1730",
                    "textColor4": "391930",
                    "url": "https://example.mzstatic.com/image/thumb/Features62/v4/39/39/37/393937c5-7f5a-db10-a7f3-0652eac2fae0/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Pop",
                "description": {
                    "short": "Our editors select the new songs you need to hear this week.",
                    "standard": "After combing through countless releases each week, our editors select their favorites for The A-List: Pop\u2014the hottest tracks from across the genre. This playlist is updated regularly, so if you like a song, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T21:15:27Z",
                "name": "The A-List: Pop",
                "playParams": {
                    "id": "pl.5ee8333dbe944d9f9151e97d92d1ead9",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/the-a-list-pop/pl.5ee8333dbe944d9f9151e97d92d1ead9"
            },
            "href": "/v1/catalog/us/playlists/pl.5ee8333dbe944d9f9151e97d92d1ead9",
            "id": "pl.5ee8333dbe944d9f9151e97d92d1ead9",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "2c6266",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "facc56",
                    "textColor3": "d4dfe0",
                    "textColor4": "d1b759",
                    "url": "https://example.mzstatic.com/image/thumb/Features118/v4/ce/41/9d/ce419d2c-34ef-9fdc-7267-0a5013bde909/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Indie",
                "description": {
                    "short": "The songs heating up festival stages.",
                    "standard": "These are the tracks that are heating up festival stages. Our editors regularly update this playlist\u2014if you hear something you like, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T16:26:31Z",
                "name": "New Fire \ud83d\udd25",
                "playParams": {
                    "id": "pl.f19f6b5be8474fe789e36a6242f6113e",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/new-fire/pl.f19f6b5be8474fe789e36a6242f6113e"
            },
            "href": "/v1/catalog/us/playlists/pl.f19f6b5be8474fe789e36a6242f6113e",
            "id": "pl.f19f6b5be8474fe789e36a6242f6113e",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "020216",
                    "height": 1080,
                    "textColor1": "2ee8fe",
                    "textColor2": "16aefd",
                    "textColor3": "25bad0",
                    "textColor4": "128cce",
                    "url": "https://example.mzstatic.com/image/thumb/Features127/v4/87/78/d2/8778d2bf-9cc0-2546-e803-51edf7bd55c5/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Pop",
                "description": {
                    "short": "What's hot this week and what's coming next.",
                    "standard": "What's hot this week and what's coming next. Our editors regularly update this playlist\u2014if you hear something you like, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T01:19:36Z",
                "name": "Future Hits",
                "playParams": {
                    "id": "pl.a0214a4b459d4f79a991d1151e6f211f",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/future-hits/pl.a0214a4b459d4f79a991d1151e6f211f"
            },
            "href": "/v1/catalog/us/playlists/pl.a0214a4b459d4f79a991d1151e6f211f",
            "id": "pl.a0214a4b459d4f79a991d1151e6f211f",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "060c06",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "fe9eb2",
                    "textColor3": "cdcecd",
                    "textColor4": "cc818f",
                    "url": "https://example.mzstatic.com/image/thumb/Features127/v4/9d/ea/80/9dea80ae-c73f-a692-2516-6f2e7936df7b/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music African",
                "description": {
                    "short": "Our editors pick the hottest tracks each week.",
                    "standard": "The best new Afrobeats sounds represent an exciting hybrid\u2014rhythms sourced from Africa now soundtrack an emerging shift in pop culture that's packing dance floors from Lagos to the Caribbean, London, and New York. Our editors regularly update this playlist, so if you hear something you like, add it to your library."
                },
                "lastModifiedDate": "2017-09-29T06:54:36Z",
                "name": "Afrobeats Hits",
                "playParams": {
                    "id": "pl.dc349df19c6f410d874c197db63ecfed",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/afrobeats-hits/pl.dc349df19c6f410d874c197db63ecfed"
            },
            "href": "/v1/catalog/us/playlists/pl.dc349df19c6f410d874c197db63ecfed",
            "id": "pl.dc349df19c6f410d874c197db63ecfed",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "ffffff",
                    "height": 1080,
                    "textColor1": "030303",
                    "textColor2": "231b17",
                    "textColor3": "353535",
                    "textColor4": "4f4846",
                    "url": "https://example.mzstatic.com/image/thumb/Features62/v4/35/1a/37/351a37b9-c1c4-e02b-1103-c159dde1b1d2/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music Hip-Hop",
                "description": {
                    "short": "Where dance, hip-hop, R&B and electronic converge.",
                    "standard": "This is where dance, hip-hop, R&B and electronic music converge. Our editors regularly update this playlist\u2014if you hear something you like, add it to your library."
                },
                "lastModifiedDate": "2017-09-02T19:36:37Z",
                "name": "The WAVE",
                "playParams": {
                    "id": "pl.babe25c8236549559cba13467accd264",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/the-wave/pl.babe25c8236549559cba13467accd264"
            },
            "href": "/v1/catalog/us/playlists/pl.babe25c8236549559cba13467accd264",
            "id": "pl.babe25c8236549559cba13467accd264",
            "type": "playlists"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "000000",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "eaf435",
                    "textColor3": "cbcbcb",
                    "textColor4": "bbc32b",
                    "url": "https://example.mzstatic.com/image/thumb/Features111/v4/bb/bd/3e/bbbd3e6f-d870-d2fd-dd1a-f50ebe51c4fd/source/{w}x{h}cc.jpeg",
                    "width": 4320
                },
                "curatorName": "Apple Music",
                "description": {
                    "short": "The infectious, genre-busting sound of the UK streets.",
                    "standard": "The producers and MCs at the vanguard of the rapidly growing Afro swing movement all follow one rule: forget about rules. Drawing on grime, UK rap, Afrobeats, dancehall, and house in varying measures, no two songs sound the same. Our editors update this playlist regularly, so when you hear something you like, make sure you add it to your library. "
                },
                "lastModifiedDate": "2017-09-29T08:57:42Z",
                "name": "Afro Swing",
                "playParams": {
                    "id": "pl.674fd462d05c47afa632fcf860332996",
                    "kind": "playlist"
                },
                "playlistType": "editorial",
                "url": "https://itunes.apple.com/us/playlist/afro-swing/pl.674fd462d05c47afa632fcf860332996"
            },
            "href": "/v1/catalog/us/playlists/pl.674fd462d05c47afa632fcf860332996",
            "id": "pl.674fd462d05c47afa632fcf860332996",
            "type": "playlists"
        }
    ],
    "next": "/v1/catalog/us/activities/976439514/playlists?offset=10"
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/activities/{id}/{relationship}`

## Parameters

- `limit` (integer): Limit is the number of objects or number of objects in the specified relationship returned.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): A list of relationship names to include for resources in the response.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Activities](activities.md)
  A resource object that represents an activity curator.
- [object ActivitiesResponse](activitiesresponse.md)
  The response to a request for activities.
- [Get a Catalog Activity](get-a-catalog-activity.md)
  Fetch an activity by using its identifier.
- [Get Multiple Catalog Activities](get-multiple-catalog-activities.md)
  Fetch one or more activities by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-1eqct)*