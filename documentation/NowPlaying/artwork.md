# Artwork

**Framework**: Now Playing  
**Kind**: struct

Artwork for a media item that can be requested at a specified size.

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
struct Artwork
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

The following example shows how to attach artwork to a content value:

```swift
let content = MusicContent(
    id: track.id,
    songTitle: track.title,
    artistName: track.artist,
    albumName: track.album,
    type: .audio,
    duration: .finite(track.duration),
    artwork: Artwork(id: track.artworkID) { size in
        let data = await loadArtworkData(size: size)
        return try ArtworkRepresentation(data: data)
    }
)
```

## Topics

### Initializers
- [init(id: String, artworkProvider: (CGSize) async throws -> ArtworkRepresentation)](artwork/init(id:artworkprovider:).md)
  Creates an artwork whose image data loads on demand at the requested size.
### Instance Properties
- [let id: String](artwork/id.md)
  A unique identifier for this artwork, which the system uses to cache artwork across fetches.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct ArtworkRepresentation](artworkrepresentation.md)
  An artwork image representation, such as music album cover art, associated with a media item.
- [struct AnimatedArtwork](animatedartwork.md)
  Animated artwork for the media item with video and preview support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/artwork)*