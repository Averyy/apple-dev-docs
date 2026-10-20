# LibraryPlaylistCreationRequest.Relationships.Tracks.Data

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

Data of the tracks too add to the created library playlist.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibraryPlaylistCreationRequest.Relationships.Tracks.Data
```

## Properties

- `id` (string) *(required)*: The unique identifier for the track. This ID can be a catalog identifier or a library identifier, depending on the track type.
- `type` (string) *(required)*: The type of the track to be added.

  **Allowed Values**: `library-music-videos`, `library-songs`, `music-videos`, `songs`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylistcreationrequest/relationships-data.dictionary/tracks-data.dictionary/data-data.dictionary)*