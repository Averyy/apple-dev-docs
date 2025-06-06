# replaceCurrentItem(with:)

**Framework**: AVFoundation  
**Kind**: method

Replaces the current item with a new item.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
func replaceCurrentItem(with item: AVPlayerItem?)
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)

#### Discussion

The player item replacement occurs immediately and the item becomes the player’s [`currentItem`](avplayer/currentitem.md). Calling this method with the player’s current player item has no effect.

## Parameters

- `item`: The new item for the player object to play.

## See Also

- [var currentItem: AVPlayerItem?](avplayer/currentitem.md)
  The item for which the player is currently controlling playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/replacecurrentitem(with:))*