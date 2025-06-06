# GCDualSenseGamepad

**Framework**: Game Controller  
**Kind**: class

A controller profile that supported the DualSense controller.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
class GCDualSenseGamepad
```

#### Overview

The DualSense controller profile is similar to a DualShock profile ([`GCDualShockGamepad`](gcdualshockgamepad.md)), but has adaptive triggers that allow you to specify a dynamic resistance force when the user pulls the trigger. For example, you can emulate the feeling of pulling back a bow string, firing a weapon, or pulling a lever.

This profile also supports motion — that is, the controller’s [`motion`](gccontroller/motion.md) property is non-nil. If you hold the controller in front of you, the direction of the axes are:

- The positive x-axis points to your right.
- The positive y-axis points up out of the USB-C port.
- The positive z-axis starts at the touchpad and points to you.

## Topics

### Getting button input
- [var touchpadButton: GCControllerButtonInput](gcdualsensegamepad/touchpadbutton.md)
  The button element on the touchpad of the controller.
### Tracking finger locations
- [var touchpadPrimary: GCControllerDirectionPad](gcdualsensegamepad/touchpadprimary.md)
  The location of the player’s primary finger on the touchpad.
- [var touchpadSecondary: GCControllerDirectionPad](gcdualsensegamepad/touchpadsecondary.md)
  The location of the player’s secondary finger on the touchpad.
### Getting adaptive triggers
- [var leftTrigger: GCDualSenseAdaptiveTrigger](gcdualsensegamepad/lefttrigger.md)
  The controller’s left adaptive trigger element.
- [var rightTrigger: GCDualSenseAdaptiveTrigger](gcdualsensegamepad/righttrigger.md)
  The controller’s right adaptive trigger element.

## Relationships

### Inherits From
- [GCExtendedGamepad](gcextendedgamepad.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var extendedGamepad: GCExtendedGamepad?](gccontroller/extendedgamepad.md)
  The extended gamepad profile.
- [class GCPhysicalInputProfile](gcphysicalinputprofile.md)
  The base class for controller profiles that support physical buttons, thumbsticks, and directional pads.
- [class GCKeyboardInput](gckeyboardinput.md)
  A controller profile that uses the keyboard as the input device.
- [class GCMouseInput](gcmouseinput.md)
  A controller profile that tracks input from a mouse.
- [class GCExtendedGamepad](gcextendedgamepad.md)
  A controller profile that supports the extended set of gamepad controls.
- [class GCDualShockGamepad](gcdualshockgamepad.md)
  A controller profile that supports the DualShock 4 controller.
- [class GCXboxGamepad](gcxboxgamepad.md)
  A controller profile that supports the Xbox controller.
- [var microGamepad: GCMicroGamepad?](gccontroller/microgamepad.md)
  The micro gamepad profile.
- [class GCMicroGamepad](gcmicrogamepad.md)
  A controller profile that supports the Siri Remote.
- [class GCDirectionalGamepad](gcdirectionalgamepad.md)
  A profile that supports only the directional pad, without motion or rotation.
- [var motion: GCMotion?](gccontroller/motion.md)
  The motion input profile.
- [var physicalInputProfile: GCPhysicalInputProfile](gccontroller/physicalinputprofile.md)
  The physical input profile for the controller.
- [var gamepad: GCGamepad?](gccontroller/gamepad.md)
  The gamepad profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsensegamepad)*