# init(player:)

**Framework**: AVKit  
**Kind**: init  
**Role**: Initializer

Creates a video-player user interface for the player object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency init(player: AVPlayer?)
```

Available when `VideoOverlay` is `EmptyView`.

## Parameters

- `player`: The player that plays the audiovisual content.

## See Also

### Creating a video player
- [init(player: AVPlayer?, videoOverlay: () -> VideoOverlay)](./init%28player,videooverlay%29.md)
  Creates a video-player user interface for the player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/videoplayer/init(player:))*