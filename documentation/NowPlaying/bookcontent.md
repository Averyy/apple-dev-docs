# BookContent

**Framework**: Now Playing  
**Kind**: struct

Content representing an audiobook or book being read aloud.

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
struct BookContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for audiobooks and other spoken-word book content.

## Topics

### Initializers
- [init(id: String, title: String, authorName: String, narratorName: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)](bookcontent/init(id:title:authorname:narratorname:type:duration:artwork:).md)
  Creates audiobook content.
- [init(id: String, title: String, authorName: String, narratorName: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](bookcontent/init(id:title:authorname:narratorname:type:duration:artwork:animatedartwork:).md)
  Creates audiobook content with static and animated artwork.
### Instance Properties
- [let animatedArtwork: AnimatedArtwork?](bookcontent/animatedartwork.md)
  Animated artwork for this content.
- [let artwork: Artwork?](bookcontent/artwork.md)
  Artwork for this content.
- [let authorName: String](bookcontent/authorname.md)
  The author of the book.
- [var chapter: (current: Int, total: Int)?](bookcontent/chapter.md)
  The current chapter information, if applicable.
- [let duration: MediaDuration?](bookcontent/duration.md)
  The duration of this content.
- [let narratorName: String?](bookcontent/narratorname.md)
  The narrator of the audiobook, if applicable.
- [let title: String](bookcontent/title.md)
  The title of the book.
- [let type: MediaType](bookcontent/type.md)
  The media type. Defaults to `.audio` for book content.

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
- [struct RadioContent](radiocontent.md)
  Content representing a radio station or live audio stream.
- [struct HomeMediaContent](homemediacontent.md)
  Content representing home media or ambient content.
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/bookcontent)*