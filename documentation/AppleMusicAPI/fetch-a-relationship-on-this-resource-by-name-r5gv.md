# Get a Library Playlist Folder’s Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library playlist folder’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/playlist-folders/p.WmzVVDOUO9pDBk/children
```

**Response**:

```json
{    
    "data": [
        {
            "id": "p.RB1AA8bCv74Zkl",
            "type": "library-playlists",
            "href": "/v1/me/library/playlists/p.RB1AA8bCv74Zkl",
            "attributes": {
                "description": {
                    "standard": ""
                },
                "dateAdded": "2021-12-03T19: 06: 29Z",
                "hasCatalog": true,
                "isPublic": false,
                "playParams": {
                    "id": "p.RB1AA8bCv74Zkl",
                    "kind": "playlist",
                    "isLibrary": true,
                    "globalId": "pl.u-jV8990gT3bLqrj"
                },
                "name": "Chill JPop",
                "canEdit": true
            }
        },
        {
            "id": "p.eoGxpgbtxAPJG6",
            "type": "library-playlists",
            "href": "/v1/me/library/playlists/p.eoGxpgbtxAPJG6",
            "attributes": {
                "description": {
                    "standard": ""
                },
                "dateAdded": "2021-09-02T18: 43: 15Z",
                "hasCatalog": true,
                "isPublic": true,
                "playParams": {
                    "id": "p.eoGxpgbtxAPJG6",
                    "kind": "playlist",
                    "isLibrary": true,
                    "globalId": "pl.u-WabZ6rRCYW2vBE"
                },
                "name": "Chill Tracks Instrumental",
                "canEdit": true
            }
        },
        {
            "id": "p.4Y0JJrJuMWkD60",
            "type": "library-playlists",
            "href": "/v1/me/library/playlists/p.4Y0JJrJuMWkD60",
            "attributes": {
                "description": {
                    "standard": ""
                },
                "dateAdded": "2022-03-10T02: 26: 39Z",
                "hasCatalog": true,
                "isPublic": false,
                "playParams": {
                    "id": "p.4Y0JJrJuMWkD60",
                    "kind": "playlist",
                    "isLibrary": true,
                    "globalId": "pl.u-kv9llBlC6XZWBv"
                },
                "name": "Chill Tracks w/ Vocals",
                "canEdit": true
            }
        }
    ],
    "meta": {
        "total": 3
    }
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/playlist-folders/{id}/{relationship}`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibraryPlaylists](libraryplaylists.md)
  A resource object that represents a library playlist.
- [object LibraryPlaylistsResponse](libraryplaylistsresponse.md)
  The response to a library playlists request.
- [Get Root Library Playlists Folder](get-root-library-playlists-folder.md)
  Fetch the root library playlists folder for the user.
- [Get a Library Playlist Folder](get-a-library-playlist-folder.md)
  Fetch a library playlist folder by using its identifier.
- [Get Multiple Library Playlist Folders](get-multiple-library-playlist-folders.md)
  Fetch one or more library playlist folders by using their identifiers.
- [Create a New Library Playlist Folder](create-a-new-library-playlist-folder.md)
  Create a new playlist folder in a user’s library.
- [object LibraryPlaylistFolderCreationRequest](libraryplaylistfoldercreationrequest.md)
  Request object to create a new library playlist folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-r5gv)*