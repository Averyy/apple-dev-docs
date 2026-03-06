# Get a Library Song's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library song’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/songs/i.PkdJNdAIrQozOW/albums
```

**Response**:

```json
{    
    "data": [
        {
            "id": "l.fsnYeFy",
            "type": "library-albums",
            "href": "/v1/me/library/albums/l.fsnYeFy",
            "attributes": {
                "trackCount": 1,
                "genreNames": [
                    "Latin"
                ],
                "releaseDate": "2022-05-06",
                "name": "Un Verano Sin Ti",
                "artistName": "Bad Bunny",
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/3e/04/eb/3e04ebf6-370f-f59d-ec84-2c2643db92f1/196626945068.jpg/{w}x{h}bb.jpg"
                },
                "playParams": {
                    "id": "l.fsnYeFy",
                    "kind": "album",
                    "isLibrary": true
                },
                "dateAdded": "2022-08-06T02:51:42Z"
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/songs/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibrarySongs](librarysongs.md)
  A resource object that represents a library song.
- [object LibrarySongsResponse](librarysongsresponse.md)
  The response to a library songs request.
- [Get a Library Song](get-a-library-song.md)
  Fetch a library song by using its identifier.
- [Get Multiple Library Songs](get-multiple-library-songs.md)
  Fetch one or more library songs by using their identifiers.
- [Get All Library Songs](get-all-library-songs.md)
  Fetch all the library songs in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-9xvg6)*