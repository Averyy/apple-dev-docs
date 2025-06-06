# init(_:width:height:)

**Framework**: MusicKit  
**Kind**: init

Creates an instance with a specified width and height.

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
init(_ artwork: Artwork, width: CGFloat, height: CGFloat)
```

#### Discussion

This initializer derives the [`URL`](https://developer.apple.com/documentation/Foundation/URL) for loading the artwork image from the [`Artwork`](Artwork.md) instance and the specified sizing parameters, as well as the display scale for the current environment.

The loaded image and placeholder have constrained frames from these sizing parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/init(_:width:height:))*