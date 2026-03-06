# MusicVideos

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a music video.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos
```

## Topics

### Related Objects
- [object MusicVideos.Attributes](musicvideos/attributes-data.dictionary.md)
  The attributes for a music video resource.
- [object MusicVideos.Relationships](musicvideos/relationships-data.dictionary.md)
  The relationships for a music video resource.
- [object MusicVideos.Views](musicvideos/views-data.dictionary.md)
  The views for a music video resource.

## Properties

- `id` (string) *(required)*: The identifier for the music video.
- `type` (string) *(required)*: This value is always `music-videos`.
- `href` (string) *(required)*: The relative location for the music video resource.
- `attributes` (MusicVideos.Attributes): The attributes for the music video.
- `relationships` (MusicVideos.Relationships): The relationships for the music video.
- `views` (MusicVideos.Views): The relationship views for the music video.

## See Also

- [object MusicVideosResponse](musicvideosresponse.md)
  The response to a music videos request.
- [object LibraryMusicVideos](librarymusicvideos.md)
  A resource object that represents a library music video.
- [object LibraryMusicVideosResponse](librarymusicvideosresponse.md)
  The response to a library music videos request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos)*