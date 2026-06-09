# AnimatedArtwork

**Framework**: Now Playing  
**Kind**: struct

Animated artwork for the media item with video and preview support.

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
struct AnimatedArtwork
```

#### Overview

The following example shows how to attach animated artwork to a content value:

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
    },
    animatedArtwork: AnimatedArtwork(
        id: "animated-789",
        supportedAspectRatios: [.square, .tall],
        preview: { size, ratio in
            let data = await loadPreviewData(size: size, ratio: ratio)
            return try ArtworkRepresentation(data: data)
        },
        video: { size, ratio in
            await loadVideoURL(size: size, ratio: ratio)
        }
    )
)
```

## Topics

### Initializers
- [init(id: String, supportedAspectRatios: [AnimatedArtwork.AspectRatio], preview: (CGSize, AnimatedArtwork.AspectRatio) async throws -> ArtworkRepresentation, video: (CGSize, AnimatedArtwork.AspectRatio) async throws -> URL)](animatedartwork/init(id:supportedaspectratios:preview:video:).md)
  Creates an animated artwork whose preview and video assets load on demand.
### Instance Properties
- [let id: String](animatedartwork/id.md)
  A unique identifier for this animated artwork asset.
- [let supportedAspectRatios: [AnimatedArtwork.AspectRatio]](animatedartwork/supportedaspectratios.md)
  The aspect ratios this artwork supports.
### Instance Methods
- [func extract(into: inout [String : Any])](animatedartwork/extract(into:).md)
### Enumerations
- [AnimatedArtwork.AspectRatio](animatedartwork/aspectratio.md)
  The aspect ratio of the animated artwork.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct Artwork](artwork.md)
  Artwork for a media item that can be requested at a specified size.
- [struct ArtworkRepresentation](artworkrepresentation.md)
  An artwork image representation, such as music album cover art, associated with a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/animatedartwork)*