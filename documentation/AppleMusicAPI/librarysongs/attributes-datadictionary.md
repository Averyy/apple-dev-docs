# LibrarySongs.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for a library song resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibrarySongs.Attributes
```

## Properties

- `albumName` (string): The name of the album the song appears on.
- `artistName` (string) *(required)*: The artist’s name.
- `artwork` (Artwork) *(required)*: The album artwork.
- `contentRating` (string): The Recording Industry Association of America (RIAA) rating of the content. The possible values for this rating are `clean` and `explicit`. No value means no rating.
- `discNumber` (integer): The disc number the song appears on.
- `durationInMillis` (integer) *(required)*: The approximate length of the song in milliseconds.
- `genreNames` ([string]) *(required)*: The genre names the song is associated with.
- `hasLyrics` (boolean) *(required)*: Indicates if the song has lyrics available in the Apple Music catalog. If `true`, the song has lyrics available; otherwise, it doesn’t.
- `inFavorites` (boolean): Whether the catalog resource ID is in the person’s favorites.
- `name` (string) *(required)*: The localized name of the song.
- `playParams` (PlayParameters): When present, this attribute indicates that the song is available to play.  The value map may be used to initiate playback.
- `releaseDate` (string): The release date of the song, when known, in YYYY-MM-DD or YYYY format. Prerelease songs may have an expected release date in the future.
- `trackNumber` (integer): The number of the song in the album’s track list.

## See Also

- [object LibrarySongs.Relationships](librarysongs/relationships-data.dictionary.md)
  The relationships for a library song resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysongs/attributes-data.dictionary)*