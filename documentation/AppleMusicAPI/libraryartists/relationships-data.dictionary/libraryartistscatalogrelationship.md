# LibraryArtists.Relationships.LibraryArtistsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the library artist to their associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibraryArtists.Relationships.LibraryArtistsCatalogRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Artists]) *(required)*: The artist from the Apple Music catalog associated with the library artist, if any.

## See Also

### Related Objects
- [object LibraryArtists.Relationships.LibraryArtistsAlbumsRelationship](./libraryartistsalbumsrelationship.md)
  A relationship from the library artist to thier albums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryartists/relationships-data.dictionary/libraryartistscatalogrelationship)*