# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean property that indicates whether the gesture recognizer is enabled.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

Disables a gesture recognizers so it does not receive touches. The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If you change this property to [`false`](https://developer.apple.com/documentation/Swift/false) while a gesture recognizer is currently recognizing a gesture, the gesture recognizer transitions to a cancelled state.

## See Also

- [var state: UIGestureRecognizer.State](uigesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [UIGestureRecognizer.State](uigesturerecognizer/state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var view: UIView?](uigesturerecognizer/view.md)
  The view the gesture recognizer is attached to.
- [var buttonMask: UIEvent.ButtonMask](uigesturerecognizer/buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](uigesturerecognizer/modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/isenabled)*