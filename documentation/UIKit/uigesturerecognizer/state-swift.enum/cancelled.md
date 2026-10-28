# UIGestureRecognizer.State.cancelled

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case cancelled
```

```c
UIGestureRecognizerStateCancelled
```

## Mentions

- [About the Gesture Recognizer State Machine](../../about-the-gesture-recognizer-state-machine.md)

## Discussion

The gesture recognizer sends its action message (or messages) at the next cycle of the run loop and resets its state to [`UIGestureRecognizer.State.possible`](./possible.md).

## See Also

### Constants
- [UIGestureRecognizer.State.possible](./possible.md)
  The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizer.State.began](./began.md)
  The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizer.State.changed](./changed.md)
  The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizer.State.ended](./ended.md)
  The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizer.State.failed](./failed.md)
  The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [static var recognized: UIGestureRecognizer.State](./recognized.md)
  The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum/cancelled)*