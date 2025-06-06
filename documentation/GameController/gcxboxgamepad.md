# GCXboxGamepad

**Framework**: Game Controller  
**Kind**: class

A controller profile that supports the Xbox controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCXboxGamepad
```

#### Overview

The Xbox controller profile is similar to an extended game pad ([`GCExtendedGamepad`](gcextendedgamepad.md)), but has four paddle button elements.

![An illustration of an Xbox controller with callouts for the four paddle buttons.](https://docs-assets.developer.apple.com/published/3ccf0bede2983f79a0c53d026b50ebc8/media-3830808%402x.png)

## Topics

### Getting button inputs
- [var paddleButton1: GCControllerButtonInput?](gcxboxgamepad/paddlebutton1.md)
  The controller’s paddle 1 button element, which has a P1 label on the back of the controller.
- [var paddleButton2: GCControllerButtonInput?](gcxboxgamepad/paddlebutton2.md)
  The paddle 2 button element, which has a P2 label on the back of the controller.
- [var paddleButton3: GCControllerButtonInput?](gcxboxgamepad/paddlebutton3.md)
  The paddle 3 button element, which has a P3 label on the back of the controller.
- [var paddleButton4: GCControllerButtonInput?](gcxboxgamepad/paddlebutton4.md)
  The paddle 4 button element, which has a P4 label on the back of the controller.
- [var buttonShare: GCControllerButtonInput?](gcxboxgamepad/buttonshare.md)
  The share button on an Xbox Series X|S controller or later.
### Accessing elements by name
- [Xbox controller input names](xbox-controller-input-names.md)
  Constants for names of Xbox elements.

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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcxboxgamepad)*