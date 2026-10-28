# remove(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a given player item from the queue.

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
func remove(_ item: AVPlayerItem)
```

```objc
- (void) removeItem:(AVPlayerItem *) item;
```

## Discussion

If the item is currently playing, calling this method has the same effect as calling the [`advanceToNextItem()`](./advancetonextitem%28%29.md) method.

## Parameters

- `item`: The player item to remove from the queue.

## See Also

### Managing the player queue
- [func items() -> [AVPlayerItem]](./items%28%29.md)
  Returns an array of the currently enqueued items.
- [func advanceToNextItem()](./advancetonextitem%28%29.md)
  Ends playback of the current item and starts playback of the next item in the player’s queue.
- [func canInsert(AVPlayerItem, after: AVPlayerItem?) -> Bool](./caninsert%28_,after%29.md)
  Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [func insert(AVPlayerItem, after: AVPlayerItem?)](./insert%28_,after%29.md)
  Inserts a player item after another player item in the queue.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all player items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer/remove(_:))*