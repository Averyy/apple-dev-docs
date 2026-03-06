# Get Multiple Catalog Apple Curators

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more Apple curators by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `AppleCurator` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/apple-curators?ids=976439526,1017168810
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artwork": {
                    "bgColor": "181f2e",
                    "height": 1080,
                    "textColor1": "ecc6bc",
                    "textColor2": "e1bdb5",
                    "textColor3": "c1a59f",
                    "textColor4": "b99e9a",
                    "url": "https://example.mzstatic.com/image/thumb/Features5/v4/16/e3/e7/16e3e76f-c06e-8479-c8ea-b2df32661ef4/source/{w}x{h}bb.jpeg",
                    "width": 1080
                },
                "editorialNotes": {
                    "short": "This is a Short Note.",
                    "standard": "In an age where alternative rock bands fill stadiums and ascend the pop charts, it begs the question: alternative to what? Early on, the alternative movement was a reaction to the commercial excesses of mainstream rock. Alt-rock instead brought quirky hooks, a do-it-yourself ethos, deeply personal songwriting, and genre-bending adventures to audiences hungry for something different. Although it truly exploded in the early \u201990s, the roots of alternative rock started with the punk revolt of the late \u201970s, when bands like the Ramones and the Sex Pistols proved that just about anyone could get up onstage or make a record. Throughout the \u201980s, an international network of under-the-radar bands developed, nurtured by college radio DJs and small clubs. While hardcore kept the traditional loud-and-fast sound of punk alive, many newer bands had their own distinctive styles: R.E.M.'s jangling folk-influenced rock, Sonic Youth's dissonant noise, The Cure's epic gloom, Pixies' whisper-to-a-scream dynamics, New Order's electronic grooves. \n<br /><br />\nEventually, these bands were dubbed \"alternative rock,\" thanks to their left-of-center sounds and attitudes. By the early \u201990s, though, grunge bands like Nirvana and Pearl Jam were combining punk\u2019s raw energy with classic hard-rock hooks and invading the pop charts. Suddenly, other alternative heroes like Red Hot Chili Peppers and Soundgarden found massive audiences. Over the next decade, alternative bands of various subgenres introduced a whole generation of young rockers to punk (Green Day), hip-hop (Rage Against the Machine), industrial (Nine Inch Nails), art rock (Radiohead), power pop (Weezer), psychedelia (The Flaming Lips), metal (Tool), the British Invasion (Oasis), electronic music (The Prodigy), and much more. By the 21st century, alternative rock had grown popular enough to allow bands like Foo Fighters and Coldplay to sell out stadiums in minutes. At the same time, the anything-goes spirit of alternative rock remained alive and well, with newer bands embracing garage rock (The White Stripes), emo (Paramore), and New Wave (The Killers)."
                },
                "name": "Apple Music Alternative",
                "url": "https://itunes.apple.com/us/curator/apple-music-alternative/id976439526"
            },
            "href": "/v1/catalog/us/apple-curators/976439526",
            "id": "976439526",
            "relationships": {
                "playlists": {
                    "data": [
                        {
                            "href": "/v1/catalog/us/playlists/pl.a56f0f75ff3b4e3286bfca783f31cacb",
                            "id": "pl.a56f0f75ff3b4e3286bfca783f31cacb",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.a56f0f75ff3b4e3286bfca783f31cacb",
                            "id": "pl.a56f0f75ff3b4e3286bfca783f31cacb",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.eee650f71b354e30a42531889ca5de25",
                            "id": "pl.eee650f71b354e30a42531889ca5de25",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.54650bcc7b3f44069f33cb78ef025e80",
                            "id": "pl.54650bcc7b3f44069f33cb78ef025e80",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.c3b0b6f95633433ba64a76f76af5d44d",
                            "id": "pl.c3b0b6f95633433ba64a76f76af5d44d",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.1aee747a7e644aa9b0ecce0145c565b9",
                            "id": "pl.1aee747a7e644aa9b0ecce0145c565b9",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.4d6e7c62a4ed49a797036daf1d6b94e1",
                            "id": "pl.4d6e7c62a4ed49a797036daf1d6b94e1",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.c3da505974c34eeba802f37c87d5bd81",
                            "id": "pl.c3da505974c34eeba802f37c87d5bd81",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.45512ae473d44ec3b1879f31621d406a",
                            "id": "pl.45512ae473d44ec3b1879f31621d406a",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.493ec39d5ca04d6b9d1d122a2a565e80",
                            "id": "pl.493ec39d5ca04d6b9d1d122a2a565e80",
                            "type": "playlists"
                        }
                    ],
                    "href": "/v1/catalog/us/apple-curators/976439526/playlists",
                    "next": "/v1/catalog/us/apple-curators/976439526/playlists?offset=10"
                }
            },
            "type": "apple-curators"
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "000000",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "ffffff",
                    "textColor3": "cbcbcb",
                    "textColor4": "cbcbcb",
                    "url": "https://example.mzstatic.com/image/thumb/Features7/v4/e4/1e/40/e41e4077-fc63-f6b6-b31c-bd6a80b1ecfa/source/{w}x{h}bb.jpeg",
                    "width": 1080
                },
                "editorialNotes": {
                    "short": "This is a short description",
                    "standard": "Live music lives here. Live Nation TV delivers unprecedented access to your favorite touring artists, producing exclusive original documentary series, videos, photos, interviews, and news.",
                    "tagline": "This is a Tag Line"
                },
                "name": "Live Nation TV",
                "url": "https://itunes.apple.com/us/curator/live-nation-tv/id1017168810"
            },
            "href": "/v1/catalog/us/apple-curators/1017168810",
            "id": "1017168810",
            "relationships": {
                "playlists": {
                    "data": [
                        {
                            "href": "/v1/catalog/us/playlists/pl.3e445e68ae6647a29c282c337599c17e",
                            "id": "pl.3e445e68ae6647a29c282c337599c17e",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.44e3e8955d164613b2714c88707221ac",
                            "id": "pl.44e3e8955d164613b2714c88707221ac",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.1408f546d114465d904b6c523408d2af",
                            "id": "pl.1408f546d114465d904b6c523408d2af",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.465a6ed130a5417c8e1afb934b980b1a",
                            "id": "pl.465a6ed130a5417c8e1afb934b980b1a",
                            "type": "playlists"
                        }
                    ],
                    "href": "/v1/catalog/us/apple-curators/1017168810/playlists"
                }
            },
            "type": "apple-curators"
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/apple-curators`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the Apple curators. The maximum fetch limit is 100.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object AppleCurators](applecurators.md)
  A resource object that represents an Apple curator.
- [object AppleCuratorsResponse](applecuratorsresponse.md)
  The response to a request for Apple curators.
- [Get a Catalog Apple Curator](get-a-catalog-apple-curator.md)
  Fetch an Apple curator by using the curator’s identifier.
- [Get a Catalog Apple Curator's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-9aupk.md)
  Fetch an Apple curator’s relationship by using its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-apple-curators)*