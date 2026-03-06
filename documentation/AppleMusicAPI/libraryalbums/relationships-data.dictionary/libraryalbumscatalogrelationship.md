# LibraryAlbums.Relationships.LibraryAlbumsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library album to its associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryAlbums.Relationships.LibraryAlbumsCatalogRelationship
```

## Properties

- `href` (string): The relative location to fetch the relationship directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `data` ([Albums]) *(required)*: The album from the Apple Music catalog associated with the library album, if any.

## See Also

- [object LibraryAlbums.Relationships.LibraryAlbumsArtistsRelationship](libraryalbums/relationships-data.dictionary/libraryalbumsartistsrelationship.md)
  A relationship from the library album to its artist.
- [object LibraryAlbums.Relationships.LibraryAlbumsTracksRelationship](libraryalbums/relationships-data.dictionary/libraryalbumstracksrelationship.md)
  A relationship from the library album to its tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryalbums/relationships-data.dictionary/libraryalbumscatalogrelationship)*