# Albums.Views.AlbumsOtherVersionsView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship view for other versions of this album.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Albums.Views.AlbumsOtherVersionsView
```

## Topics

### Related Objects
- [object Albums.Views.AlbumsOtherVersionsView.Attributes](./albumsotherversionsview/attributes-data.dictionary.md)
  The attributes for the view.

## Properties

- `href` (string): The relative location to fetch the view directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `attributes` (Albums.Views.AlbumsOtherVersionsView.Attributes) *(required)*: The attributes for the view.
- `data` ([Albums]) *(required)*: Other versions of the album.

## See Also

### Related Objects
- [object Albums.Views.AlbumsAppearsOnView](./albumsappearsonview.md)
  A relationship view from this album to a selection of playlists tracks from this album appear on.
- [object Albums.Views.AlbumsRelatedAlbumsView](./albumsrelatedalbumsview.md)
  A relationship view from this album to related and similar albums.
- [object Albums.Views.AlbumsRelatedVideosView](./albumsrelatedvideosview.md)
  A relationship view from this album to music videos for the songs on the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/views-data.dictionary/albumsotherversionsview)*