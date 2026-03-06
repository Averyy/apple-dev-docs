# Albums.Relationships.AlbumsTracksRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the album to its tracks.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Albums.Relationships.AlbumsTracksRelationship
```

## Properties

- `data` ([*]) *(required)*: The ordered songs and music videos in the tracklist of the album.
- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.

## See Also

- [object Albums.Relationships.AlbumsArtistsRelationship](albums/relationships-data.dictionary/albumsartistsrelationship.md)
  A relationship from the album to its artists.
- [object Albums.Relationships.AlbumsGenresRelationship](albums/relationships-data.dictionary/albumsgenresrelationship.md)
  A relationship from the album to its genres.
- [object Albums.Relationships.AlbumsLibraryRelationship](albums/relationships-data.dictionary/albumslibraryrelationship.md)
  A relationship from the album to an associated library album.
- [object Albums.Relationships.AlbumsRecordLabelsRelationship](albums/relationships-data.dictionary/albumsrecordlabelsrelationship.md)
  A relationship from the album to its associated record label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/relationships-data.dictionary/albumstracksrelationship)*