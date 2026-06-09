# ArtworkRepresentation

**Framework**: Now Playing  
**Kind**: struct

An artwork image representation, such as music album cover art, associated with a media item.

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
struct ArtworkRepresentation
```

#### Overview

The system may display this artwork on the Lock Screen, in Control Center, and on connected accessories.

## Topics

### Initializers
- [init(cgImage: CGImage) throws](artworkrepresentation/init(cgimage:).md)
  Creates an [`ArtworkRepresentation`](artworkrepresentation.md) from a `CGImage` instance.
- [init(data: Data) throws](artworkrepresentation/init(data:).md)
  Creates an [`ArtworkRepresentation`](artworkrepresentation.md) from image data.
### Enumerations
- [ArtworkRepresentation.ArtworkRepresentationError](artworkrepresentation/artworkrepresentationerror.md)
  Errors that can occur when creating an [`ArtworkRepresentation`](artworkrepresentation.md).

## See Also

- [struct Artwork](artwork.md)
  Artwork for a media item that can be requested at a specified size.
- [struct AnimatedArtwork](animatedartwork.md)
  Animated artwork for the media item with video and preview support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/artworkrepresentation)*