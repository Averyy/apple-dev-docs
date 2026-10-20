# AVPlayerLooper.ItemOrdering

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that define the ordering of items in a player looper.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum ItemOrdering
```

```c
enum AVPlayerLooperItemOrdering : NSInteger;
```

## Topics

### Ordering
- [AVPlayerLooper.ItemOrdering.loopingItemsPrecedeExistingItems](./itemordering/loopingitemsprecedeexistingitems.md)
  Indicates to insert replica items before any existing items in the specified player’s queue.
- [AVPlayerLooper.ItemOrdering.loopingItemsFollowExistingItems](./itemordering/loopingitemsfollowexistingitems.md)
  Indicates to insert replica items after any existing items in the specified player’s queue.
### Initializers
- [init?(rawValue: Int)](./itemordering/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/itemordering)*