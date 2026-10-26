# queuePlayerWithItems:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an object that plays a queue of items.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) queuePlayerWithItems:(NSArray<AVPlayerItem *> *) items;
```

#### Return Value

A new queue player.

## Parameters

- `items`: An array of [`AVPlayerItem`](../avplayeritem.md) objects with which to initially populate the player’s queue.

## See Also

### Creating a queue player
- [init(items: [AVPlayerItem])](./init%28items%29.md)
  Creates an object that plays a queue of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer/queueplayerwithitems:)*