# TVShowContent

**Framework**: Now Playing  
**Kind**: struct

Content representing a TV show episode.

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
struct TVShowContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for television series playback, including individual episodes.

## Topics

### Initializers
- [init(id: String, episodeTitle: String, showName: String, duration: MediaDuration?, artwork: Artwork?)](tvshowcontent/init(id:episodetitle:showname:duration:artwork:).md)
  Creates TV show episode content.
- [init(id: String, episodeTitle: String, showName: String, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](tvshowcontent/init(id:episodetitle:showname:duration:artwork:animatedartwork:).md)
  Creates TV show episode content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](tvshowcontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](tvshowcontent/artwork.md)
  Artwork for this content.
- [let duration: MediaDuration?](tvshowcontent/duration.md)
  The duration of this content.
- [let episodeTitle: String](tvshowcontent/episodetitle.md)
  The title of the episode.
- [let showName: String](tvshowcontent/showname.md)
  The name of the TV show.
- [var type: MediaType](tvshowcontent/type.md)
  The media type (always video for TV shows).

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
- [struct BookContent](bookcontent.md)
  Content representing an audiobook or book being read aloud.
- [struct RadioContent](radiocontent.md)
  Content representing a radio station or live audio stream.
- [struct HomeMediaContent](homemediacontent.md)
  Content representing home media or ambient content.
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/tvshowcontent)*