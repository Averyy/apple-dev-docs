# UIGestureRecognizer.State

**Framework**: UIKit  
**Kind**: enum

Constants that represent the current state a gesture recognizer is in.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum State
```

#### Overview

Gesture recognizers recognize a discrete event such as a tap or a swipe but don’t report changes within the gesture. In other words, discrete gestures don’t transition through the Began and Changed states and they can’t fail or be canceled.

## Topics

### Constants
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
- [static var recognized: UIGestureRecognizer.State](uigesturerecognizer/state-swift.enum/recognized.md)
  The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.
### Initializers
- [init?(rawValue: Int)](uigesturerecognizer/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: UIGestureRecognizer.State](uigesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [var view: UIView?](uigesturerecognizer/view.md)
  The view the gesture recognizer is attached to.
- [var isEnabled: Bool](uigesturerecognizer/isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](uigesturerecognizer/buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](uigesturerecognizer/modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum)*