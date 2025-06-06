# phase

**Framework**: BrowserEngineKit  
**Kind**: property

The point in the scrolling lifecycle represented by the scroll update.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
var phase: BEScrollViewScrollUpdate.Phase { get }
```

#### Overview

The phases of a scroll update represent a state machine:

1. A scroll gesture is initially in the [`BEScrollViewScrollUpdate.Phase.began`](bescrollviewscrollupdate/phase-swift.enum/began.md) phase, when the person puts their finger down in the scroll view.
2. As the person interacts with the scroll view, the system generates zero or more [`BEScrollViewScrollUpdate.Phase.changed`](bescrollviewscrollupdate/phase-swift.enum/changed.md) updates for the scroll gesture.
3. Finally, the scroll gesture either enters the [`BEScrollViewScrollUpdate.Phase.ended`](bescrollviewscrollupdate/phase-swift.enum/ended.md) phase when the person stops interacting with the scroll view; or it becomes [`BEScrollViewScrollUpdate.Phase.cancelled`](bescrollviewscrollupdate/phase-swift.enum/cancelled.md) when the operating system receives another event that means it stops tracking the scroll gesture.

## See Also

- [var timestamp: TimeInterval](bescrollviewscrollupdate/timestamp.md)
  The time at which the scroll update occurred.
- [BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.enum.md)
  The phase of a scroll update in a scroll gesture’s lifecycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/phase-swift.property)*