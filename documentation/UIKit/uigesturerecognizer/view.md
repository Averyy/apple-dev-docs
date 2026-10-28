# view

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view the gesture recognizer is attached to.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var view: UIView? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIView * view;
```

## Discussion

You attach (or add) a gesture recognizer to a `UIView` object using the [`addGestureRecognizer(_:)`](../uiview/addgesturerecognizer%28_%29.md) method.

## See Also

### Getting the recognizer’s state and view
- [var state: UIGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
- [UIGestureRecognizer.State](./state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](./buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](./modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/view)*