# Artists.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for an artist resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Artists.Relationships
```

## Topics

### Related Objects
- [object Artists.Relationships.ArtistsAlbumsRelationship](artists/relationships-data.dictionary/artistsalbumsrelationship.md)
  A relationship from the artist to its albums.
- [object Artists.Relationships.ArtistsGenresRelationship](artists/relationships-data.dictionary/artistsgenresrelationship.md)
  A relationship from the artist to its genres.
- [object Artists.Relationships.ArtistsMusicVideosRelationship](artists/relationships-data.dictionary/artistsmusicvideosrelationship.md)
  A relationship from the artist to its music videos.
- [object Artists.Relationships.ArtistsPlaylistsRelationship](artists/relationships-data.dictionary/artistsplaylistsrelationship.md)
  A relationship from the artist to its playlists.
- [object Artists.Relationships.ArtistsStationRelationship](artists/relationships-data.dictionary/artistsstationrelationship.md)
  A relationship from the artist to its station.

## Properties

- `albums` (Artists.Relationships.ArtistsAlbumsRelationship): The albums associated with the artist. By default, `albums` includes identifiers only. Fetch limits: 25 default, 100 maximum
- `genres` (Artists.Relationships.ArtistsGenresRelationship): The genres associated with the artist. By default, `genres` not included. Fetch limits: None
- `music-videos` (Artists.Relationships.ArtistsMusicVideosRelationship): The music videos associated with the artist. By default, `musicVideos` not included. Fetch limits: 25 default, 100 maximum
- `playlists` (Artists.Relationships.ArtistsPlaylistsRelationship): The playlists associated with the artist. By default, `playlists` not included. Fetch limits: 10 default, 10 maximum
- `station` (Artists.Relationships.ArtistsStationRelationship): The station associated with the artist. By default, station not included. Fetch limits: None (one station).

## See Also

- [object Artists.Attributes](artists/attributes-data.dictionary.md)
  The attributes for an artist resource.
- [object Artists.Views](artists/views-data.dictionary.md)
  The views for associations between artists and other resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists/relationships-data.dictionary)*