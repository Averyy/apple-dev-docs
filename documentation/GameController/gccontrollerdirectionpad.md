# GCControllerDirectionPad

**Framework**: Game Controller  
**Kind**: class

A control element associated with a directional pad or a thumbstick.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerDirectionPad
```

#### Overview

You get the input values for this element from its subelements. You can use either the [`xAxis`](gccontrollerdirectionpad/xaxis.md) and [`yAxis`](gccontrollerdirectionpad/yaxis.md) properties to get coordinates, or the [`up`](gccontrollerdirectionpad/up.md), [`down`](gccontrollerdirectionpad/down.md), [`left`](gccontrollerdirectionpad/left.md), and [`right`](gccontrollerdirectionpad/right.md) buttons that simulate directional pad buttons.

## Topics

### Accessing values using the axes
- [var xAxis: GCControllerAxisInput](gccontrollerdirectionpad/xaxis.md)
  The x-axis element of the directional pad.
- [var yAxis: GCControllerAxisInput](gccontrollerdirectionpad/yaxis.md)
  The y-axis element of the directional pad.
### Accessing values using directional buttons
- [var right: GCControllerButtonInput](gccontrollerdirectionpad/right.md)
  The button element that changes the positive x-axis.
- [var left: GCControllerButtonInput](gccontrollerdirectionpad/left.md)
  The button element that changes the negative x-axis.
- [var up: GCControllerButtonInput](gccontrollerdirectionpad/up.md)
  The button element that changes the positive y-axis.
- [var down: GCControllerButtonInput](gccontrollerdirectionpad/down.md)
  The button element used for the negative y-axis direction.
### Getting change information
- [var valueChangedHandler: GCControllerDirectionPadValueChangedHandler?](gccontrollerdirectionpad/valuechangedhandler.md)
  The block that the directional pad calls when the user changes its values.
- [typealias GCControllerDirectionPadValueChangedHandler](gccontrollerdirectionpadvaluechangedhandler.md)
  The signature for the block that executes when either axis changes values.
### Setting snapshot values
- [func setValueForXAxis(Float, yAxis: Float)](gccontrollerdirectionpad/setvalueforxaxis(_:yaxis:).md)
  Sets the input values of a snapshot of a directional pad.

## Relationships

### Inherits From
- [GCControllerElement](gccontrollerelement.md)
### Inherited By
- [GCDeviceCursor](gcdevicecursor.md)
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
- [class GCControllerTouchpad](gccontrollertouchpad.md)
  A control element that represents a touch event on a touchpad.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad)*