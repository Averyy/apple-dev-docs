# Get Catalog Charts

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more charts from the Apple Music Catalog.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the response contains an object where `results` contains chart collections. The members for the collections are the chart types in the request and the values are `Chart` objects. The `data` member of each `Chart` object contains an array of the corresponding resource ordered by popularity. For example, if the request contains the `songs` chart type, the object contains a `songs` member with a value that is a `Chart` object containing `Song` objects. This may be a paginated response. For more information, see `Fetch Resources by Page`.

If unsuccessful, the HTTP status code indicates the error and the details are in the errors array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/charts?types=songs,albums,playlists&genre=20&limit=1
```

**Response**:

```json
{
    "results": {
        "songs": [
            {
                "chart": "most-played",
                "name": "Top Songs",
                "orderId": "most-played:songs",
                "next": "/v1/catalog/us/charts?chart=most-played&genre=20&limit=1&offset=1&types=songs",
                "data": [
                    {
                        "id": "635016640",
                        "type": "songs",
                        "href": "/v1/catalog/us/songs/635016640",
                        "attributes": {
                            "albumName": "I Love You.",
                            "genreNames": [
                                "Alternative",
                                "Music"
                            ],
                            "trackNumber": 4,
                            "releaseDate": "2012-12-03",
                            "durationInMillis": 240400,
                            "isrc": "USSM11300080",
                            "artwork": {
                                "width": 3840,
                                "height": 3840,
                                "url": "https://is4-ssl.mzstatic.com/image/thumb/Music126/v4/28/71/00/287100fb-5c31-0195-5343-e6b3625886d0/886443969834.jpg/{w}x{h}bb.jpg",
                                "bgColor": "4b4b4b",
                                "textColor1": "f4f4f4",
                                "textColor2": "eaeaea",
                                "textColor3": "d2d2d2",
                                "textColor4": "cacaca"
                            },
                            "composerName": "Jesse, Zachary Abels & Jeremiah Freedman",
                            "playParams": {
                                "id": "635016640",
                                "kind": "song"
                            },
                            "url": "https://music.apple.com/us/album/sweater-weather/635016635?i=635016640",
                            "discNumber": 1,
                            "hasLyrics": true,
                            "isAppleDigitalMaster": false,
                            "name": "Sweater Weather",
                            "previews": [
                                {
                                    "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/42/2c/9d/422c9dbc-a759-d111-3b2d-ccf81ff4f33b/mzaf_16532534404492549180.plus.aac.p.m4a"
                                }
                            ],
                            "artistName": "The Neighbourhood"
                        }
                    }
                ],
                "href": "/v1/catalog/us/charts?chart=most-played&genre=20&limit=1&types=songs"
            }
        ],
        "playlists": [
            {
                "chart": "most-played",
                "name": "Top Playlists",
                "orderId": "most-played:playlists",
                "href": "/v1/catalog/us/charts?chart=most-played&genre=20&limit=1&types=playlists",
                "data": []
            }
        ],
        "albums": [
            {
                "chart": "most-played",
                "name": "Top Albums",
                "orderId": "most-played:albums",
                "next": "/v1/catalog/us/charts?chart=most-played&genre=20&limit=1&offset=1&types=albums",
                "data": [
                    {
                        "id": "1608118564",
                        "type": "albums",
                        "href": "/v1/catalog/us/albums/1608118564",
                        "attributes": {
                            "copyright": "℗ 2022 Bad Boy/Interscope Records",
                            "genreNames": [
                                "Alternative",
                                "Music"
                            ],
                            "releaseDate": "2022-03-25",
                            "upc": "00602445545803",
                            "isMasteredForItunes": true,
                            "artwork": {
                                "width": 3000,
                                "height": 3000,
                                "url": "https://is3-ssl.mzstatic.com/image/thumb/Music116/v4/d9/48/6f/d9486f75-e228-26c2-9498-befd009e2a90/22UMGIM11298.rgb.jpg/{w}x{h}bb.jpg",
                                "bgColor": "dee3e6",
                                "textColor1": "21242d",
                                "textColor2": "32333b",
                                "textColor3": "474a52",
                                "textColor4": "54565d"
                            },
                            "playParams": {
                                "id": "1608118564",
                                "kind": "album"
                            },
                            "url": "https://music.apple.com/us/album/mainstream-sellout/1608118564",
                            "recordLabel": "Bad Boy/Interscope Records",
                            "isCompilation": false,
                            "trackCount": 16,
                            "isSingle": false,
                            "name": "mainstream sellout",
                            "artistName": "Machine Gun Kelly",
                            "contentRating": "explicit",
                            "editorialNotes": {
                                "standard": "Originally, Machine Gun Kelly wanted to name his sixth LP <i>born with horns</i>, as a nod to the way he’s felt his entire life—like an outsider, whether he’s rapping or holding a guitar. Instead, he made the song <i>mainstream sellout</i>’s opening statement: a concussive, cathartic, two-and-a-half-minute rush of early-2000s pop punk whose chorus comes like a freight train, framed by a scream. “Alienate me, I'm not the one you want,” he roars...",
                                "short": "In Spatial Audio, MGK’s pop-punk hybrid hits like a bag of hammers."
                            },
                            "isComplete": true
                        }
                    }
                ],
                "href": "/v1/catalog/us/charts?chart=most-played&genre=20&limit=1&types=albums"
            }
        ]
    },
    "meta": {
        "results": {
            "order": [
                "most-played:songs",
                "most-played:playlists",
                "most-played:albums"
            ]
        }
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/charts`

## Parameters

- `types` ([string]) *(required)*: A list of the types of charts to include in the results. The possible values are `albums`, `songs`, and `music-videos`.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `chart` (string): The chart to fetch for the specified types. For possible values, get all the charts by sending this endpoint without the chart parameter. The possible values for this parameter are the `chart` attributes of the `Chart` objects in the response.
- `genre` (string): The identifier for the genre to use in the chart results.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `with` ([string]): The request modifiers for fetching non-standard charts collections. The value `cityCharts` fetches per-city charts. The value `globalTopCharts` allows the global charts to be fetched.

## See Also

- [object ChartResponse](chartresponse.md)
  The response to a request for a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/charts)*