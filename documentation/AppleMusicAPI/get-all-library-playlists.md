# Get All Library Playlists

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the library playlists in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

## See Also

- [object LibraryPlaylists](libraryplaylists.md)
  A resource object that represents a library playlist.
- [object LibraryPlaylistsResponse](libraryplaylistsresponse.md)
  The response to a library playlists request.
- [Get a Library Playlist](get-a-library-playlist.md)
  Fetch a library playlist by using its identifier.
- [Get a Library Playlist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-5l22w.md)
  Fetch a library playlist’s relationship by using its identifier.
- [Get Multiple Library Playlists](get-multiple-library-playlists.md)
  Fetch one or more library playlists by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-library-playlists)*