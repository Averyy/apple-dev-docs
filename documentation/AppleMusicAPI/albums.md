# Albums

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents an album.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Albums
```

## Mentions

- [Handling Resource Representation and Relationships](handling-resource-representation-and-relationships.md)

## Topics

### Related Objects
- [object Albums.Attributes](albums/attributes-data.dictionary.md)
  The attributes for an album resource.
- [object Albums.Relationships](albums/relationships-data.dictionary.md)
  The relationships for an album resource.
- [object Albums.Views](albums/views-data.dictionary.md)
  The relationship views for an album resource.

## Properties

- `id` (string) *(required)*: The identifier for the album.
- `type` (string) *(required)*: This value is always `albums`.
- `href` (string) *(required)*: The relative location for the album resource.
- `attributes` (Albums.Attributes): The attributes for the album.
- `relationships` (Albums.Relationships): The relationships for the album.
- `views` (Albums.Views): The relationship views for the album.

## See Also

- [object AlbumsResponse](albumsresponse.md)
  The response to an albums request.
- [object LibraryAlbums](libraryalbums.md)
  A resource object that represents a library album.
- [object LibraryAlbumsResponse](libraryalbumsresponse.md)
  The response to a library albums request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums)*