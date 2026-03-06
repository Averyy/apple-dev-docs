# LibraryMusicVideos.Relationships.LibraryMusicVideosArtistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library music video to its artists in the library.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryMusicVideos.Relationships.LibraryMusicVideosArtistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryArtists]) *(required)*: The artists in the library the music video is associated with.

## See Also

- [object LibraryMusicVideos.Relationships.LibraryMusicVideosAlbumsRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideosalbumsrelationship.md)
  A relationship from the library music video to its albums in the library.
- [object LibraryMusicVideos.Relationships.LibraryMusicVideosCatalogRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideoscatalogrelationship.md)
  A relationship from the library music video to its associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarymusicvideos/relationships-data.dictionary/librarymusicvideosartistsrelationship)*