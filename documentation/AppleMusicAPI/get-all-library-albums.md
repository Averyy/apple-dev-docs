# Get All Library Albums

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the library albums in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/albums
```

**Response**:

```json
{
    "next": "/v1/me/library/albums?offset=2",
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
                "playParams": {
                    "id": "l.sticiFl",
                    "kind": "album",
                    "isLibrary": true
                },
                "dateAdded": "2022-08-06T02:18:57Z"
            }
        },
        {
            "id": "l.OGRixf5",
            "type": "library-albums",
            "href": "/v1/me/library/albums/l.OGRixf5",
            "attributes": {
                "trackCount": 14,
                "genreNames": [
                    "Alternative"
                ],
                "releaseDate": "2022-03-12",
                "name": "Dance Fever",
                "artistName": "Florence + the Machine",
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/93/ce/c5/93cec50d-bb01-3a42-364a-54af31cd73c7/22UMGIM23127.rgb.jpg/{w}x{h}bb.jpg"
                },
                "playParams": {
                    "id": "l.OGRixf5",
                    "kind": "album",
                    "isLibrary": true
                },
                "dateAdded": "2022-08-06T02:18:51Z"
            }
        }
    ],
    "meta": {
        "total": 10
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/albums`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryAlbums](libraryalbums.md)
  A resource object that represents a library album.
- [object LibraryAlbumsResponse](libraryalbumsresponse.md)
  The response to a library albums request.
- [Get a Library Album](get-a-library-album.md)
  Fetch a library album by using its identifier.
- [Get a Library Album's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-165fz.md)
  Fetch a library album’s relationship by using its identifier.
- [Get Multiple Library Albums](get-multiple-library-albums.md)
  Fetch one or more library albums by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-library-albums)*