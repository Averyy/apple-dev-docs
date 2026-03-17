# Songs.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for a song resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Songs.Attributes
```

## Properties

- `albumName` (string) *(required)*: The name of the album the song appears on.
- `artistName` (string) *(required)*: The artist’s name.
- `artistUrl` (string): **(Extended)** The URL of the artist for the content.
- `artwork` (Artwork) *(required)*: The album artwork.
- `attribution` (string): (Classical music only) The name of the artist or composer to attribute the song with.
- `audioVariants` ([string]): **(Extended)** Indicates the specific audio variant for a song. > ❗ **Important**:  Use badges to indicate the audio variant in Apple Music. For more information, see [`Dolby Asset Center (DAC)`](https://developer.apple.comhttps://assetcenter.dolby.com/) for identifying tracks with the Dolby Atmos logo and [`Apple Lossless glyphs`](https://developer.apple.comhttps://developer.apple.com/go/?id=lossless-badges) for identifying tracks with the specific Apple Lossless glyph.
- `composerName` (string): The song’s composer.
- `contentRating` (string): The Recording Industry Association of America (RIAA) rating of the content. No value means no rating.
- `discNumber` (integer): The disc number of the album the song appears on.
- `durationInMillis` (integer) *(required)*: The duration of the song in milliseconds.
- `editorialNotes` (EditorialNotes): The notes about the song that appear in the Apple Music catalog.
- `genreNames` ([string]) *(required)*: The genre names the song is associated with.
- `hasLyrics` (boolean) *(required)*: Indicates whether the song has lyrics available in the Apple Music catalog. If `true`, the song has lyrics available; otherwise, it doesn’t.
- `inFavorites` (boolean): Whether the catalog resource ID is in the person’s favorites.
- `isAppleDigitalMaster` (boolean) *(required)*: Indicates whether the response delivered the song as an [`Apple Digital Master`](https://developer.apple.comhttps://www.apple.com/apple-music/apple-digital-masters/).
- `isrc` (string): The International Standard Recording Code (ISRC) for the song.
- `movementCount` (integer): (Classical music only) The movement count of the song.
- `movementName` (string): (Classical music only) The movement name of the song.
- `movementNumber` (integer): (Classical music only) The movement number of the song.
- `name` (string) *(required)*: The localized name of the song.
- `playParams` (PlayParameters): When present, this attribute indicates that the song is available to play with an Apple Music subscription. The value map may be used to initiate playback. Previews of the song audio may be available with or without an Apple Music subscription.
- `previews` ([Preview]) *(required)*: The preview assets for the song.
- `releaseDate` (string): The release date of the song, when known, in YYYY-MM-DD or YYYY format. Prerelease songs may have an expected release date in the future.
- `trackNumber` (integer): The number of the song in the album’s track list.
- `url` (string) *(required)*: The URL for sharing the song in Apple Music.
- `workName` (string): (Classical music only) The name of the associated work.

## See Also

- [object Songs.Relationships](songs/relationships-data.dictionary.md)
  The relationships for a song resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/songs/attributes-data.dictionary)*