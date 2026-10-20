# Playlists.Views.PlaylistsMoreByCuratorView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

Additional content by the same curator for this playlist.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Views.PlaylistsMoreByCuratorView
```

## Topics

### Related Objects
- [object Playlists.Views.PlaylistsMoreByCuratorView.Attributes](./playlistsmorebycuratorview/attributes-data.dictionary.md)
  Attribute metadata for the view containing additional content by the same curator for this playlist.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (Playlists.Views.PlaylistsMoreByCuratorView.Attributes) *(required)*: The attribute metadata for the view.
- `data` ([Playlists]) *(required)*: A paginated collection of resources in the view.

## See Also

### Related Objects
- [object Playlists.Views.PlaylistsFeaturedArtistsView](./playlistsfeaturedartistsview.md)
  Artists that are featured on this playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/views-data.dictionary/playlistsmorebycuratorview)*