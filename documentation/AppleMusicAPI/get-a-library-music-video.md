# Get a Library Music Video

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch a library music video by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [User Authentication for MusicKit](./user-authentication-for-musickit.md).

##### Example

**Request**:

```
https://api.music.apple.com/v1/me/library/music-videos/i.V7B9dQLsZ8DZKe
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
                "name": "We’re Good",
                "trackNumber": 0,
                "playParams": {
                    "id": "i.V7B9dQLsZ8DZKe",
                    "kind": "musicVideo",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1553279848"
                },
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Video124/v4/3f/1e/6f/3f1e6f35-6960-3f0e-0a0c-8701aa2012d4/dj.bcvxpufw.jpg/{w}x{h}bb.jpg"
                },
                "artistName": "Dua Lipa",
                "durationInMillis": 191913,
                "releaseDate": "2021-02-12",
                "genreNames": [
                    "Pop"
                ]
            }
        }
    ]
}


```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/music-videos/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the library music video.

### Query Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## Responses

- `200` OK (`LibraryMusicVideosResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object LibraryMusicVideos](./librarymusicvideos.md)
  A resource object that represents a library music video.
- [object LibraryMusicVideosResponse](./librarymusicvideosresponse.md)
  The response to a library music videos request.
### Requesting a Library Music Video
- [Get a Library Music Video's Relationship Directly by Name](./fetch-a-relationship-on-this-resource-by-name-419dz.md)
  Fetch a library music video’s relationship by using its identifier.
- [Get Multiple Library Music Videos](./get-multiple-library-music-videos.md)
  Fetch one or more library music videos by using their identifiers.
- [Get All Library Music Videos](./get-all-library-music-videos.md)
  Fetch all the library music videos in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-library-music-video)*