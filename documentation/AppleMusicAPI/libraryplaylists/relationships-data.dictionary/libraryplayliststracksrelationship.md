# LibraryPlaylists.Relationships.LibraryPlaylistsTracksRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the playlist to its tracks.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylists.Relationships.LibraryPlaylistsTracksRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([*]) *(required)*: The ordered library songs and library music videos in the tracklist of the playlist.

## See Also

- [object LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship](libraryplaylists/relationships-data.dictionary/libraryplaylistscatalogrelationship.md)
  A relationship from the playlist to its associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylists/relationships-data.dictionary/libraryplayliststracksrelationship)*