# pressedChangedHandler

**Framework**: Game Controller  
**Kind**: property

The block that the element calls when the user presses or releases the button.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var pressedChangedHandler: GCControllerButtonValueChangedHandler? { get set }
```

#### Discussion

Set this handler when you only want to know when the user presses or releases the button — that is, when the [`isPressed`](gccontrollerbuttoninput/ispressed.md) property changes.

## See Also

- [var touchedChangedHandler: GCControllerButtonTouchedChangedHandler?](gccontrollerbuttoninput/touchedchangedhandler.md)
  The block that the element calls when the user touches the button.
- [typealias GCControllerButtonTouchedChangedHandler](gccontrollerbuttontouchedchangedhandler.md)
  The signature for the block that executes when the user touches the button if the controller supports that feature.
- [var valueChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/valuechangedhandler.md)
  The block that the element calls when the user changes the level of pressure on the button.
- [typealias GCControllerButtonValueChangedHandler](gccontrollerbuttonvaluechangedhandler.md)
  The signature for the block that executes when a button’s state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/pressedchangedhandler)*