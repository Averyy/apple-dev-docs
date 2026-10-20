# LibraryPlaylistCreationRequest.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The relationships for a library playlist creation request object.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibraryPlaylistCreationRequest.Relationships
```

## Topics

### Related Objects
- [object LibraryPlaylistCreationRequest.Relationships.Parent](./relationships-data.dictionary/parent-data.dictionary.md)
  Library playlist folder which contains the playlist that the user creates.
- [object LibraryPlaylistCreationRequest.Relationships.Tracks](./relationships-data.dictionary/tracks-data.dictionary.md)
  The songs and music videos to add to the created playlist’s tracklist.

## Properties

- `tracks` (LibraryPlaylistCreationRequest.Relationships.Tracks) *(required)*: The songs and music videos the user adds to the playlist for the creation request.
- `parent` (LibraryPlaylistCreationRequest.Relationships.Parent) *(required)*: The library playlist folder which contains the created playlist.

## See Also

### Related Objects
- [object LibraryPlaylistCreationRequest.Attributes](./attributes-data.dictionary.md)
  The attributes for a library playlist creation request object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylistcreationrequest/relationships-data.dictionary)*