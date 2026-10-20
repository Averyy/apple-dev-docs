# Artists.Relationships.ArtistsPlaylistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the artist to its playlists.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Artists.Relationships.ArtistsPlaylistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Playlists]) *(required)*: The playlists for the artist.

## See Also

### Related Objects
- [object Artists.Relationships.ArtistsAlbumsRelationship](./artistsalbumsrelationship.md)
  A relationship from the artist to its albums.
- [object Artists.Relationships.ArtistsGenresRelationship](./artistsgenresrelationship.md)
  A relationship from the artist to its genres.
- [object Artists.Relationships.ArtistsMusicVideosRelationship](./artistsmusicvideosrelationship.md)
  A relationship from the artist to its music videos.
- [object Artists.Relationships.ArtistsStationRelationship](./artistsstationrelationship.md)
  A relationship from the artist to its station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists/relationships-data.dictionary/artistsplaylistsrelationship)*