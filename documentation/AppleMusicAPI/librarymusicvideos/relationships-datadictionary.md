# LibraryMusicVideos.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships from library music videos to other resources.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryMusicVideos.Relationships
```

## Topics

### Related Objects
- [object LibraryMusicVideos.Relationships.LibraryMusicVideosAlbumsRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideosalbumsrelationship.md)
  A relationship from the library music video to its albums in the library.
- [object LibraryMusicVideos.Relationships.LibraryMusicVideosArtistsRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideosartistsrelationship.md)
  A relationship from the library music video to its artists in the library.
- [object LibraryMusicVideos.Relationships.LibraryMusicVideosCatalogRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideoscatalogrelationship.md)
  A relationship from the library music video to its associated catalog content.

## Properties

- `albums` (LibraryMusicVideos.Relationships.LibraryMusicVideosAlbumsRelationship): The library albums associated with the music video. By default, `albums` not included. Fetch limits: 10 default, 10 maximum.
- `artists` (LibraryMusicVideos.Relationships.LibraryMusicVideosArtistsRelationship): The library artists associated with the music video. By default, `artists` not included. Fetch limits: 10 default, 10 maximum.
- `catalog` (LibraryMusicVideos.Relationships.LibraryMusicVideosCatalogRelationship): The music video in the Apple Music catalog the library music video is associated with, when known. Fetch limits: None (associated with at most one catalog music video).

## See Also

- [object LibraryMusicVideos.Attributes](librarymusicvideos/attributes-data.dictionary.md)
  The attributes for the library music videos resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarymusicvideos/relationships-data.dictionary)*