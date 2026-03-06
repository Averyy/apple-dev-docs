# Albums.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for an album resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Albums.Attributes
```

## Properties

- `artistName` (string) *(required)*: The name of the primary artist associated with the album.
- `artistUrl` (string): **(Extended)** The URL of the artist for this content.
- `artwork` (Artwork) *(required)*: The artwork for the album.
- `audioVariants` ([string]): **(Extended)** Indicates the specific audio variant for the album. > ❗ **Important**:  Use badges to indicate the audio variant in Apple Music. For more information, see [`Dolby Asset Center (DAC)`](https://developer.apple.comhttps://assetcenter.dolby.com/) for identifying tracks with the Dolby Atmos logo and [`Apple Lossless glyphs`](https://developer.apple.comhttps://developer.apple.com/go/?id=lossless-badges) for identifying tracks with the specific Apple Lossless glyph.
- `contentRating` (string): The Recording Industry Association of America (RIAA) rating of the content. No value means no rating.
- `copyright` (string): The copyright text.
- `editorialNotes` (EditorialNotes): The notes about the album that appear in the iTunes Store.
- `genreNames` ([string]) *(required)*: The names of the genres associated with the album.
- `isCompilation` (boolean) *(required)*: Indicates whether the album is marked as a compilation. If `true`, the album is a compilation; otherwise, it’s not.
- `isComplete` (boolean) *(required)*: Indicates whether the album is complete. If `true`, the album is complete; otherwise, it’s not. An album is complete if it contains all its tracks and songs.
- `isMasteredForItunes` (boolean) *(required)*: Indicates whether the response delivered the album as an [`Apple Digital Master`](https://developer.apple.comhttps://www.apple.com/itunes/mastered-for-itunes/).
- `isSingle` (boolean) *(required)*: Indicates whether the album contains a single song.
- `name` (string) *(required)*: The localized name of the album.
- `playParams` (PlayParameters): When present, this attribute indicates that one or more tracks on the album are available to play with an Apple Music subscription. The value map may be used to initiate playback of available tracks on the album.
- `recordLabel` (string): The name of the record label for the album.
- `releaseDate` (string): The release date of the album, when known, in YYYY-MM-DD or YYYY format. Prerelease content may have an expected release date in the future.
- `trackCount` (integer) *(required)*: The number of tracks for the album.
- `upc` (string): The Universal Product Code for the album.
- `url` (string) *(required)*: The URL for sharing the album in Apple Music.

## See Also

- [object Albums.Relationships](albums/relationships-data.dictionary.md)
  The relationships for an album resource.
- [object Albums.Views](albums/views-data.dictionary.md)
  The relationship views for an album resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albums/attributes-data.dictionary)*