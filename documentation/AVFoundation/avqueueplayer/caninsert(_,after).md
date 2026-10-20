# canInsert(_:after:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func canInsert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?) -> Bool
```

```objc
- (BOOL) canInsertItem:(AVPlayerItem *) item afterItem:(AVPlayerItem *) afterItem;
```

#### Return Value

[`true`](../../Swift/true.md) if `item` can be appended to the queue, otherwise [`false`](../../Swift/false.md).

#### Discussion

Adding the same item to a player at more than one position in the queue isn’t supported.

## Parameters

- `item`: The player item to insert.
- `afterItem`: The player item in the queue to follow. Pass `nil` to test if you can append the item to the queue.

## See Also

### Managing the player queue
- [func items() -> [AVPlayerItem]](./items%28%29.md)
  Returns an array of the currently enqueued items.
- [func advanceToNextItem()](./advancetonextitem%28%29.md)
  Ends playback of the current item and starts playback of the next item in the player’s queue.
- [func insert(AVPlayerItem, after: AVPlayerItem?)](./insert%28_,after%29.md)
  Inserts a player item after another player item in the queue.
- [func remove(AVPlayerItem)](./remove%28_%29.md)
  Removes a given player item from the queue.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all player items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer/caninsert(_:after:))*