# recognized

**Framework**: UIKit  
**Kind**: property

The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var recognized: UIGestureRecognizer.State { get }
```

## Mentions

- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)

#### Discussion

The gesture recognizer sends its action message (or messages) at the next cycle of the run loop and resets its state to [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md).

## See Also

- [UIGestureRecognizer.State.possible](uigesturerecognizer/state-swift.enum/possible.md)
  The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizer.State.began](uigesturerecognizer/state-swift.enum/began.md)
  The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizer.State.changed](uigesturerecognizer/state-swift.enum/changed.md)
  The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizer.State.ended](uigesturerecognizer/state-swift.enum/ended.md)
  The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizer.State.cancelled](uigesturerecognizer/state-swift.enum/cancelled.md)
  The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizer.State.failed](uigesturerecognizer/state-swift.enum/failed.md)
  The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum/recognized)*