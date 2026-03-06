# MusicVideos.Views

**Framework**: Apple Music API  
**Kind**: dictionary

The views for a music video resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Views
```

## Topics

### Related Objects
- [object MusicVideos.Views.MusicVideosMoreByArtistView](musicvideos/views-data.dictionary/musicvideosmorebyartistview.md)
  A relationship view from this music video to more music videos of various types by the artist.
- [object MusicVideos.Views.MusicVideosMoreInGenreView](musicvideos/views-data.dictionary/musicvideosmoreingenreview.md)
  A relationship view from this music video to more music videos in a specific music video genre.

## Properties

- `more-by-artist` (MusicVideos.Views.MusicVideosMoreByArtistView): More music videos of some type by the artist. Fetch limits: 15 default, 100 maximum.
- `more-in-genre` (MusicVideos.Views.MusicVideosMoreInGenreView): More music videos in the given music video genre. Fetch limits: 15 default, 100 maximum.

## See Also

- [object MusicVideos.Attributes](musicvideos/attributes-data.dictionary.md)
  The attributes for a music video resource.
- [object MusicVideos.Relationships](musicvideos/relationships-data.dictionary.md)
  The relationships for a music video resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/views-data.dictionary)*