# LibrarySongs.Relationships.LibrarySongsCatalogRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the library song to its associated catalog content.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibrarySongs.Relationships.LibrarySongsCatalogRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Songs]) *(required)*: The song from the Apple Music catalog associated with the library song, if any.

## See Also

- [object LibrarySongs.Relationships.LibrarySongsAlbumsRelationship](librarysongs/relationships-data.dictionary/librarysongsalbumsrelationship.md)
  A relationship from the library song to its albums.
- [object LibrarySongs.Relationships.LibrarySongsArtistsRelationship](librarysongs/relationships-data.dictionary/librarysongsartistsrelationship.md)
  A relationship from the library song to its artists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs/relationships-data.dictionary/librarysongscatalogrelationship)*