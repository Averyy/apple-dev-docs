# PodcastContent

**Framework**: Now Playing  
**Kind**: struct

Content representing a podcast episode.

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
struct PodcastContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for podcast playback, including individual episodes and series.

## Topics

### Initializers
- [init(id: String, episodeTitle: String, showName: String, releaseDate: Date?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)](podcastcontent/init(id:episodetitle:showname:releasedate:type:duration:artwork:).md)
  Creates podcast episode content.
- [init(id: String, episodeTitle: String, showName: String, releaseDate: Date?, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](podcastcontent/init(id:episodetitle:showname:releasedate:type:duration:artwork:animatedartwork:).md)
  Creates podcast episode content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](podcastcontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](podcastcontent/artwork.md)
  Artwork for this content.
- [let duration: MediaDuration?](podcastcontent/duration.md)
  The duration of this content.
- [let episodeTitle: String](podcastcontent/episodetitle.md)
  The title of the podcast episode.
- [let releaseDate: Date?](podcastcontent/releasedate.md)
  The release date of the episode.
- [let showName: String](podcastcontent/showname.md)
  The name of the podcast show.
- [let type: MediaType](podcastcontent/type.md)
  The media type (audio or video).

## Relationships

### Conforms To
- [Identifiable](../swift/identifiable.md)
- [MediaContentRepresentable](mediacontentrepresentable.md)

## See Also

- [protocol MediaContentRepresentable](mediacontentrepresentable.md)
  A protocol that describes media content being played.
- [struct MusicContent](musiccontent.md)
  Content representing a music track or song.
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
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/podcastcontent)*