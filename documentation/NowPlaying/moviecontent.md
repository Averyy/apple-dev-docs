# MovieContent

**Framework**: Now Playing  
**Kind**: struct

Content representing a movie.

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
struct MovieContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for movie playback, including films and documentaries.

## Topics

### Initializers
- [init(id: String, title: String, duration: MediaDuration?, artwork: Artwork?)](moviecontent/init(id:title:duration:artwork:).md)
  Creates movie content.
- [init(id: String, title: String, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](moviecontent/init(id:title:duration:artwork:animatedartwork:).md)
  Creates movie content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](moviecontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](moviecontent/artwork.md)
  Artwork for this content.
- [let duration: MediaDuration?](moviecontent/duration.md)
  The duration of this content.
- [let title: String](moviecontent/title.md)
  The title of the movie.
- [var type: MediaType](moviecontent/type.md)
  The media type (always video for movies).

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
- [struct TVShowContent](tvshowcontent.md)
  Content representing a TV show episode.
- [struct BookContent](bookcontent.md)
  Content representing an audiobook or book being read aloud.
- [struct RadioContent](radiocontent.md)
  Content representing a radio station or live audio stream.
- [struct HomeMediaContent](homemediacontent.md)
  Content representing home media or ambient content.
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/moviecontent)*