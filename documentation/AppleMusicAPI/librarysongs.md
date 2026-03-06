# LibrarySongs

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a library song.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibrarySongs
```

## Topics

### Related Objects
- [object LibrarySongs.Attributes](librarysongs/attributes-data.dictionary.md)
  The attributes for a library song resource.
- [object LibrarySongs.Relationships](librarysongs/relationships-data.dictionary.md)
  The relationships for a library song resource.

## Properties

- `id` (string) *(required)*: The identifier for the library song.
- `type` (string) *(required)*: This value is always `library-songs`.
- `href` (string) *(required)*: The relative location for the library song resource.
- `attributes` (LibrarySongs.Attributes): The attributes for the library song.
- `relationships` (LibrarySongs.Relationships): The relationships for the library song.

## See Also

- [object Songs](songs.md)
  A resource object that represents a song.
- [object SongsResponse](songsresponse.md)
  The response to a songs request.
- [object LibrarySongsResponse](librarysongsresponse.md)
  The response to a library songs request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs)*