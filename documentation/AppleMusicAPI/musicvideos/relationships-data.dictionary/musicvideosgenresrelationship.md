# MusicVideos.Relationships.MusicVideosGenresRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the music video to its genres.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Relationships.MusicVideosGenresRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Genres]) *(required)*: The genres associated with the music video.

## See Also

- [object MusicVideos.Relationships.MusicVideosAlbumsRelationship](musicvideos/relationships-data.dictionary/musicvideosalbumsrelationship.md)
  A relationship from the music video to its albums.
- [object MusicVideos.Relationships.MusicVideosArtistsRelationship](musicvideos/relationships-data.dictionary/musicvideosartistsrelationship.md)
  A relationship from the music video to its artists.
- [object MusicVideos.Relationships.MusicVideosLibraryRelationship](musicvideos/relationships-data.dictionary/musicvideoslibraryrelationship.md)
  A relationship from the music video to its library.
- [object MusicVideos.Relationships.MusicVideosSongsRelationship](musicvideos/relationships-data.dictionary/musicvideossongsrelationship.md)
  A relationship from the music video to its songs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/relationships-data.dictionary/musicvideosgenresrelationship)*