# Get Multiple Library Artists

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more library artists by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/artists?ids=r.y8mMT7t
```

**Response**:

```json
{
    "data": [
        {
            "id": "r.y8mMT7t",
            "type": "library-artists",
            "href": "/v1/me/library/artists/r.y8mMT7t",
            "attributes": {
                "name": "Orville Peck"
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/artists`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the artists. The maximum fetch limit is 25.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
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
- [Get All Library Artists](get-all-library-artists.md)
  Fetch all the library artists in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-library-artists)*