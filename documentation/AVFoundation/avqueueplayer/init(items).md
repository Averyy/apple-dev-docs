# init(items:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that plays a queue of items.

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
init(items: [AVPlayerItem])
```

```objc
- (instancetype) initWithItems:(NSArray<AVPlayerItem *> *) items;
```

## Parameters

- `items`: The array of player items with which to populate the queue.

## See Also

### Creating a queue player
- [+ queuePlayerWithItems:](./queueplayerwithitems_.md)
  Returns an object that plays a queue of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer/init(items:))*