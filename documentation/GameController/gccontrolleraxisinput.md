# GCControllerAxisInput

**Framework**: Game Controller  
**Kind**: class

A control element that tracks movement along an axis.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerAxisInput
```

#### Overview

A `GCControllerAxisInput` object represents the value of a physical controller’s axis. For example, a [`GCControllerDirectionPad`](gccontrollerdirectionpad.md) has x-axis and y-axis subelements.

## Topics

### Accessing the input values
- [var value: Float](gccontrolleraxisinput/value.md)
  The current value of the axis.
- [func setValue(Float)](gccontrolleraxisinput/setvalue(_:).md)
  Sets the normalized value of the axis.
### Getting change information
- [var valueChangedHandler: GCControllerAxisValueChangedHandler?](gccontrolleraxisinput/valuechangedhandler.md)
  The block that the element calls when the user changes the axis value.
- [typealias GCControllerAxisValueChangedHandler](gccontrolleraxisvaluechangedhandler.md)
  The signature for the block that executes when the user changes the axis value.

## Relationships

### Inherits From
- [GCControllerElement](gccontrollerelement.md)
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
- [class GCControllerButtonInput](gccontrollerbuttoninput.md)
  A control element that represents a button touch or press.
- [class GCControllerTouchpad](gccontrollertouchpad.md)
  A control element that represents a touch event on a touchpad.
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput)*