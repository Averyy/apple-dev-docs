# LibraryArtists

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents an artist present in a user’s library.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryArtists
```

## Topics

### Related Objects
- [object LibraryArtists.Attributes](libraryartists/attributes-data.dictionary.md)
  The attributes for a library artist resource.
- [object LibraryArtists.Relationships](libraryartists/relationships-data.dictionary.md)
  The relationships for a library artist resource.

## Properties

- `id` (string) *(required)*: The identifier for the library artist.
- `type` (string) *(required)*: This value is always `library-artists`.
- `href` (string) *(required)*: The relative location for the library artist resource.
- `attributes` (LibraryArtists.Attributes): The attributes for the library artist.
- `relationships` (LibraryArtists.Relationships): The relationships for the library artist.

## See Also

- [object Artists](artists.md)
  A resource object that represents the artist of an album where an artist can be one or more people.
- [object ArtistsResponse](artistsresponse.md)
  The response to an artists request.
- [object LibraryArtistsResponse](libraryartistsresponse.md)
  The response to a library artists request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryartists)*