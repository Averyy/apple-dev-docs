# LibrarySongs.Relationships.LibrarySongsArtistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the library song to its artists.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibrarySongs.Relationships.LibrarySongsArtistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryArtists]) *(required)*: The artists in the library associated with the song.

## See Also

### Related Objects
- [object LibrarySongs.Relationships.LibrarySongsAlbumsRelationship](./librarysongsalbumsrelationship.md)
  A relationship from the library song to its albums.
- [object LibrarySongs.Relationships.LibrarySongsCatalogRelationship](./librarysongscatalogrelationship.md)
  A relationship from the library song to its associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs/relationships-data.dictionary/librarysongsartistsrelationship)*