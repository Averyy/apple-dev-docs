# modifierFlags

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bit mask of modifier flags in the gesture represented by the gesture recognizer.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var modifierFlags: UIKeyModifierFlags { get }
```

```objc
@property (nonatomic, readonly) UIKeyModifierFlags modifierFlags;
```

## See Also

### Getting the recognizer’s state and view
- [var state: UIGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
- [UIGestureRecognizer.State](./state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var view: UIView?](./view.md)
  The view the gesture recognizer is attached to.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](./buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/modifierflags)*