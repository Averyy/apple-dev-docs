# LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the playlist to its associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Playlists]) *(required)*: The playlist from the Apple Music catalog associated with the library playlist, if any.

## See Also

- [object LibraryPlaylists.Relationships.LibraryPlaylistsTracksRelationship](libraryplaylists/relationships-data.dictionary/libraryplayliststracksrelationship.md)
  A relationship from the playlist to its tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylists/relationships-data.dictionary/libraryplaylistscatalogrelationship)*