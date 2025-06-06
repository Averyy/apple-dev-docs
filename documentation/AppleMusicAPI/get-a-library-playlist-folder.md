# Get a Library Playlist Folder

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a library playlist folder by using its identifier.

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
- [Get Root Library Playlists Folder](get-root-library-playlists-folder.md)
  Fetch the root library playlists folder for the user.
- [Get a Library Playlist Folder’s Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-r5gv.md)
  Fetch a library playlist folder’s relationship by using its identifier.
- [Get Multiple Library Playlist Folders](get-multiple-library-playlist-folders.md)
  Fetch one or more library playlist folders by using their identifiers.
- [Create a New Library Playlist Folder](create-a-new-library-playlist-folder.md)
  Create a new playlist folder in a user’s library.
- [object LibraryPlaylistFolderCreationRequest](libraryplaylistfoldercreationrequest.md)
  Request object to create a new library playlist folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-library-playlist-folder)*