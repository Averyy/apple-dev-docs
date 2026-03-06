# LibraryArtists.Relationships.LibraryArtistsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library artist to their associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryArtists.Relationships.LibraryArtistsCatalogRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Artists]) *(required)*: The artist from the Apple Music catalog associated with the library artist, if any.

## See Also

- [object LibraryArtists.Relationships.LibraryArtistsAlbumsRelationship](libraryartists/relationships-data.dictionary/libraryartistsalbumsrelationship.md)
  A relationship from the library artist to thier albums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryartists/relationships-data.dictionary/libraryartistscatalogrelationship)*