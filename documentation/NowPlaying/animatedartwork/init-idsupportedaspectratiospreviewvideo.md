# init(id:supportedAspectRatios:preview:video:)

**Framework**: Now Playing  
**Kind**: init

Creates an animated artwork whose preview and video assets load on demand.

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
init(id: String, supportedAspectRatios: [AnimatedArtwork.AspectRatio] = [.square], preview previewProvider: @escaping @Sendable (CGSize, AnimatedArtwork.AspectRatio) async throws -> ArtworkRepresentation, video videoProvider: @escaping @Sendable (CGSize, AnimatedArtwork.AspectRatio) async throws -> URL)
```

## Parameters

- `id`: A unique identifier for this artwork.
- `supportedAspectRatios`: The aspect ratios your app supports.
- `previewProvider`: A closure that loads a preview image for the specified size and aspect ratio.
- `videoProvider`: A closure that provides a URL to a video file for the specified size and aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/animatedartwork/init(id:supportedaspectratios:preview:video:))*