# replaceCurrentItem(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Replaces the current item with a new item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
func replaceCurrentItem(with item: AVPlayerItem?)
```

```objc
- (void) replaceCurrentItemWithPlayerItem:(AVPlayerItem *) item;
```

## Mentions

- [Controlling the transport behavior of a player](../controlling-the-transport-behavior-of-a-player.md)

#### Discussion

The player item replacement occurs immediately and the item becomes the player’s [`currentItem`](./currentitem.md). Calling this method with the player’s current player item has no effect.

Replacing the current item removes the previous item from the player’s queue. An item that plays an HTTP Live Streaming (HLS) asset stops requesting playlists and media segments when the player removes it.

## Parameters

- `item`: The new item for the player object to play.

## See Also

### Managing the player item
- [var currentItem: AVPlayerItem?](./currentitem.md)
  The item for which the player is currently controlling playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/replacecurrentitem(with:))*