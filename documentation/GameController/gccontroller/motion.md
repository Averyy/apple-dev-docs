# motion

**Framework**: Game Controller  
**Kind**: property

The motion input profile.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var motion: GCMotion? { get }
```

#### Discussion

If the controller supports the motion profile, this property is a [`GCMotion`](gcmotion.md) object that you use to access the controller’s motion data. If the controller doesn’t support the motion input profile, this property is `nil`.

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
- [class GCDualSenseGamepad](gcdualsensegamepad.md)
  A controller profile that supported the DualSense controller.
- [var microGamepad: GCMicroGamepad?](gccontroller/microgamepad.md)
  The micro gamepad profile.
- [class GCMicroGamepad](gcmicrogamepad.md)
  A controller profile that supports the Siri Remote.
- [class GCDirectionalGamepad](gcdirectionalgamepad.md)
  A profile that supports only the directional pad, without motion or rotation.
- [var physicalInputProfile: GCPhysicalInputProfile](gccontroller/physicalinputprofile.md)
  The physical input profile for the controller.
- [var gamepad: GCGamepad?](gccontroller/gamepad.md)
  The gamepad profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/motion)*