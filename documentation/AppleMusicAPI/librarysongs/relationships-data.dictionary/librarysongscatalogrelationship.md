# LibrarySongs.Relationships.LibrarySongsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the library song to its associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibrarySongs.Relationships.LibrarySongsCatalogRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Songs]) *(required)*: The song from the Apple Music catalog associated with the library song, if any.

## See Also

### Related Objects
- [object LibrarySongs.Relationships.LibrarySongsAlbumsRelationship](./librarysongsalbumsrelationship.md)
  A relationship from the library song to its albums.
- [object LibrarySongs.Relationships.LibrarySongsArtistsRelationship](./librarysongsartistsrelationship.md)
  A relationship from the library song to its artists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs/relationships-data.dictionary/librarysongscatalogrelationship)*