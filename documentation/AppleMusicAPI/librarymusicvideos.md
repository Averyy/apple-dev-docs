# LibraryMusicVideos

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a library music video.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryMusicVideos
```

## Topics

### Related Objects
- [object LibraryMusicVideos.Attributes](librarymusicvideos/attributes-data.dictionary.md)
  The attributes for the library music videos resource type.
- [object LibraryMusicVideos.Relationships](librarymusicvideos/relationships-data.dictionary.md)
  The relationships from library music videos to other resources.

## Properties

- `id` (string) *(required)*: The identifier for the library music video.
- `type` (string) *(required)*: This value is always `library-music-videos`.
- `href` (string) *(required)*: The relative location for the library music video resource.
- `attributes` (LibraryMusicVideos.Attributes): The attributes for the library music video.
- `relationships` (LibraryMusicVideos.Relationships): The relationships for the library music video.

## See Also

- [object MusicVideos](musicvideos.md)
  A resource object that represents a music video.
- [object MusicVideosResponse](musicvideosresponse.md)
  The response to a music videos request.
- [object LibraryMusicVideosResponse](librarymusicvideosresponse.md)
  The response to a library music videos request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarymusicvideos)*