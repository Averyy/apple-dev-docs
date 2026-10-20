# MusicVideos.Views.MusicVideosMoreInGenreView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship view from this music video to more music videos in a specific music video genre.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object MusicVideos.Views.MusicVideosMoreInGenreView
```

## Topics

### Related Objects
- [object MusicVideos.Views.MusicVideosMoreInGenreView.Attributes](./musicvideosmoreingenreview/attributes-data.dictionary.md)
  More music videos in a specific music video genre.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (MusicVideos.Views.MusicVideosMoreInGenreView.Attributes) *(required)*: The attributes for the view.
- `data` ([MusicVideos]) *(required)*: Music videos in the given music video genre.

## See Also

### Related Objects
- [object MusicVideos.Views.MusicVideosMoreByArtistView](./musicvideosmorebyartistview.md)
  A relationship view from this music video to more music videos of various types by the artist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/views-data.dictionary/musicvideosmoreingenreview)*