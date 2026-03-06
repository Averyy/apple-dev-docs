# LibraryPlaylistFolders

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a library playlist folder.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylistFolders
```

## Topics

### Related Objects
- [object LibraryPlaylistFolders.Attributes](libraryplaylistfolders/attributes-data.dictionary.md)
  A resource object that represents the attributes for a library playlist folder.
- [object LibraryPlaylistFolders.Relationships](libraryplaylistfolders/relationships-data.dictionary.md)
  A resource Object that represents the relationships for a library playlist folder.

## Properties

- `id` (string) *(required)*: The identifier for the library playlist folder.
- `type` (string) *(required)*: This value is always `library-playlist-folders`.
- `href` (string) *(required)*: The relative location for the library playlist folder resource.
- `attributes` (LibraryPlaylistFolders.Attributes): The attributes for the library-playlist-folders resource type.
- `relationships` (LibraryPlaylistFolders.Relationships): The relationships from library-playlist-folders to other resources.

## See Also

- [object Playlists](playlists.md)
  A resource object that represents a playlist.
- [object PlaylistsResponse](playlistsresponse.md)
  The response to a playlists request.
- [object LibraryPlaylists](libraryplaylists.md)
  A resource object that represents a library playlist.
- [object LibraryPlaylistsResponse](libraryplaylistsresponse.md)
  The response to a library playlists request.
- [object LibraryPlaylistsTracksRelationshipResponse](libraryplayliststracksrelationshipresponse.md)
  The response to a library playlists tracks relationship request.
- [object LibraryPlaylistFoldersResponse](libraryplaylistfoldersresponse.md)
  The response to a library playlist folders request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylistfolders)*