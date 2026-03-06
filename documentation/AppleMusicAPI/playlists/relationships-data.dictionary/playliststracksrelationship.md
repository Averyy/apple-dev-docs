# Playlists.Relationships.PlaylistsTracksRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the playlist to its tracks.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Playlists.Relationships.PlaylistsTracksRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([*]) *(required)*: The ordered songs and music videos in the tracklist of the playlist.

## See Also

- [object Playlists.Relationships.PlaylistsCuratorRelationship](playlists/relationships-data.dictionary/playlistscuratorrelationship.md)
  A relationship from the playlist to its curator.
- [object Playlists.Relationships.PlaylistsLibraryRelationship](playlists/relationships-data.dictionary/playlistslibraryrelationship.md)
  A relationship from the playlist to its library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/relationships-data.dictionary/playliststracksrelationship)*