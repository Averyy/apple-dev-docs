# Albums.Views.AlbumsRelatedVideosView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship view from this album to music videos for the songs on the album.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Albums.Views.AlbumsRelatedVideosView
```

## Topics

### Related Objects
- [object Albums.Views.AlbumsRelatedVideosView.Attributes](./albumsrelatedvideosview/attributes-data.dictionary.md)
  The attributes for the view.

## Properties

- `href` (string): The relative location to fetch the view directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `attributes` (Albums.Views.AlbumsRelatedVideosView.Attributes) *(required)*: The attributes for the view.
- `data` ([MusicVideos]) *(required)*: The music videos available for songs on the album.

## See Also

### Related Objects
- [object Albums.Views.AlbumsAppearsOnView](./albumsappearsonview.md)
  A relationship view from this album to a selection of playlists tracks from this album appear on.
- [object Albums.Views.AlbumsOtherVersionsView](./albumsotherversionsview.md)
  A relationship view for other versions of this album.
- [object Albums.Views.AlbumsRelatedAlbumsView](./albumsrelatedalbumsview.md)
  A relationship view from this album to related and similar albums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/views-data.dictionary/albumsrelatedvideosview)*