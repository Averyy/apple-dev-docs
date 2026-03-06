# MusicVideos.Relationships.MusicVideosArtistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the music video to its artists.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Relationships.MusicVideosArtistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Artists]) *(required)*: The artists associated with the music video.

## See Also

- [object MusicVideos.Relationships.MusicVideosAlbumsRelationship](musicvideos/relationships-data.dictionary/musicvideosalbumsrelationship.md)
  A relationship from the music video to its albums.
- [object MusicVideos.Relationships.MusicVideosGenresRelationship](musicvideos/relationships-data.dictionary/musicvideosgenresrelationship.md)
  A relationship from the music video to its genres.
- [object MusicVideos.Relationships.MusicVideosLibraryRelationship](musicvideos/relationships-data.dictionary/musicvideoslibraryrelationship.md)
  A relationship from the music video to its library.
- [object MusicVideos.Relationships.MusicVideosSongsRelationship](musicvideos/relationships-data.dictionary/musicvideossongsrelationship.md)
  A relationship from the music video to its songs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/relationships-data.dictionary/musicvideosartistsrelationship)*