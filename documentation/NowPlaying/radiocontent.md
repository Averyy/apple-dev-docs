# RadioContent

**Framework**: Now Playing  
**Kind**: struct

Content representing a radio station or live audio stream.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct RadioContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for radio stations, live streams, and other continuous audio broadcasts.

## Topics

### Initializers
- [init(id: String, stationName: String, programName: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)](radiocontent/init(id:stationname:programname:type:duration:artwork:).md)
  Creates radio station content.
- [init(id: String, stationName: String, programName: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](radiocontent/init(id:stationname:programname:type:duration:artwork:animatedartwork:).md)
  Creates radio station content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](radiocontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](radiocontent/artwork.md)
  Artwork for this content.
- [let duration: MediaDuration?](radiocontent/duration.md)
  The duration of this content.
- [let programName: String?](radiocontent/programname.md)
  The current program or show name, if available.
- [let stationName: String](radiocontent/stationname.md)
  The name of the radio station.
- [let type: MediaType](radiocontent/type.md)
  The media type (audio or video). Defaults to `.audio` for radio content.

## Relationships

### Conforms To
- [Identifiable](../swift/identifiable.md)
- [MediaContentRepresentable](mediacontentrepresentable.md)

## See Also

- [protocol MediaContentRepresentable](mediacontentrepresentable.md)
  A protocol that describes media content being played.
- [struct MusicContent](musiccontent.md)
  Content representing a music track or song.
- [struct PodcastContent](podcastcontent.md)
  Content representing a podcast episode.
- [struct MovieContent](moviecontent.md)
  Content representing a movie.
- [struct TVShowContent](tvshowcontent.md)
  Content representing a TV show episode.
- [struct BookContent](bookcontent.md)
  Content representing an audiobook or book being read aloud.
- [struct HomeMediaContent](homemediacontent.md)
  Content representing home media or ambient content.
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/radiocontent)*