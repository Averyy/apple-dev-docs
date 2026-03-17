# LibraryAlbums.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for a library album resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryAlbums.Attributes
```

## Properties

- `artistName` (string) *(required)*: The artist’s name.
- `artwork` (Artwork) *(required)*: The album artwork.
- `contentRating` (string): The Recording Industry Association of America (RIAA) rating of the content. The possible values for this rating are `clean` and `explicit`. No value means no rating.
- `dateAdded` (string): The date the album was added to the library, in YYYY-MM-DD or YYYY format.
- `name` (string) *(required)*: The localized name of the album.
- `playParams` (PlayParameters): When present, this attribute indicates that tracks from the album are available to play.  The value map may be used to initiate playback of available tracks on the album.
- `releaseDate` (string): The release date of the album, when known, in YYYY-MM-DD or YYYY format. Prerelease albums may have an expected release date in the future.
- `trackCount` (integer) *(required)*: The number of tracks.
- `genreNames` ([string]) *(required)*: The names of the genres associated with this album.
- `inFavorites` (boolean): Whether the catalog resource ID is in the person’s favorites.

## See Also

- [object LibraryAlbums.Relationships](libraryalbums/relationships-data.dictionary.md)
  The relationships for a library album object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryalbums/attributes-data.dictionary)*