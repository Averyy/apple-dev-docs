# Albums.Relationships.AlbumsGenresRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the album to its genres.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Albums.Relationships.AlbumsGenresRelationship
```

## Properties

- `href` (string): The relative location to fetch the relationship directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `data` ([Genres]) *(required)*: The album’s associated genre.

## See Also

### Related Objects
- [object Albums.Relationships.AlbumsArtistsRelationship](./albumsartistsrelationship.md)
  A relationship from the album to its artists.
- [object Albums.Relationships.AlbumsTracksRelationship](./albumstracksrelationship.md)
  A relationship from the album to its tracks.
- [object Albums.Relationships.AlbumsLibraryRelationship](./albumslibraryrelationship.md)
  A relationship from the album to an associated library album.
- [object Albums.Relationships.AlbumsRecordLabelsRelationship](./albumsrecordlabelsrelationship.md)
  A relationship from the album to its associated record label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/relationships-data.dictionary/albumsgenresrelationship)*