# GCDualShockGamepad

**Framework**: Game Controller  
**Kind**: class

A controller profile that supports the DualShock 4 controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCDualShockGamepad
```

#### Overview

The DualShock 4 controller profile is similar to an extended gamepad ([`GCExtendedGamepad`](gcextendedgamepad.md)), but has a touchpad with a button and two-finger tracking.

![An illustration of a DualShock 4 controller showing the touchpad.](https://docs-assets.developer.apple.com/published/5c84f963dd6a6fcfc5c95a53c75f49d3/media-3830806%402x.png)

This profile also supports motion — that is, the controller’s [`motion`](gccontroller/motion.md) property is non-nil. If you hold the controller in front of you, the direction of the axes are:

- The positive x-axis points to your right.
- The positive y-axis points up.
- The positive z-axis starts at the touchpad and points to you.

![An illustration of a DualShock 4 controller showing the directions of the x, y, and z axes.](https://docs-assets.developer.apple.com/published/3e9dc14944907fc3a25e41e2cee2a320/media-3856422%402x.png)

## Topics

### Getting button input
- [var touchpadButton: GCControllerButtonInput!](gcdualshockgamepad/touchpadbutton.md)
  The button element on the touchpad of the controller.
### Tracking finger locations
- [var touchpadPrimary: GCControllerDirectionPad!](gcdualshockgamepad/touchpadprimary.md)
  The location of the player’s primary finger on the touchpad.
- [var touchpadSecondary: GCControllerDirectionPad!](gcdualshockgamepad/touchpadsecondary.md)
  The location of the player’s secondary finger on the touchpad.
### Accessing elements by name
- [DualShock controller input names](dualshock-controller-input-names.md)
  Constants for names of DualShock 4 elements.

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
- [class GCXboxGamepad](gcxboxgamepad.md)
  A controller profile that supports the Xbox controller.
- [class GCDualSenseGamepad](gcdualsensegamepad.md)
  A controller profile that supported the DualSense controller.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualshockgamepad)*