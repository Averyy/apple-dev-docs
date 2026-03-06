# MusicVideos.Views.MusicVideosMoreByArtistView

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship view from this music video to more music videos of various types by the artist.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Views.MusicVideosMoreByArtistView
```

## Topics

### Related Objects
- [object MusicVideos.Views.MusicVideosMoreByArtistView.Attributes](musicvideos/views-data.dictionary/musicvideosmorebyartistview/attributes-data.dictionary.md)
  More content of some other type by the artist.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (MusicVideos.Views.MusicVideosMoreByArtistView.Attributes) *(required)*: The attributes for the view.
- `data` ([MusicVideos]) *(required)*: Music videos of some type by the artist.

## See Also

- [object MusicVideos.Views.MusicVideosMoreInGenreView](musicvideos/views-data.dictionary/musicvideosmoreingenreview.md)
  A relationship view from this music video to more music videos in a specific music video genre.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/views-data.dictionary/musicvideosmorebyartistview)*