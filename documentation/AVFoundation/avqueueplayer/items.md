# items()

**Framework**: AVFoundation  
**Kind**: method

Returns an array of the currently enqueued items.

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
func items() -> [AVPlayerItem]
```

#### Return Value

An array of the currently enqueued player items.

#### Discussion

The array contains [`AVPlayerItem`](avplayeritem.md) objects currently in the player’s queue.

## See Also

- [func advanceToNextItem()](avqueueplayer/advancetonextitem.md)
  Ends playback of the current item and starts playback of the next item in the player’s queue.
- [func canInsert(AVPlayerItem, after: AVPlayerItem?) -> Bool](avqueueplayer/caninsert(_:after:).md)
  Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [func insert(AVPlayerItem, after: AVPlayerItem?)](avqueueplayer/insert(_:after:).md)
  Inserts a player item after another player item in the queue.
- [func remove(AVPlayerItem)](avqueueplayer/remove(_:).md)
  Removes a given player item from the queue.
- [func removeAllItems()](avqueueplayer/removeallitems.md)
  Removes all player items from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer/items())*