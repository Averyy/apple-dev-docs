# Get Multiple Library Music Videos

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more library music videos by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/music-videos?ids=i.V7B9dQLsZ8DZKe
```

**Response**:

```json
{
    "data": [
        {
            "id": "i.V7B9dQLsZ8DZKe",
            "type": "library-music-videos",
            "href": "/v1/me/library/music-videos/i.V7B9dQLsZ8DZKe",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Video124/v4/3f/1e/6f/3f1e6f35-6960-3f0e-0a0c-8701aa2012d4/dj.bcvxpufw.jpg/{w}x{h}bb.jpeg"
                },
                "releaseDate": "2021-02-12",
                "genreNames": [
                    "Pop"
                ],
                "playParams": {
                    "id": "i.V7B9dQLsZ8DZKe",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1553279848"
                },
                "trackNumber": 0,
                "name": "We’re Good",
                "durationInMillis": 191913,
                "artistName": "Dua Lipa"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/music-videos`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the library music videos. The maximum fetch limit is 100. For possible values, get all the library music videos by sending this endpoint without the `ids` parameter.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
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
- [Get All Library Music Videos](get-all-library-music-videos.md)
  Fetch all the library music videos in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-library-music-videos)*