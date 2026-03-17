# LibraryMusicVideos.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for the library music videos resource type.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryMusicVideos.Attributes
```

## Properties

- `albumName` (string): The name of the album the music video appears on.
- `artistName` (string) *(required)*: The artist’s name.
- `artwork` (Artwork) *(required)*: The artwork for the music video’s associated album.
- `contentRating` (string): The Recording Industry Association of America (RIAA) rating of the content. The possible values for this rating are `clean` and `explicit`. No value means no rating.
- `durationInMillis` (integer) *(required)*: The duration of the music video in milliseconds.
- `genreNames` ([string]) *(required)*: The names of the genres associated with this music video.
- `inFavorites` (boolean): Whether the catalog resource ID is in the person’s favorites.
- `name` (string) *(required)*: The localized name of the music video.
- `playParams` (PlayParameters): When present, this attribute indicates that the music video is able to play.  The value map may be used to initiate playback.
- `releaseDate` (string): The release date of the music video, when known, in YYYY-MM-DD or YYYY format. Prerelease content may have an expected release date in the future.
- `trackNumber` (integer): The number of the music video in the album’s track list.

## See Also

- [object LibraryMusicVideos.Relationships](librarymusicvideos/relationships-data.dictionary.md)
  The relationships from library music videos to other resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarymusicvideos/attributes-data.dictionary)*