# Songs.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The relationships for a song resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Songs.Relationships
```

## Topics

### Related Objects
- [object Songs.Relationships.SongsAlbumsRelationship](./relationships-data.dictionary/songsalbumsrelationship.md)
  A relationship from the song to its albums.
- [object Songs.Relationships.SongsArtistsRelationship](./relationships-data.dictionary/songsartistsrelationship.md)
  A relationship from the song to its artists.
- [object Songs.Relationships.SongsGenresRelationship](./relationships-data.dictionary/songsgenresrelationship.md)
  A relationship from the song to its genres.
- [object Songs.Relationships.SongsComposersRelationship](./relationships-data.dictionary/songscomposersrelationship.md)
  A relationship from the song to its composers.
- [object Songs.Relationships.SongsLibraryRelationship](./relationships-data.dictionary/songslibraryrelationship.md)
  A relationship from the song to its library.
- [object Songs.Relationships.SongsMusicVideosRelationship](./relationships-data.dictionary/songsmusicvideosrelationship.md)
  A relationship from the song to its music videos.
- [object Songs.Relationships.SongsStationRelationship](./relationships-data.dictionary/songsstationrelationship.md)
  A relationship from the song to its station.

## Properties

- `albums` (Songs.Relationships.SongsAlbumsRelationship): The albums associated with the song. By default, `albums` includes identifiers only.

  Fetch limits: 10 default, 10 maximum
- `artists` (Songs.Relationships.SongsArtistsRelationship): The artists associated with the song. By default, `artists` includes identifiers only.

  Fetch limits: 10 default, 10 maximum
- `composers` (Songs.Relationships.SongsComposersRelationship): The composers for a catalog song.
- `genres` (Songs.Relationships.SongsGenresRelationship): The genres associated with the song. By default, `genres` is not included.

  Fetch limits: None
- `library` (Songs.Relationships.SongsLibraryRelationship): Library song for a catalog song if added to library.
- `music-videos` (Songs.Relationships.SongsMusicVideosRelationship): Music videos for a catalog song.
- `station` (Songs.Relationships.SongsStationRelationship): The station associated with the song. By default, `station` is not included.

  Fetch limits: None

## See Also

### Related Objects
- [object Songs.Attributes](./attributes-data.dictionary.md)
  The attributes for a song resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/songs/relationships-data.dictionary)*