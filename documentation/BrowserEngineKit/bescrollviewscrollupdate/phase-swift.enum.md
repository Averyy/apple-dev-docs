# BEScrollViewScrollUpdate.Phase

**Framework**: BrowserEngineKit  
**Kind**: enum  
**Role**: Enumeration

Phases in the scroll gesture life cycle.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
enum Phase
```

```c
enum BEScrollViewScrollUpdatePhase : NSInteger;
```

## Topics

### Enumeration Cases
- [BEScrollViewScrollUpdate.Phase.began](./phase-swift.enum/began.md)
  The scroll phase that indicates the gesture has begun.
- [BEScrollViewScrollUpdate.Phase.cancelled](./phase-swift.enum/cancelled.md)
  A scroll phase that indicates the system stops scroll view gesture tracking due to an event.
- [BEScrollViewScrollUpdate.Phase.changed](./phase-swift.enum/changed.md)
  A scroll phase that indicates the gesture changes scroll location.
- [BEScrollViewScrollUpdate.Phase.ended](./phase-swift.enum/ended.md)
  A scroll phase that indicates the scroll gesture has ended.
### Initializers
- [init?(rawValue: Int)](./phase-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving scroll state information
- [var timestamp: TimeInterval](./timestamp.md)
  The time at which a scroll update occurs.
- [var phase: BEScrollViewScrollUpdate.Phase](./phase-swift.property.md)
  A value that indicates the scroll update’s position in the scrolling life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/phase-swift.enum)*