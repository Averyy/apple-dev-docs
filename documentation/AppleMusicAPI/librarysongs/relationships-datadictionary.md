# LibrarySongs.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for a library song resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibrarySongs.Relationships
```

## Topics

### Related Objects
- [object LibrarySongs.Relationships.LibrarySongsAlbumsRelationship](librarysongs/relationships-data.dictionary/librarysongsalbumsrelationship.md)
  A relationship from the library song to its albums.
- [object LibrarySongs.Relationships.LibrarySongsArtistsRelationship](librarysongs/relationships-data.dictionary/librarysongsartistsrelationship.md)
  A relationship from the library song to its artists.
- [object LibrarySongs.Relationships.LibrarySongsCatalogRelationship](librarysongs/relationships-data.dictionary/librarysongscatalogrelationship.md)
  A relationship from the library song to its associated catalog content.

## Properties

- `albums` (LibrarySongs.Relationships.LibrarySongsAlbumsRelationship): The library albums associated with the song. By default, `albums` not included. Fetch limits: 10 default, 10 maximum.
- `artists` (LibrarySongs.Relationships.LibrarySongsArtistsRelationship): The library artists associated with the song. By default, `artists` not included. Fetch limits: 10 default, 10 maximum.
- `catalog` (LibrarySongs.Relationships.LibrarySongsCatalogRelationship): The song in the Apple Music catalog the library song is associated with, when known. Fetch limits: None.

## See Also

- [object LibrarySongs.Attributes](librarysongs/attributes-data.dictionary.md)
  The attributes for a library song resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs/relationships-data.dictionary)*