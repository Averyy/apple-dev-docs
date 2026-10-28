# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the gesture recognizer is enabled.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

Disables a gesture recognizers so it does not receive touches. The default value is [`true`](../../Swift/true.md). If you change this property to [`false`](../../Swift/false.md) while a gesture recognizer is currently recognizing a gesture, the gesture recognizer transitions to a cancelled state.

## See Also

### Getting the recognizer’s state and view
- [var state: UIGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
- [UIGestureRecognizer.State](./state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var view: UIView?](./view.md)
  The view the gesture recognizer is attached to.
- [var buttonMask: UIEvent.ButtonMask](./buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](./modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/isenabled)*