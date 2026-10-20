# MusicVideos.Views.MusicVideosMoreByArtistView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship view from this music video to more music videos of various types by the artist.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object MusicVideos.Views.MusicVideosMoreByArtistView
```

## Topics

### Related Objects
- [object MusicVideos.Views.MusicVideosMoreByArtistView.Attributes](./musicvideosmorebyartistview/attributes-data.dictionary.md)
  More content of some other type by the artist.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (MusicVideos.Views.MusicVideosMoreByArtistView.Attributes) *(required)*: The attributes for the view.
- `data` ([MusicVideos]) *(required)*: Music videos of some type by the artist.

## See Also

### Related Objects
- [object MusicVideos.Views.MusicVideosMoreInGenreView](./musicvideosmoreingenreview.md)
  A relationship view from this music video to more music videos in a specific music video genre.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/views-data.dictionary/musicvideosmorebyartistview)*