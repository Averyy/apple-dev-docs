# remove(_:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Removes a media item from the music player’s queue.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ item: MPMediaItem)
```

```objc
- (void) removeItem:(MPMediaItem *) item;
```

## Parameters

- `item`: The media item to remove from the queue.

## See Also

### Adding and removing items
- [func insert(MPMusicPlayerQueueDescriptor, after: MPMediaItem?)](./insert%28_,after%29.md)
  Inserts a modified queue after the designated media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollermutablequeue/remove(_:))*