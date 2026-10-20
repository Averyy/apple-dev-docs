# Playlists.Relationships.PlaylistsCuratorRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the playlist to its curator.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Relationships.PlaylistsCuratorRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([*]) *(required)*: The curator for the playlist.

  **Allowed Types**: `Activities`, `AppleCurators`, `Curators`

## See Also

### Related Objects
- [object Playlists.Relationships.PlaylistsTracksRelationship](./playliststracksrelationship.md)
  A relationship from the playlist to its tracks.
- [object Playlists.Relationships.PlaylistsLibraryRelationship](./playlistslibraryrelationship.md)
  A relationship from the playlist to its library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/relationships-data.dictionary/playlistscuratorrelationship)*