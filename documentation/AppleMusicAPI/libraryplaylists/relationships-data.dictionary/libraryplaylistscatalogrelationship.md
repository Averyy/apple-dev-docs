# LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the playlist to its associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Playlists]) *(required)*: The playlist from the Apple Music catalog associated with the library playlist, if any.

## See Also

### Related Objects
- [object LibraryPlaylists.Relationships.LibraryPlaylistsTracksRelationship](./libraryplayliststracksrelationship.md)
  A relationship from the playlist to its tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylists/relationships-data.dictionary/libraryplaylistscatalogrelationship)*