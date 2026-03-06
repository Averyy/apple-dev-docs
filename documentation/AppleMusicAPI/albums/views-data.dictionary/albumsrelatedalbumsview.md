# Albums.Views.AlbumsRelatedAlbumsView

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship view from this album to related and similar albums.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Albums.Views.AlbumsRelatedAlbumsView
```

## Topics

### Related Objects
- [object Albums.Views.AlbumsRelatedAlbumsView.Attributes](albums/views-data.dictionary/albumsrelatedalbumsview/attributes-data.dictionary.md)
  The attributes for the view.

## Properties

- `href` (string): The relative location to fetch the view directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `attributes` (Albums.Views.AlbumsRelatedAlbumsView.Attributes) *(required)*: The attributes for the view.
- `data` ([Albums]) *(required)*: A collection of other albums related or similar to the album.

## See Also

- [object Albums.Views.AlbumsAppearsOnView](albums/views-data.dictionary/albumsappearsonview.md)
  A relationship view from this album to a selection of playlists tracks from this album appear on.
- [object Albums.Views.AlbumsOtherVersionsView](albums/views-data.dictionary/albumsotherversionsview.md)
  A relationship view for other versions of this album.
- [object Albums.Views.AlbumsRelatedVideosView](albums/views-data.dictionary/albumsrelatedvideosview.md)
  A relationship view from this album to music videos for the songs on the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/views-data.dictionary/albumsrelatedalbumsview)*