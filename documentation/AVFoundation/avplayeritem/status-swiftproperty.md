# status

**Framework**: AVFoundation  
**Kind**: property

The status of the player item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var status: AVPlayerItem.Status { get }
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md)

#### Discussion

When a player item is created, its [`status`](avplayeritem/status-swift.property.md) is [`AVPlayerItem.Status.unknown`](avplayeritem/status-swift.enum/unknown.md), meaning its media hasn’t been loaded and has not yet been enqueued for playback. Associating a player item with an [`AVPlayer`](avplayer.md) immediately begins enqueuing the item’s media and preparing it for playback. When the player item’s media has been loaded and is ready for use, its status will change to [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md). You can observe this change using key-value observing.

For possible values, see [`AVPlayerItem.Status`](avplayeritem/status-swift.enum.md).

## See Also

- [AVPlayerItem.Status](avplayeritem/status-swift.enum.md)
  The statuses for a player item.
- [var error: (any Error)?](avplayeritem/error.md)
  The error that caused the player item to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/status-swift.property)*