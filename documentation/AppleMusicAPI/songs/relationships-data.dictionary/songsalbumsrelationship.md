# Songs.Relationships.SongsAlbumsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the song to its albums.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Songs.Relationships.SongsAlbumsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Albums]) *(required)*: The albums associated with the song.

## See Also

### Related Objects
- [object Songs.Relationships.SongsArtistsRelationship](./songsartistsrelationship.md)
  A relationship from the song to its artists.
- [object Songs.Relationships.SongsGenresRelationship](./songsgenresrelationship.md)
  A relationship from the song to its genres.
- [object Songs.Relationships.SongsComposersRelationship](./songscomposersrelationship.md)
  A relationship from the song to its composers.
- [object Songs.Relationships.SongsLibraryRelationship](./songslibraryrelationship.md)
  A relationship from the song to its library.
- [object Songs.Relationships.SongsMusicVideosRelationship](./songsmusicvideosrelationship.md)
  A relationship from the song to its music videos.
- [object Songs.Relationships.SongsStationRelationship](./songsstationrelationship.md)
  A relationship from the song to its station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/songs/relationships-data.dictionary/songsalbumsrelationship)*