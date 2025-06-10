# BEScrollViewScrollUpdate.Phase

**Framework**: BrowserEngineKit  
**Kind**: enum

The phase of a scroll update in a scroll gesture’s lifecycle.

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
  The scroll gesture began.
- [BEScrollViewScrollUpdate.Phase.cancelled](bescrollviewscrollupdate/phase-swift.enum/cancelled.md)
  The operating system detected an event that caused it to stop tracking the scroll gesture.
- [BEScrollViewScrollUpdate.Phase.changed](bescrollviewscrollupdate/phase-swift.enum/changed.md)
  The scroll gesture changed the scroll location.
- [BEScrollViewScrollUpdate.Phase.ended](bescrollviewscrollupdate/phase-swift.enum/ended.md)
  The scroll gesture came to an end.
### Initializers
- [init?(rawValue: Int)](bescrollviewscrollupdate/phase-swift.enum/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](bescrollviewscrollupdate/phase-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](bescrollviewscrollupdate/phase-swift.enum/rawrepresentable-implementations.md)

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
  The time at which the scroll update occurred.
- [var phase: BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.property.md)
  The point in the scrolling lifecycle represented by the scroll update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/phase-swift.enum)*