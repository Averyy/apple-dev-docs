# Playlists.Relationships.PlaylistsTracksRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the playlist to its tracks.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Relationships.PlaylistsTracksRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([*]) *(required)*: The ordered songs and music videos in the tracklist of the playlist.

  **Allowed Types**: `MusicVideos`, `Songs`

## See Also

### Related Objects
- [object Playlists.Relationships.PlaylistsCuratorRelationship](./playlistscuratorrelationship.md)
  A relationship from the playlist to its curator.
- [object Playlists.Relationships.PlaylistsLibraryRelationship](./playlistslibraryrelationship.md)
  A relationship from the playlist to its library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/relationships-data.dictionary/playliststracksrelationship)*