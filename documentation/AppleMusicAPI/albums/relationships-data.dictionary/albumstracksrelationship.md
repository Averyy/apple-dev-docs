# Albums.Relationships.AlbumsTracksRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the album to its tracks.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Albums.Relationships.AlbumsTracksRelationship
```

## Properties

- `data` ([*]) *(required)*: The ordered songs and music videos in the tracklist of the album.

  **Allowed Types**: `MusicVideos`, `Songs`
- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.

## See Also

### Related Objects
- [object Albums.Relationships.AlbumsArtistsRelationship](./albumsartistsrelationship.md)
  A relationship from the album to its artists.
- [object Albums.Relationships.AlbumsGenresRelationship](./albumsgenresrelationship.md)
  A relationship from the album to its genres.
- [object Albums.Relationships.AlbumsLibraryRelationship](./albumslibraryrelationship.md)
  A relationship from the album to an associated library album.
- [object Albums.Relationships.AlbumsRecordLabelsRelationship](./albumsrecordlabelsrelationship.md)
  A relationship from the album to its associated record label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/relationships-data.dictionary/albumstracksrelationship)*