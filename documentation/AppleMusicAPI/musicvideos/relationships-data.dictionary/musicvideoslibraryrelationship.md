# MusicVideos.Relationships.MusicVideosLibraryRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the music video to its library.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Relationships.MusicVideosLibraryRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryMusicVideos]) *(required)*: The library associated with the music video, if any.

## See Also

- [object MusicVideos.Relationships.MusicVideosAlbumsRelationship](musicvideos/relationships-data.dictionary/musicvideosalbumsrelationship.md)
  A relationship from the music video to its albums.
- [object MusicVideos.Relationships.MusicVideosArtistsRelationship](musicvideos/relationships-data.dictionary/musicvideosartistsrelationship.md)
  A relationship from the music video to its artists.
- [object MusicVideos.Relationships.MusicVideosGenresRelationship](musicvideos/relationships-data.dictionary/musicvideosgenresrelationship.md)
  A relationship from the music video to its genres.
- [object MusicVideos.Relationships.MusicVideosSongsRelationship](musicvideos/relationships-data.dictionary/musicvideossongsrelationship.md)
  A relationship from the music video to its songs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/relationships-data.dictionary/musicvideoslibraryrelationship)*