# LibraryAlbums

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a library album.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryAlbums
```

## Topics

### Related Objects
- [object LibraryAlbums.Attributes](libraryalbums/attributes-data.dictionary.md)
  The attributes for a library album resource.
- [object LibraryAlbums.Relationships](libraryalbums/relationships-data.dictionary.md)
  The relationships for a library album object.

## Properties

- `id` (string) *(required)*: The identifier for the library album.
- `type` (string) *(required)*: This value is always `library-albums`.
- `href` (string) *(required)*: The relative location for the library album resource.
- `attributes` (LibraryAlbums.Attributes): The attributes for the library album.
- `relationships` (LibraryAlbums.Relationships): The relationships for the library album.

## See Also

- [object Albums](albums.md)
  A resource object that represents an album.
- [object AlbumsResponse](albumsresponse.md)
  The response to an albums request.
- [object LibraryAlbumsResponse](libraryalbumsresponse.md)
  The response to a library albums request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryalbums)*