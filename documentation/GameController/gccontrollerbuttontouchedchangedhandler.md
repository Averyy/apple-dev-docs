# GCControllerButtonTouchedChangedHandler

**Framework**: Game Controller  
**Kind**: typealias

The signature for the block that executes when the user touches the button if the controller supports that feature.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCControllerButtonTouchedChangedHandler = (GCControllerButtonInput, Float, Bool, Bool) -> Void
```

## Parameters

- `button`: The button element whose value changed.
- `value`: A normalized number between   (minimum) and   (maximum) that represents the amount of physical or simulated pressure that the user applies to the button.
- `pressed`: A Boolean value that indicates whether the user is pressing the button. If  , the user is pressing the button and the   parameter contains the amount of pressure. If  , the user isn’t applying any pressure and the   parameter is  .
- `touched`: A Boolean value that indicates whether the user is touching the button. If  , the user is touching the button; otherwise, the user isn’t.

## See Also

- [var touchedChangedHandler: GCControllerButtonTouchedChangedHandler?](gccontrollerbuttoninput/touchedchangedhandler.md)
  The block that the element calls when the user touches the button.
- [var pressedChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/pressedchangedhandler.md)
  The block that the element calls when the user presses or releases the button.
- [var valueChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/valuechangedhandler.md)
  The block that the element calls when the user changes the level of pressure on the button.
- [typealias GCControllerButtonValueChangedHandler](gccontrollerbuttonvaluechangedhandler.md)
  The signature for the block that executes when a button’s state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttontouchedchangedhandler)*