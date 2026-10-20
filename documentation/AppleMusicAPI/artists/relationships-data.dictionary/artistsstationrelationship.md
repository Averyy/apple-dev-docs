# Artists.Relationships.ArtistsStationRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the artist to its station.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Artists.Relationships.ArtistsStationRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Stations]) *(required)*: The station for the artist.

## See Also

### Related Objects
- [object Artists.Relationships.ArtistsAlbumsRelationship](./artistsalbumsrelationship.md)
  A relationship from the artist to its albums.
- [object Artists.Relationships.ArtistsGenresRelationship](./artistsgenresrelationship.md)
  A relationship from the artist to its genres.
- [object Artists.Relationships.ArtistsMusicVideosRelationship](./artistsmusicvideosrelationship.md)
  A relationship from the artist to its music videos.
- [object Artists.Relationships.ArtistsPlaylistsRelationship](./artistsplaylistsrelationship.md)
  A relationship from the artist to its playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists/relationships-data.dictionary/artistsstationrelationship)*