# LibraryPlaylistCreationRequest.Relationships.Tracks

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The songs and music videos to add to the created playlist’s tracklist.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibraryPlaylistCreationRequest.Relationships.Tracks
```

## Topics

### Related Objects
- [object LibraryPlaylistCreationRequest.Relationships.Tracks.Data](./tracks-data.dictionary/data-data.dictionary.md)
  Data of the tracks too add to the created library playlist.

## Properties

- `data` ([LibraryPlaylistCreationRequest.Relationships.Tracks.Data]) *(required)*: A dictionary that includes strings for the `identifier` and `type` of the new playlist.

## See Also

### Related Objects
- [object LibraryPlaylistCreationRequest.Relationships.Parent](./parent-data.dictionary.md)
  Library playlist folder which contains the playlist that the user creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylistcreationrequest/relationships-data.dictionary/tracks-data.dictionary)*