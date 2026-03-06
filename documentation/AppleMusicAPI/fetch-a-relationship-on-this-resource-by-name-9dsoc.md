# Get a Library Artist's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library artist’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/artists/r.y8mMT7t/albums
```

**Response**:

```json
{
    "data": [
        {
            "id": "l.sticiFl",
            "type": "library-albums",
            "href": "/v1/me/library/albums/l.sticiFl",
            "attributes": {
                "trackCount": 15,
                "genreNames": [
                    "Country"
                ],
                "releaseDate": "2022-02-11",
                "name": "Bronco",
                "artistName": "Orville Peck",
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is3-ssl.mzstatic.com/image/thumb/Music116/v4/6d/de/02/6dde02ae-a9fe-f96e-e81f-4f18ad13d2f9/886449873302.jpg/{w}x{h}bb.jpg"
                },
                "dateAdded": "2022-08-06T02:18:57Z",
                "playParams": {
                    "id": "l.sticiFl",
                    "kind": "album",
                    "isLibrary": true
                }
            }
        }
    ],
    "meta": {
        "total": 1
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/artists/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryArtists](libraryartists.md)
  A resource object that represents an artist present in a user’s library.
- [object LibraryArtistsResponse](libraryartistsresponse.md)
  The response to a library artists request.
- [Get a Library Artist](get-a-library-artist.md)
  Fetch a library artist by using its identifier.
- [Get Multiple Library Artists](get-multiple-library-artists.md)
  Fetch one or more library artists by using their identifiers.
- [Get All Library Artists](get-all-library-artists.md)
  Fetch all the library artists in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-9dsoc)*