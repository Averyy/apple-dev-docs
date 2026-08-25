# MediaContentRepresentable

**Framework**: Now Playing  
**Kind**: protocol

A protocol that describes media content being played.

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
protocol MediaContentRepresentable : Identifiable
```

#### Overview

Content types like [`MusicContent`](musiccontent.md), [`PodcastContent`](podcastcontent.md), [`MovieContent`](moviecontent.md), [`TVShowContent`](tvshowcontent.md), [`BookContent`](bookcontent.md), [`RadioContent`](radiocontent.md), [`HomeMediaContent`](homemediacontent.md), and [`GenericContent`](genericcontent.md) conform to this protocol. Each content type provides structured metadata appropriate for its media type.

## Topics

### Instance Properties
- [var animatedArtwork: AnimatedArtwork?](mediacontentrepresentable/animatedartwork.md)
  Animated artwork for this content.
- [var appEntityIdentifiers: [EntityIdentifier]](mediacontentrepresentable/appentityidentifiers.md)
  The entities that represent this content, making them available to Siri and Apple Intelligence.
- [var artwork: Artwork?](mediacontentrepresentable/artwork.md)
  Artwork for this content.
- [var duration: MediaDuration?](mediacontentrepresentable/duration.md)
  The duration of this content.
- [var genre: String?](mediacontentrepresentable/genre.md)
  The genre of this content.
- [var id: String](mediacontentrepresentable/id.md)
  The unique identifier for this content.
- [var isExcludedFromSuggestions: Bool?](mediacontentrepresentable/isexcludedfromsuggestions.md)
  A Boolean value that indicates whether to exclude this content from media suggestions.
- [var isExplicit: Bool?](mediacontentrepresentable/isexplicit.md)
  A Boolean value that indicates whether this content is explicit.
- [var type: MediaType](mediacontentrepresentable/type.md)
  The media type (audio or video).

## Relationships

### Inherits From
- [Identifiable](../swift/identifiable.md)
### Conforming Types
- [BookContent](bookcontent.md)
- [GenericContent](genericcontent.md)
- [HomeMediaContent](homemediacontent.md)
- [MovieContent](moviecontent.md)
- [MusicContent](musiccontent.md)
- [PodcastContent](podcastcontent.md)
- [RadioContent](radiocontent.md)
- [TVShowContent](tvshowcontent.md)

## See Also

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
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacontentrepresentable)*