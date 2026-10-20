# Playlists.Relationships.PlaylistsLibraryRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the playlist to its library.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Relationships.PlaylistsLibraryRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryPlaylists]) *(required)*: The library for the playlist.

## See Also

### Related Objects
- [object Playlists.Relationships.PlaylistsCuratorRelationship](./playlistscuratorrelationship.md)
  A relationship from the playlist to its curator.
- [object Playlists.Relationships.PlaylistsTracksRelationship](./playliststracksrelationship.md)
  A relationship from the playlist to its tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/relationships-data.dictionary/playlistslibraryrelationship)*