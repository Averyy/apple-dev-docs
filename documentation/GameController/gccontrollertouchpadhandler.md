# GCControllerTouchpadHandler

**Framework**: Game Controller  
**Kind**: typealias

The signature for the block that executes when the user interacts with the touchpad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCControllerTouchpadHandler = (GCControllerTouchpad, Float, Float, Float, Bool) -> Void
```

## Parameters

- `touchpad`: The touchpad that the user interacts with.
- `xValue`: A normalized value of the x-axis touch location ranging from   to  .
- `yValue`: A normalized value of the y-axis touch location ranging from   to  .
- `buttonValue`: A normalized number between   (minimum) and   (maximum) that represents the level of pressure the user applies to the touchpad button.
- `buttonPressed`: A Boolean value that indicates whether the user is pressing the touchpad button. If  , the user is pressing the button; otherwise, the user isn’t.

## See Also

- [var touchDown: GCControllerTouchpadHandler?](gccontrollertouchpad/touchdown.md)
  The block that the element calls when the user begins touching the touchpad.
- [var touchMoved: GCControllerTouchpadHandler?](gccontrollertouchpad/touchmoved.md)
  The block that the element calls when the user continues touching the touchpad, not when the user begins or ends touching the touchpad.
- [var touchUp: GCControllerTouchpadHandler?](gccontrollertouchpad/touchup.md)
  The block that the element calls when the user finishes touching the touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpadhandler)*