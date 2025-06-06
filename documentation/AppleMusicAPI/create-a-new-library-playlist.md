# Create a New Library Playlist

**Framework**: Apple Music API  
**Kind**: httpRequest

Create a new playlist in a user’s library.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 201 (Created) and a new resource created as a result. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

> **Note**:  There may be a delay before a new resource appears in a user’s library.

 There may be a delay before a new resource appears in a user’s library.

You can include an optional `tracks` relationship in this request.

##### Example

## Request Body

The `POST` request containing the `name` `tracks` and `parent` playlist folder for the playlist to be added.

## See Also

- [object LibraryPlaylists](libraryplaylists.md)
  A resource object that represents a library playlist.
- [object LibraryPlaylistsResponse](libraryplaylistsresponse.md)
  The response to a library playlists request.
- [Add Tracks to a Library Playlist](add-tracks-to-a-library-playlist.md)
  Add new tracks to the end of a library playlist.
- [Add a Resource to a Library](add-a-resource-to-a-library.md)
  Add a catalog resource to a user’s iCloud Music Library.
- [object LibraryPlaylistCreationRequest](libraryplaylistcreationrequest.md)
  A request to create a new playlist in a user’s library.
- [object LibraryPlaylistTracksRequest](libraryplaylisttracksrequest.md)
  A request to add tracks to a library playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/create-a-new-library-playlist)*