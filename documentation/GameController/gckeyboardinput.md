# GCKeyboardInput

**Framework**: Game Controller  
**Kind**: class

A controller profile that uses the keyboard as the input device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCKeyboardInput
```

#### Overview

Use this profile to get the state of the keyboard buttons that the [`GCKeyCode`](gckeycode.md) structure defines.

## Topics

### Getting Change Information
- [var keyChangedHandler: GCKeyboardValueChangedHandler?](gckeyboardinput/keychangedhandler.md)
  The block that the profile calls when the user presses a key.
- [typealias GCKeyboardValueChangedHandler](gckeyboardvaluechangedhandler.md)
  The signature for the block that the keyboard input profile calls when a key value changes.
### Accessing Buttons
- [var isAnyKeyPressed: Bool](gckeyboardinput/isanykeypressed.md)
  A Boolean value that indicates whether the user is pressing any of the keys.
- [func button(forKeyCode: GCKeyCode) -> GCControllerButtonInput?](gckeyboardinput/button(forkeycode:).md)
  Returns the button element for the specified key code.
- [struct GCKeyCode](gckeycode.md)
  The key codes for keys on a keyboard.
- [Keycode Constants](keycode-constants.md)
  Constants for the codes of keyboard keys.

## Relationships

### Inherits From
- [GCPhysicalInputProfile](gcphysicalinputprofile.md)
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
- [class GCMouseInput](gcmouseinput.md)
  A controller profile that tracks input from a mouse.
- [class GCExtendedGamepad](gcextendedgamepad.md)
  A controller profile that supports the extended set of gamepad controls.
- [class GCDualShockGamepad](gcdualshockgamepad.md)
  A controller profile that supports the DualShock 4 controller.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboardinput)*