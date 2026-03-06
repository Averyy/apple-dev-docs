# LibraryAlbums.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for a library album object.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryAlbums.Relationships
```

## Topics

### Related Objects
- [object LibraryAlbums.Relationships.LibraryAlbumsArtistsRelationship](libraryalbums/relationships-data.dictionary/libraryalbumsartistsrelationship.md)
  A relationship from the library album to its artist.
- [object LibraryAlbums.Relationships.LibraryAlbumsCatalogRelationship](libraryalbums/relationships-data.dictionary/libraryalbumscatalogrelationship.md)
  A relationship from the library album to its associated catalog content.
- [object LibraryAlbums.Relationships.LibraryAlbumsTracksRelationship](libraryalbums/relationships-data.dictionary/libraryalbumstracksrelationship.md)
  A relationship from the library album to its tracks.

## Properties

- `artists` (LibraryAlbums.Relationships.LibraryAlbumsArtistsRelationship): The library artists associated with the album. By default, `artists` not included. Fetch limits: 10 default, 10 maximum
- `catalog` (LibraryAlbums.Relationships.LibraryAlbumsCatalogRelationship): The album in the Apple Music catalog the library album is associated with, when known. Fetch limits: None (associated with at most one catalog album)
- `tracks` (LibraryAlbums.Relationships.LibraryAlbumsTracksRelationship): The library songs and library music videos on the album. Only available when fetching single library album resource by ID. By default, `tracks` includes objects. Fetch limits: 300 default, 300 maximum.

## See Also

- [object LibraryAlbums.Attributes](libraryalbums/attributes-data.dictionary.md)
  The attributes for a library album resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryalbums/relationships-data.dictionary)*