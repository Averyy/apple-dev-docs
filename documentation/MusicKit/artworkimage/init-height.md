# init(_:height:)

**Framework**: MusicKit  
**Kind**: init

Creates an instance with a specified height.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
init(_ artwork: Artwork, height: CGFloat)
```

#### Discussion

This initializer derives the [`URL`](https://developer.apple.com/documentation/Foundation/URL) for loading the artwork image from the [`Artwork`](Artwork.md) instance and the specified sizing parameters, as well as the display scale for the current environment.

The loaded image and placeholder have constrained frames from these sizing parameters.

If you provide the height only, the artwork image calculates the width dimension as a proportional length according to the aspect ratio of the artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/init(_:height:))*