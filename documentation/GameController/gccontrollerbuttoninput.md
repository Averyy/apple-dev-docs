# GCControllerButtonInput

**Framework**: Game Controller  
**Kind**: class

A control element that represents a button touch or press.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerButtonInput
```

#### Overview

A `GCControllerButtonInput` object represents a button on a controller that can report either analog or digital values.

## Topics

### Accessing input values
- [var isTouched: Bool](gccontrollerbuttoninput/istouched.md)
  A Boolean value that indicates whether the user is touching the button.
- [var isPressed: Bool](gccontrollerbuttoninput/ispressed.md)
  A Boolean value that indicates whether the user is pressing the button.
- [var value: Float](gccontrollerbuttoninput/value.md)
  The level of pressure the user is applying to the button.
### Getting change information
- [var touchedChangedHandler: GCControllerButtonTouchedChangedHandler?](gccontrollerbuttoninput/touchedchangedhandler.md)
  The block that the element calls when the user touches the button.
- [typealias GCControllerButtonTouchedChangedHandler](gccontrollerbuttontouchedchangedhandler.md)
  The signature for the block that executes when the user touches the button if the controller supports that feature.
- [var pressedChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/pressedchangedhandler.md)
  The block that the element calls when the user presses or releases the button.
- [var valueChangedHandler: GCControllerButtonValueChangedHandler?](gccontrollerbuttoninput/valuechangedhandler.md)
  The block that the element calls when the user changes the level of pressure on the button.
- [typealias GCControllerButtonValueChangedHandler](gccontrollerbuttonvaluechangedhandler.md)
  The signature for the block that executes when a button’s state changes.
### Setting snapshot values
- [func setValue(Float)](gccontrollerbuttoninput/setvalue(_:).md)
  Sets the pressure value of a snapshot of a button.

## Relationships

### Inherits From
- [GCControllerElement](gccontrollerelement.md)
### Inherited By
- [GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCControllerElement](gccontrollerelement.md)
  An input for a physical control, such as a button or thumbstick.
- [class GCControllerAxisInput](gccontrolleraxisinput.md)
  A control element that tracks movement along an axis.
- [class GCControllerTouchpad](gccontrollertouchpad.md)
  A control element that represents a touch event on a touchpad.
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput)*