# MusicVideos.Relationships.MusicVideosGenresRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the music video to its genres.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object MusicVideos.Relationships.MusicVideosGenresRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Genres]) *(required)*: The genres associated with the music video.

## See Also

### Related Objects
- [object MusicVideos.Relationships.MusicVideosAlbumsRelationship](./musicvideosalbumsrelationship.md)
  A relationship from the music video to its albums.
- [object MusicVideos.Relationships.MusicVideosArtistsRelationship](./musicvideosartistsrelationship.md)
  A relationship from the music video to its artists.
- [object MusicVideos.Relationships.MusicVideosLibraryRelationship](./musicvideoslibraryrelationship.md)
  A relationship from the music video to its library.
- [object MusicVideos.Relationships.MusicVideosSongsRelationship](./musicvideossongsrelationship.md)
  A relationship from the music video to its songs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/relationships-data.dictionary/musicvideosgenresrelationship)*