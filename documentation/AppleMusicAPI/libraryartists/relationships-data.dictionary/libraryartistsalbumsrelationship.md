# LibraryArtists.Relationships.LibraryArtistsAlbumsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library artist to thier albums.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryArtists.Relationships.LibraryArtistsAlbumsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryAlbums]) *(required)*: The albums for the library artist present in the user’s library.

## See Also

- [object LibraryArtists.Relationships.LibraryArtistsCatalogRelationship](libraryartists/relationships-data.dictionary/libraryartistscatalogrelationship.md)
  A relationship from the library artist to their associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryartists/relationships-data.dictionary/libraryartistsalbumsrelationship)*