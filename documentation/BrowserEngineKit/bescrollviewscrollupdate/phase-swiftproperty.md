# phase

**Framework**: BrowserEngineKit  
**Kind**: property

A value that indicates the scroll update’s position in the scrolling life cycle.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var phase: BEScrollViewScrollUpdate.Phase { get }
```

#### Discussion

The phases of a scroll update follow a state machine:

1. A scroll gesture begins in the [`BEScrollViewScrollUpdate.Phase.began`](bescrollviewscrollupdate/phase-swift.enum/began.md) phase when the person places their finger in the scroll view.
2. As the person interacts with the scroll view, the system generates zero or more [`BEScrollViewScrollUpdate.Phase.changed`](bescrollviewscrollupdate/phase-swift.enum/changed.md) updates.
3. The gesture enters the [`BEScrollViewScrollUpdate.Phase.ended`](bescrollviewscrollupdate/phase-swift.enum/ended.md) phase when the person lifts their finger, or the [`BEScrollViewScrollUpdate.Phase.cancelled`](bescrollviewscrollupdate/phase-swift.enum/cancelled.md) phase when another event causes the system to stop tracking the gesture.

## See Also

- [var timestamp: TimeInterval](bescrollviewscrollupdate/timestamp.md)
  The time at which a scroll update occurs.
- [BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.enum.md)
  Phases in the scroll gesture life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/phase-swift.property)*