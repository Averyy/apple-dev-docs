# view

**Framework**: UIKit  
**Kind**: property

The view the gesture recognizer is attached to.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var view: UIView? { get }
```

#### Discussion

You attach (or add) a gesture recognizer to a `UIView` object using the [`addGestureRecognizer(_:)`](uiview/addgesturerecognizer(_:).md) method.

## See Also

- [var state: UIGestureRecognizer.State](uigesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [UIGestureRecognizer.State](uigesturerecognizer/state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var isEnabled: Bool](uigesturerecognizer/isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](uigesturerecognizer/buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](uigesturerecognizer/modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/view)*