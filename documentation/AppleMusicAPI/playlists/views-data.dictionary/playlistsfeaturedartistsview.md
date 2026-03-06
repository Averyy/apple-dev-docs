# Playlists.Views.PlaylistsFeaturedArtistsView

**Framework**: Apple Music API  
**Kind**: dictionary

Artists that are featured on this playlist.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Playlists.Views.PlaylistsFeaturedArtistsView
```

## Topics

### Related Objects
- [object Playlists.Views.PlaylistsFeaturedArtistsView.Attributes](playlists/views-data.dictionary/playlistsfeaturedartistsview/attributes-data.dictionary.md)
  Attribute metadata for the playlist featured artists view.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (Playlists.Views.PlaylistsFeaturedArtistsView.Attributes) *(required)*: The attribute metadata for the view.
- `data` ([Artists]) *(required)*: A paginated collection of resources in the view.

## See Also

- [object Playlists.Views.PlaylistsMoreByCuratorView](playlists/views-data.dictionary/playlistsmorebycuratorview.md)
  Additional content by the same curator for this playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/playlists/views-data.dictionary/playlistsfeaturedartistsview)*