# GCControllerTouchpad

**Framework**: Game Controller  
**Kind**: class

A control element that represents a touch event on a touchpad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerTouchpad
```

#### Overview

A `GCControllerTouchpad` object provides the state of the touches and presses on a touchpad. This is a compound element with button and directional pad subelements.

## Topics

### Getting the subelements
- [var touchSurface: GCControllerDirectionPad](gccontrollertouchpad/touchsurface.md)
  The element that represents the state of the user’s touch on the surface of the touchpad.
- [var button: GCControllerButtonInput](gccontrollertouchpad/button.md)
  The element that represents the button component on the touchpad.
### Accessing the input values
- [var touchState: GCControllerTouchpad.TouchState](gccontrollertouchpad/touchstate-swift.property.md)
  The state of the user’s touch on the surface of the touchpad.
- [GCControllerTouchpad.TouchState](gccontrollertouchpad/touchstate-swift.enum.md)
  The possible states of the user’s touch.
- [var reportsAbsoluteTouchSurfaceValues: Bool](gccontrollertouchpad/reportsabsolutetouchsurfacevalues.md)
  A Boolean value that determines whether the touch values are absolute or relative.
### Getting change information
- [var touchDown: GCControllerTouchpadHandler?](gccontrollertouchpad/touchdown.md)
  The block that the element calls when the user begins touching the touchpad.
- [var touchMoved: GCControllerTouchpadHandler?](gccontrollertouchpad/touchmoved.md)
  The block that the element calls when the user continues touching the touchpad, not when the user begins or ends touching the touchpad.
- [var touchUp: GCControllerTouchpadHandler?](gccontrollertouchpad/touchup.md)
  The block that the element calls when the user finishes touching the touchpad.
- [typealias GCControllerTouchpadHandler](gccontrollertouchpadhandler.md)
  The signature for the block that executes when the user interacts with the touchpad.
### Setting snapshot values
- [func setValueForXAxis(Float, yAxis: Float, touchDown: Bool, buttonValue: Float)](gccontrollertouchpad/setvalueforxaxis(_:yaxis:touchdown:buttonvalue:).md)
  Sets the input values of a snapshot of a touchpad.

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
- [class GCControllerAxisInput](gccontrolleraxisinput.md)
  A control element that tracks movement along an axis.
- [class GCControllerButtonInput](gccontrollerbuttoninput.md)
  A control element that represents a button touch or press.
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad)*