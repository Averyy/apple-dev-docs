# UIGestureRecognizer.State.changed

**Framework**: UIKit  
**Kind**: case

The gesture recognizer has received touches recognized as a change to a continuous gesture.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case changed
```

## Mentions

- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
- [Handling long-press gestures](handling-long-press-gestures.md)
- [Handling pan gestures](handling-pan-gestures.md)
- [Handling pinch gestures](handling-pinch-gestures.md)
- [Handling rotation gestures](handling-rotation-gestures.md)

#### Discussion

It sends its action message (or messages) at the next cycle of the run loop.

## See Also

- [UIGestureRecognizer.State.possible](uigesturerecognizer/state-swift.enum/possible.md)
  The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizer.State.began](uigesturerecognizer/state-swift.enum/began.md)
  The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizer.State.ended](uigesturerecognizer/state-swift.enum/ended.md)
  The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizer.State.cancelled](uigesturerecognizer/state-swift.enum/cancelled.md)
  The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizer.State.failed](uigesturerecognizer/state-swift.enum/failed.md)
  The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [static var recognized: UIGestureRecognizer.State](uigesturerecognizer/state-swift.enum/recognized.md)
  The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum/changed)*