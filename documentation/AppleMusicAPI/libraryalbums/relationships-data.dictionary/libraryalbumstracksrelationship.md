# LibraryAlbums.Relationships.LibraryAlbumsTracksRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library album to its tracks.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryAlbums.Relationships.LibraryAlbumsTracksRelationship
```

## Properties

- `href` (string): The relative location to fetch the relationship directly.
- `next` (string): The relative location to request the next page of resources in the collection, if additional resources are available for fetching.
- `data` ([*]) *(required)*: The songs and music videos from the library album’s tracklist added to the user’s library.

## See Also

- [object LibraryAlbums.Relationships.LibraryAlbumsArtistsRelationship](libraryalbums/relationships-data.dictionary/libraryalbumsartistsrelationship.md)
  A relationship from the library album to its artist.
- [object LibraryAlbums.Relationships.LibraryAlbumsCatalogRelationship](libraryalbums/relationships-data.dictionary/libraryalbumscatalogrelationship.md)
  A relationship from the library album to its associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryalbums/relationships-data.dictionary/libraryalbumstracksrelationship)*