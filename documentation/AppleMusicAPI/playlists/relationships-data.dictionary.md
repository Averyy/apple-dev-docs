# Playlists.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The relationships for a playlist resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Relationships
```

## Topics

### Related Objects
- [object Playlists.Relationships.PlaylistsCuratorRelationship](./relationships-data.dictionary/playlistscuratorrelationship.md)
  A relationship from the playlist to its curator.
- [object Playlists.Relationships.PlaylistsTracksRelationship](./relationships-data.dictionary/playliststracksrelationship.md)
  A relationship from the playlist to its tracks.
- [object Playlists.Relationships.PlaylistsLibraryRelationship](./relationships-data.dictionary/playlistslibraryrelationship.md)
  A relationship from the playlist to its library.

## Properties

- `curator` (Playlists.Relationships.PlaylistsCuratorRelationship): The curator that created the playlist. By default, `curator` includes identifiers only.

  Fetch limits: None
- `library` (Playlists.Relationships.PlaylistsLibraryRelationship): Library playlist for a catalog playlist if added to library.
- `tracks` (Playlists.Relationships.PlaylistsTracksRelationship): The songs and music videos included in the playlist. By default, `tracks` includes objects.

  Fetch limits: 100 default, 300 maximum

## See Also

### Related Objects
- [object Playlists.Attributes](./attributes-data.dictionary.md)
  The attributes for a playlist resource.
- [object Playlists.Views](./views-data.dictionary.md)
  The views for a music video resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/relationships-data.dictionary)*