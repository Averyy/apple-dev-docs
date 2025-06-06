# GCDeviceCursor

**Framework**: Game Controller  
**Kind**: class

A control element for the cursor used as a directional pad.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCDeviceCursor
```

#### Overview

This controller element allows you to use the cursor as a directional pad with the values of the [`xAxis`](gccontrollerdirectionpad/xaxis.md) and [`yAxis`](gccontrollerdirectionpad/yaxis.md) elements scaled to the width and height of the screen, not ranging from `-1` to `1`.

## Relationships

### Inherits From
- [GCControllerDirectionPad](gccontrollerdirectionpad.md)
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
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicecursor)*