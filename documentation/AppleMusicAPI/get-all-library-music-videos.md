# Get All Library Music Videos

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the library music videos in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/music-videos
```

**Response**:

```json
{
    "data": [
        {
            "id": "i.AWPNGa5hL7bLma",
            "type": "library-music-videos",
            "href": "/v1/me/library/music-videos/i.AWPNGa5hL7bLma",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Video128/v4/0a/13/98/0a13981b-7de7-82e5-84ac-42ecd6b1269d/Universal.422085486.00602527623597_USUV71002949.CROPPED.mzi.hhhryqtm.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Kanye West",
                "genreNames": [
                    "Hip Hop/Rap"
                ],
                "durationInMillis": 321570,
                "releaseDate": "2011-01-01",
                "name": "All of the Lights",
                "albumName": "",
                "playParams": {
                    "id": "i.AWPNGa5hL7bLma",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": false,
                    "purchasedId": "422085486"
                },
                "trackNumber": 0
            }
        },
        {
            "id": "i.qQdG97GuAVxAL2",
            "type": "library-music-videos",
            "href": "/v1/me/library/music-videos/i.qQdG97GuAVxAL2",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video/v4/33/74/ce/3374ced4-62d5-4585-86b2-5c49acc4b012/8806384543285.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "PSY",
                "genreNames": [
                    "Dance"
                ],
                "durationInMillis": 252210,
                "releaseDate": "2012-07-15",
                "name": "GANGNAM STYLE",
                "albumName": "",
                "playParams": {
                    "id": "i.qQdG97GuAVxAL2",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": false,
                    "purchasedId": "552661419"
                },
                "trackNumber": 0
            }
        },
        {
            "id": "i.1YBN9XQsq0vqZP",
            "type": "library-music-videos",
            "href": "/v1/me/library/music-videos/i.1YBN9XQsq0vqZP",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music/c9/fc/73/mzi.dqhlmfjc.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Nickelback",
                "genreNames": [
                    "Rock"
                ],
                "durationInMillis": 255672,
                "releaseDate": "2007-10-02",
                "name": "Rockstar",
                "albumName": "",
                "playParams": {
                    "id": "i.1YBN9XQsq0vqZP",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "264600886",
                    "purchasedId": "264600886"
                },
                "trackNumber": 0,
                "contentRating": "explicit"
            }
        },
        {
            "id": "i.6xpNYQrSvDJvXA",
            "type": "library-music-videos",
            "href": "/v1/me/library/music-videos/i.6xpNYQrSvDJvXA",
            "attributes": {
                "releaseDate": "2012-09-11",
                "artistName": "Conor Maynard",
                "genreNames": [
                    "Pop"
                ],
                "trackNumber": 0,
                "durationInMillis": 246203,
                "playParams": {
                    "id": "i.6xpNYQrSvDJvXA",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": false,
                    "purchasedId": "561707545"
                },
                "name": "Turn Around (feat. Ne-Yo)"
            }
        },
        {
            "id": "i.V7B9dQLsZ8DZKe",
            "type": "library-music-videos",
            "href": "/v1/me/library/music-videos/i.V7B9dQLsZ8DZKe",
            "attributes": {
                "releaseDate": "2021-02-12",
                "artistName": "Dua Lipa",
                "genreNames": [
                    "Pop"
                ],
                "trackNumber": 0,
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video124/v4/3f/1e/6f/3f1e6f35-6960-3f0e-0a0c-8701aa2012d4/dj.bcvxpufw.jpg/{w}x{h}bb.jpg"
                },
                "durationInMillis": 191913,
                "playParams": {
                    "id": "i.V7B9dQLsZ8DZKe",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1553279848"
                },
                "name": "We’re Good"
            }
        }
    ],
    "meta": {
        "total": 5
    }
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/music-videos`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryMusicVideos](librarymusicvideos.md)
  A resource object that represents a library music video.
- [object LibraryMusicVideosResponse](librarymusicvideosresponse.md)
  The response to a library music videos request.
- [Get a Library Music Video](get-a-library-music-video.md)
  Fetch a library music video by using its identifier.
- [Get a Library Music Video's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-419dz.md)
  Fetch a library music video’s relationship by using its identifier.
- [Get Multiple Library Music Videos](get-multiple-library-music-videos.md)
  Fetch one or more library music videos by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-library-music-videos)*