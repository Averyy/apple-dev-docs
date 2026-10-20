# LibraryPlaylistTracksRequest.Data

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

An object that represents a single track when added to a library playlist in a request.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibraryPlaylistTracksRequest.Data
```

## Properties

- `id` (string) *(required)*: The unique identifier of the library playlist track.
- `type` (string) *(required)*: The type of the track to be added. The possible values are `library-music-videos`, `library-songs`,  `music-videos`, or `songs`.

  **Allowed Values**: `library-music-videos`, `library-songs`, `music-videos`, `songs`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylisttracksrequest/data-data.dictionary)*