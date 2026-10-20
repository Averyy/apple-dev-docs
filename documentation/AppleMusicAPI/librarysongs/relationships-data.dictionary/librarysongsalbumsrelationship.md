# LibrarySongs.Relationships.LibrarySongsAlbumsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship from the library song to its albums.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibrarySongs.Relationships.LibrarySongsAlbumsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryAlbums]) *(required)*: The albums in the library associated with the song.

## See Also

### Related Objects
- [object LibrarySongs.Relationships.LibrarySongsArtistsRelationship](./librarysongsartistsrelationship.md)
  A relationship from the library song to its artists.
- [object LibrarySongs.Relationships.LibrarySongsCatalogRelationship](./librarysongscatalogrelationship.md)
  A relationship from the library song to its associated catalog content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs/relationships-data.dictionary/librarysongsalbumsrelationship)*