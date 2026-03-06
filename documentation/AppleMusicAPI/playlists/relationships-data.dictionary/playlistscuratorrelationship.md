# Playlists.Relationships.PlaylistsCuratorRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the playlist to its curator.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Playlists.Relationships.PlaylistsCuratorRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([*]) *(required)*: The curator for the playlist.

## See Also

- [object Playlists.Relationships.PlaylistsTracksRelationship](playlists/relationships-data.dictionary/playliststracksrelationship.md)
  A relationship from the playlist to its tracks.
- [object Playlists.Relationships.PlaylistsLibraryRelationship](playlists/relationships-data.dictionary/playlistslibraryrelationship.md)
  A relationship from the playlist to its library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/relationships-data.dictionary/playlistscuratorrelationship)*