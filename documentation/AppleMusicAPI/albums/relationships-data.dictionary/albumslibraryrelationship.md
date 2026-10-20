# Albums.Relationships.AlbumsLibraryRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the album to an associated library album.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Albums.Relationships.AlbumsLibraryRelationship
```

## Properties

- `href` (string): The relative location to fetch the relationship directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `data` ([LibraryAlbums]) *(required)*: The library content this album is associated with if added to the user’s library.

## See Also

### Related Objects
- [object Albums.Relationships.AlbumsArtistsRelationship](./albumsartistsrelationship.md)
  A relationship from the album to its artists.
- [object Albums.Relationships.AlbumsGenresRelationship](./albumsgenresrelationship.md)
  A relationship from the album to its genres.
- [object Albums.Relationships.AlbumsTracksRelationship](./albumstracksrelationship.md)
  A relationship from the album to its tracks.
- [object Albums.Relationships.AlbumsRecordLabelsRelationship](./albumsrecordlabelsrelationship.md)
  A relationship from the album to its associated record label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/relationships-data.dictionary/albumslibraryrelationship)*