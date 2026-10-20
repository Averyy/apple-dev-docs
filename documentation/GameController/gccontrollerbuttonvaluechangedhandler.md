# GCControllerButtonValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(GCControllerButtonInput *, float, _Bool) GCControllerButtonValueChangedHandler;
```

## Parameters

- `button`: The button element whose state changed.
- `value`: A normalized number between `0.0` (minimum) and `1.0` (maximum) that represents the amount of physical or simulated pressure that the user applies to the button.
- `pressed`: A Boolean value that indicates whether the user is pressing the button. If [`true`](../Swift/true.md), the user is pressing the button and the `value` parameter contains the amount of pressure. If [`false`](../Swift/false.md), the user isn’t applying any pressure and the `value` parameter is `0.0`.

## See Also

### Getting change information
- [var touchedChangedHandler: GCControllerButtonTouchedChangedHandler?](./gccontrollerbuttoninput/touchedchangedhandler.md)
  The block that the element calls when the user touches the button.
- [typealias GCControllerButtonTouchedChangedHandler](./gccontrollerbuttontouchedchangedhandler.md)
  The signature for the block that executes when the user touches the button if the controller supports that feature.
- [var pressedChangedHandler: GCControllerButtonValueChangedHandler?](./gccontrollerbuttoninput/pressedchangedhandler.md)
  The block that the element calls when the user presses or releases the button.
- [var valueChangedHandler: GCControllerButtonValueChangedHandler?](./gccontrollerbuttoninput/valuechangedhandler.md)
  The block that the element calls when the user changes the level of pressure on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttonvaluechangedhandler)*