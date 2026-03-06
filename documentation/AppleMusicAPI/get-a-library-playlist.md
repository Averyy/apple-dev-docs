# Get a Library Playlist

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library playlist by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/playlists/p.ldvAAZ3C3Qmop9
```

**Response**:

```json
{
    "data": [
        {
            "id": "p.ldvAAZ3C3Qmop9",
            "type": "library-playlists",
            "href": "/v1/me/library/playlists/p.ldvAAZ3C3Qmop9",
            "attributes": {
                "playParams": {
                    "id": "p.ldvAAZ3C3Qmop9",
                    "kind": "playlist",
                    "isLibrary": true,
                    "globalId": "pl.cb4d1c09a2df4230a78d0395fe1f8fde"
                },
                "canEdit": false,
                "name": "Piano Chill",
                "description": {
                    "standard": "Discover the liberating power of the piano with pieces chosen by Dirk Maassen."
                },
                "dateAdded": "2021-09-30T00: 55: 48Z",
                "artwork": {
                    "width": null,
                    "height": null,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features125/v4/dc/47/7c/dc477c6f-9029-bd1c-8e89-87b04042a55b/U0MtTVMtV1ctUGlhbm9fQ2hpbGwtQURBTV9JRD0xMDcyODMxMzA0LnBuZw.png/{w}x{h}SC.DN01.jpeg"
                },
                "isPublic": false,
                "hasCatalog": true
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/playlists/{id}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryPlaylists](libraryplaylists.md)
  A resource object that represents a library playlist.
- [object LibraryPlaylistsResponse](libraryplaylistsresponse.md)
  The response to a library playlists request.
- [Get a Library Playlist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-5l22w.md)
  Fetch a library playlist’s relationship by using its identifier.
- [Get Multiple Library Playlists](get-multiple-library-playlists.md)
  Fetch one or more library playlists by using their identifiers.
- [Get All Library Playlists](get-all-library-playlists.md)
  Fetch all the library playlists in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-library-playlist)*