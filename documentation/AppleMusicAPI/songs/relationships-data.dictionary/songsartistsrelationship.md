# Songs.Relationships.SongsArtistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the song to its artists.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Songs.Relationships.SongsArtistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Artists]) *(required)*: The artists associated with the song.

## See Also

- [object Songs.Relationships.SongsAlbumsRelationship](songs/relationships-data.dictionary/songsalbumsrelationship.md)
  A relationship from the song to its albums.
- [object Songs.Relationships.SongsGenresRelationship](songs/relationships-data.dictionary/songsgenresrelationship.md)
  A relationship from the song to its genres.
- [object Songs.Relationships.SongsComposersRelationship](songs/relationships-data.dictionary/songscomposersrelationship.md)
  A relationship from the song to its composers.
- [object Songs.Relationships.SongsLibraryRelationship](songs/relationships-data.dictionary/songslibraryrelationship.md)
  A relationship from the song to its library.
- [object Songs.Relationships.SongsMusicVideosRelationship](songs/relationships-data.dictionary/songsmusicvideosrelationship.md)
  A relationship from the song to its music videos.
- [object Songs.Relationships.SongsStationRelationship](songs/relationships-data.dictionary/songsstationrelationship.md)
  A relationship from the song to its station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/songs/relationships-data.dictionary/songsartistsrelationship)*