# Songs

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a song.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Songs
```

## Topics

### Related Objects
- [object Songs.Attributes](songs/attributes-data.dictionary.md)
  The attributes for a song resource.
- [object Songs.Relationships](songs/relationships-data.dictionary.md)
  The relationships for a song resource.

## Properties

- `id` (string) *(required)*: The identifier for the song.
- `type` (string) *(required)*: This value is always `songs`.
- `href` (string) *(required)*: The relative location for the song resource.
- `attributes` (Songs.Attributes): The attributes for the song.
- `relationships` (Songs.Relationships): The relationships for the song.

## See Also

- [object SongsResponse](songsresponse.md)
  The response to a songs request.
- [object LibrarySongs](librarysongs.md)
  A resource object that represents a library song.
- [object LibrarySongsResponse](librarysongsresponse.md)
  The response to a library songs request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/songs)*