# init(player:videoOverlay:)

**Framework**: AVKit  
**Kind**: init

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
@preconcurrency init(player: AVPlayer?, @ViewBuilder videoOverlay: () -> VideoOverlay)
```

## Parameters

- `player`: The player that plays the audiovisual content.
- `videoOverlay`: A closure that returns a   view to present over the player’s video content. This view is fully interactive, but is placed below the system-provided playback controls, and only receives unhandled events.

## See Also

- [init(player: AVPlayer?)](videoplayer/init(player:).md)
  Creates a video-player user interface for the player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/videoplayer/init(player:videooverlay:))*