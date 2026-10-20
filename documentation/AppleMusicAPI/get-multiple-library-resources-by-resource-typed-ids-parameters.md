# Get Multiple Library Resources Using Resource-Typed ID Parameters

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch one or more library resources by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [User Authentication for MusicKit](./user-authentication-for-musickit.md).

##### Example

**Request**:

```
https://api.music.apple.com/v1/me/library?ids[library-songs]=i.gelNOzPuL41Lxo
```

**Response**:

```json
{
    "data": [
        {
            "id": "i.gelNOzPuL41Lxo",
            "type": "library-songs",
            "href": "/v1/me/library/songs/i.gelNOzPuL41Lxo",
            "attributes": {
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Music115/v4/2d/f3/c9/2df3c9fd-e0eb-257c-c035-b04f05a66580/21UMGIM36691.rgb.jpg/{w}x{h}bb.jpeg",
                    "hasP3": false
                },
                "artistName": "Billie Eilish",
                "discNumber": 1,
                "genreNames": [
                    "Alternative"
                ],
                "durationInMillis": 298899,
                "releaseDate": "2021-07-30",
                "name": "Happier Than Ever",
                "hasLyrics": true,
                "albumName": "Happier Than Ever",
                "playParams": {
                    "id": "i.gelNOzPuL41Lxo",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1564531202"
                },
                "trackNumber": 15,
                "contentRating": "explicit"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/library`

## Parameters

### Query Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `ids[library-songs]` ([string]): The unique identifiers for the library songs.
- `ids[library-playlists]` ([string]): The unique identifiers for the library playlists.
- `ids[library-playlist-folders]` ([string]): The unique identifiers for the library playlist folders.
- `ids[library-music-videos]` ([string]): The unique identifiers for the library music videos.
- `ids[library-artists]` ([string]): The unique identifiers for the library artists.
- `ids[library-albums]` ([string]): The unique identifiers for the library albums.

## Responses

- `200` OK (`ResourceCollectionResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Resource](./resource.md)
  A resource—such as an album, song, or playlist.
### Fetching Multiple Resource Types
- [Get Multiple Catalog Resources Using Resource-Typed ID Parameters](./get-multiple-catalog-resources-by-resource-typed-ids-parameters.md)
  Fetch one or more catalog resources by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-library-resources-by-resource-typed-ids-parameters)*