# state

**Framework**: UIKit  
**Kind**: property

The current state of the gesture recognizer.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var state: UIGestureRecognizer.State { get set }
```

## Mentions

- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
- [Handling tap gestures](handling-tap-gestures.md)

#### Discussion

The possible states a gesture recognizer can be in are represented by the constants of type [`UIGestureRecognizer.State`](uigesturerecognizer/state-swift.enum.md). Some of these states aren’t applicable to discrete gestures. The read-only version of the [`state`](uigesturerecognizer/state-swift.property.md) property is intended for clients of a gesture-recognizer class and not subclasses.

##### Special Considerations

Subclasses of [`UIGestureRecognizer`](uigesturerecognizer.md) must use a read-write version of the state property. They get this redeclaration when they import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift):

```objc
@property(nonatomic,readwrite) UIGestureRecognizerState state;
```

Recognizers for discrete gestures transition from [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) to [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md) or [`recognized`](uigesturerecognizer/state-swift.enum/recognized.md). Recognizers for continuous gesture transition from [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md) to these phases in the given order: [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md), [`UIGestureRecognizer.State.changed`](uigesturerecognizer/state-swift.enum/changed.md), and [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md). If, however, they receive a cancellation touch, they should transition to [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md). If recognizers for continuous gestures can’t interpret a multi-touch sequence as their gesture, they transition to [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md).

## See Also

- [UIGestureRecognizer.State](uigesturerecognizer/state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var view: UIView?](uigesturerecognizer/view.md)
  The view the gesture recognizer is attached to.
- [var isEnabled: Bool](uigesturerecognizer/isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](uigesturerecognizer/buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](uigesturerecognizer/modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.property)*