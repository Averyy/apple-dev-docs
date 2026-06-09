# GenericContent

**Framework**: Now Playing  
**Kind**: struct

Content representing generic or unspecified media.

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
struct GenericContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type when the media doesn’t fit into other specific content types such as [`MusicContent`](musiccontent.md), [`PodcastContent`](podcastcontent.md), [`MovieContent`](moviecontent.md), or [`TVShowContent`](tvshowcontent.md). This provides maximum flexibility for custom media types.

## Topics

### Initializers
- [init(id: String, title: String, subtitle: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)](genericcontent/init(id:title:subtitle:type:duration:artwork:).md)
  Creates generic media content.
- [init(id: String, title: String, subtitle: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](genericcontent/init(id:title:subtitle:type:duration:artwork:animatedartwork:).md)
  Creates generic media content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](genericcontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](genericcontent/artwork.md)
  Artwork for this content.
- [let duration: MediaDuration?](genericcontent/duration.md)
  The duration of this content.
- [let subtitle: String?](genericcontent/subtitle.md)
  An optional subtitle or secondary description.
- [let title: String](genericcontent/title.md)
  The title of the content.
- [let type: MediaType](genericcontent/type.md)
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
- [struct HomeMediaContent](homemediacontent.md)
  Content representing home media or ambient content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/genericcontent)*