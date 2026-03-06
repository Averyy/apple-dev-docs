# LibraryMusicVideos.Relationships.LibraryMusicVideosAlbumsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library music video to its albums in the library.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryMusicVideos.Relationships.LibraryMusicVideosAlbumsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryAlbums]) *(required)*: The albums in the library the music video is associated with, if any.

## See Also

- [object LibraryMusicVideos.Relationships.LibraryMusicVideosArtistsRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideosartistsrelationship.md)
  A relationship from the library music video to its artists in the library.
- [object LibraryMusicVideos.Relationships.LibraryMusicVideosCatalogRelationship](librarymusicvideos/relationships-data.dictionary/librarymusicvideoscatalogrelationship.md)
  A relationship from the library music video to its associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarymusicvideos/relationships-data.dictionary/librarymusicvideosalbumsrelationship)*