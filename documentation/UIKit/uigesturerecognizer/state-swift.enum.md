# UIGestureRecognizer.State

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the current state a gesture recognizer is in.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum State
```

```c
enum UIGestureRecognizerState : NSInteger;
```

## Overview

Gesture recognizers recognize a discrete event such as a tap or a swipe but don’t report changes within the gesture. In other words, discrete gestures don’t transition through the Began and Changed states and they can’t fail or be canceled.

## Topics

### Constants
- [UIGestureRecognizer.State.possible](./state-swift.enum/possible.md)
  The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizer.State.began](./state-swift.enum/began.md)
  The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizer.State.changed](./state-swift.enum/changed.md)
  The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizer.State.ended](./state-swift.enum/ended.md)
  The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizer.State.cancelled](./state-swift.enum/cancelled.md)
  The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizer.State.failed](./state-swift.enum/failed.md)
  The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [static var recognized: UIGestureRecognizer.State](./state-swift.enum/recognized.md)
  The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the recognizer’s state and view
- [var state: UIGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
- [var view: UIView?](./view.md)
  The view the gesture recognizer is attached to.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](./buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](./modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum)*