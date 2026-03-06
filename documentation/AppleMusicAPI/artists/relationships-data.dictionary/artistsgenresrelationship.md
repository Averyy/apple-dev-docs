# Artists.Relationships.ArtistsGenresRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the artist to its genres.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Artists.Relationships.ArtistsGenresRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Genres]) *(required)*: The artist’s associated genres.

## See Also

- [object Artists.Relationships.ArtistsAlbumsRelationship](artists/relationships-data.dictionary/artistsalbumsrelationship.md)
  A relationship from the artist to its albums.
- [object Artists.Relationships.ArtistsMusicVideosRelationship](artists/relationships-data.dictionary/artistsmusicvideosrelationship.md)
  A relationship from the artist to its music videos.
- [object Artists.Relationships.ArtistsPlaylistsRelationship](artists/relationships-data.dictionary/artistsplaylistsrelationship.md)
  A relationship from the artist to its playlists.
- [object Artists.Relationships.ArtistsStationRelationship](artists/relationships-data.dictionary/artistsstationrelationship.md)
  A relationship from the artist to its station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists/relationships-data.dictionary/artistsgenresrelationship)*