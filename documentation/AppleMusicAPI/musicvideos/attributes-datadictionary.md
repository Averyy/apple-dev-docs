# MusicVideos.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for a music video resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Attributes
```

## Properties

- `albumName` (string): The name of the album the music video appears on.
- `artistName` (string) *(required)*: The artist’s name.
- `artistUrl` (string): **(Extended)** The URL of the artist for this content.
- `artwork` (Artwork) *(required)*: The artwork for the music video’s associated album.
- `contentRating` (string): The Recording Industry Association of America (RIAA) rating of the content. No value means no rating.
- `durationInMillis` (integer) *(required)*: The duration of the music video in milliseconds.
- `editorialNotes` (EditorialNotes): The editorial notes for the music video.
- `genreNames` ([string]) *(required)*: The music video’s associated genres.
- `has4K` (boolean) *(required)*: Whether the music video has 4K content.
- `hasHDR` (boolean) *(required)*: Whether the music video has HDR10-encoded content.
- `isrc` (string): The International Standard Recording Code (ISRC) for the music video.
- `name` (string) *(required)*: The localized name of the music video.
- `playParams` (PlayParameters): When present, indicates that the music video is available to play with an Apple Music subscription. The value map may be used to initiate playback. Previews of the music video may be available with or without an Apple Music subscription.
- `previews` ([Preview]) *(required)*: The preview assets for the music video.
- `releaseDate` (string): The release date of the music video, when known, in YYYY-MM-DD or YYYY format. Prerelease music videos may have an expected release date in the future.
- `trackNumber` (integer): The number of the music video in the album’s track list, when associated with an album.
- `url` (string) *(required)*: The URL for sharing the music video in Apple Music.
- `videoSubType` (string): The video subtype associated with the content.
- `workId` (string): (Classical music only) A unique identifier for the associated work.
- `workName` (string): (Classical music only) The name of the associated work.

## See Also

- [object MusicVideos.Relationships](musicvideos/relationships-data.dictionary.md)
  The relationships for a music video resource.
- [object MusicVideos.Views](musicvideos/views-data.dictionary.md)
  The views for a music video resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/attributes-data.dictionary)*