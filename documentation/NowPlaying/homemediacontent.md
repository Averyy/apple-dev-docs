# HomeMediaContent

**Framework**: Now Playing  
**Kind**: struct

Content representing home media or ambient content.

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
struct HomeMediaContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for home-related media such as security camera feeds, baby monitors, or ambient soundscapes.

## Topics

### Initializers
- [init(id: String, sourceName: String, contentDescription: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)](homemediacontent/init(id:sourcename:contentdescription:type:duration:artwork:).md)
  Creates home media content.
- [init(id: String, sourceName: String, contentDescription: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](homemediacontent/init(id:sourcename:contentdescription:type:duration:artwork:animatedartwork:).md)
  Creates home media content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](homemediacontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](homemediacontent/artwork.md)
  Artwork for this content.
- [let contentDescription: String?](homemediacontent/contentdescription.md)
  A description of the content, if available.
- [let duration: MediaDuration?](homemediacontent/duration.md)
  The duration of this content.
- [let sourceName: String](homemediacontent/sourcename.md)
  The name of the home media source or device.
- [let type: MediaType](homemediacontent/type.md)
  The media type (audio or video).

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
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
- [struct RadioContent](radiocontent.md)
  Content representing a radio station or live audio stream.
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/homemediacontent)*