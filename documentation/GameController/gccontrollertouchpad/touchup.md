# touchUp

**Framework**: Game Controller  
**Kind**: property

The block that the element calls when the user finishes touching the touchpad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var touchUp: GCControllerTouchpadHandler? { get set }
```

#### Discussion

The element invokes this handler when the user removes their fingers from the touchpad.

## See Also

- [var touchDown: GCControllerTouchpadHandler?](gccontrollertouchpad/touchdown.md)
  The block that the element calls when the user begins touching the touchpad.
- [var touchMoved: GCControllerTouchpadHandler?](gccontrollertouchpad/touchmoved.md)
  The block that the element calls when the user continues touching the touchpad, not when the user begins or ends touching the touchpad.
- [typealias GCControllerTouchpadHandler](gccontrollertouchpadhandler.md)
  The signature for the block that executes when the user interacts with the touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/touchup)*