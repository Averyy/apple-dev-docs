# BEScrollViewScrollUpdate.Phase

**Framework**: BrowserEngineKit  
**Kind**: enum

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

## Topics

### Enumeration Cases
- [BEScrollViewScrollUpdate.Phase.began](bescrollviewscrollupdate/phase-swift.enum/began.md)
  The scroll phase that indicates the gesture has begun.
- [BEScrollViewScrollUpdate.Phase.cancelled](bescrollviewscrollupdate/phase-swift.enum/cancelled.md)
  A scroll phase that indicates the system stops scroll view gesture tracking due to an event.
- [BEScrollViewScrollUpdate.Phase.changed](bescrollviewscrollupdate/phase-swift.enum/changed.md)
  A scroll phase that indicates the gesture changes scroll location.
- [BEScrollViewScrollUpdate.Phase.ended](bescrollviewscrollupdate/phase-swift.enum/ended.md)
  A scroll phase that indicates the scroll gesture has ended.
### Initializers
- [init?(rawValue: Int)](bescrollviewscrollupdate/phase-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var timestamp: TimeInterval](bescrollviewscrollupdate/timestamp.md)
  The time at which a scroll update occurs.
- [var phase: BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.property.md)
  A value that indicates the scroll update’s position in the scrolling life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/phase-swift.enum)*