# GCControllerButtonValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias

The signature for the block that executes when a button’s state changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCControllerButtonValueChangedHandler = (GCControllerButtonInput, Float, Bool) -> Void
```

## Parameters

- `button`: The button element whose state changed.
- `value`: A normalized number between   (minimum) and   (maximum) that represents the amount of physical or simulated pressure that the user applies to the button.
- `pressed`: A Boolean value that indicates whether the user is pressing the button. If  , the user is pressing the button and the   parameter contains the amount of pressure. If  , the user isn’t applying any pressure and the   parameter is  .

## See Also

- [var touchedChangedHandler: GCControllerButtonTouchedChangedHandler?](gccontrollerbuttoninput/touchedchangedhandler.md)
  The block that the element calls when the user touches the button.
- [typealias GCControllerButtonTouchedChangedHandler](gccontrollerbuttontouchedchangedhandler.md)
  The signature for the block that executes when the user touches the button if the controller supports that feature.
- [var pressedChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/pressedchangedhandler.md)
  The block that the element calls when the user presses or releases the button.
- [var valueChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/valuechangedhandler.md)
  The block that the element calls when the user changes the level of pressure on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttonvaluechangedhandler)*