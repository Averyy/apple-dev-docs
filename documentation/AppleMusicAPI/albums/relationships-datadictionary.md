# Albums.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for an album resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Albums.Relationships
```

## Topics

### Related Objects
- [object Albums.Relationships.AlbumsArtistsRelationship](albums/relationships-data.dictionary/albumsartistsrelationship.md)
  A relationship from the album to its artists.
- [object Albums.Relationships.AlbumsGenresRelationship](albums/relationships-data.dictionary/albumsgenresrelationship.md)
  A relationship from the album to its genres.
- [object Albums.Relationships.AlbumsTracksRelationship](albums/relationships-data.dictionary/albumstracksrelationship.md)
  A relationship from the album to its tracks.
- [object Albums.Relationships.AlbumsLibraryRelationship](albums/relationships-data.dictionary/albumslibraryrelationship.md)
  A relationship from the album to an associated library album.
- [object Albums.Relationships.AlbumsRecordLabelsRelationship](albums/relationships-data.dictionary/albumsrecordlabelsrelationship.md)
  A relationship from the album to its associated record label.

## Properties

- `artists` (Albums.Relationships.AlbumsArtistsRelationship): The artists associated with the album. By default, `artists` includes identifiers only. Fetch limits: 10 default, 10 maximum
- `genres` (Albums.Relationships.AlbumsGenresRelationship): The genres for the album. By default, `genres` not included. Fetch limits: None
- `tracks` (Albums.Relationships.AlbumsTracksRelationship): The songs and music videos on the album. By default, `tracks` includes objects. Fetch limits: 300 default, 300 maximum
- `library` (Albums.Relationships.AlbumsLibraryRelationship): The album in the user’s library for the catalog album, if any. Fetch limits: None
- `record-labels` (Albums.Relationships.AlbumsRecordLabelsRelationship): The record labels for the album Fetch limits: 10 default, 10 maximum.

## See Also

- [object Albums.Attributes](albums/attributes-data.dictionary.md)
  The attributes for an album resource.
- [object Albums.Views](albums/views-data.dictionary.md)
  The relationship views for an album resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/relationships-data.dictionary)*