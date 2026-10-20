# Playlists.Views.PlaylistsFeaturedArtistsView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

Artists that are featured on this playlist.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Playlists.Views.PlaylistsFeaturedArtistsView
```

## Topics

### Related Objects
- [object Playlists.Views.PlaylistsFeaturedArtistsView.Attributes](./playlistsfeaturedartistsview/attributes-data.dictionary.md)
  Attribute metadata for the playlist featured artists view.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (Playlists.Views.PlaylistsFeaturedArtistsView.Attributes) *(required)*: The attribute metadata for the view.
- `data` ([Artists]) *(required)*: A paginated collection of resources in the view.

## See Also

### Related Objects
- [object Playlists.Views.PlaylistsMoreByCuratorView](./playlistsmorebycuratorview.md)
  Additional content by the same curator for this playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/views-data.dictionary/playlistsfeaturedartistsview)*