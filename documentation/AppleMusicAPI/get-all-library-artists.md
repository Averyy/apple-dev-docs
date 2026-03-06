# Get All Library Artists

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the library artists in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/artists
```

**Response**:

```json
{    
    "next": "/v1/me/library/artists?offset=2",
    "data": [
        {
            "id": "r.y8mMT7t",
            "type": "library-artists",
            "href": "/v1/me/library/artists/r.y8mMT7t",
            "attributes": {
                "name": "Orville Peck"
            }
        },
        {
            "id": "r.SvEnrEf",
            "type": "library-artists",
            "href": "/v1/me/library/artists/r.SvEnrEf",
            "attributes": {
                "name": "Florence + the Machine"
            }
        }
    ],
    "meta": {
        "total": 10
    }
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/artists`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryArtists](libraryartists.md)
  A resource object that represents an artist present in a user’s library.
- [object LibraryArtistsResponse](libraryartistsresponse.md)
  The response to a library artists request.
- [Get a Library Artist](get-a-library-artist.md)
  Fetch a library artist by using its identifier.
- [Get a Library Artist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-9dsoc.md)
  Fetch a library artist’s relationship by using its identifier.
- [Get Multiple Library Artists](get-multiple-library-artists.md)
  Fetch one or more library artists by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-library-artists)*