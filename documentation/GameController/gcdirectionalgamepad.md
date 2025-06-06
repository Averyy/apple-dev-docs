# GCDirectionalGamepad

**Framework**: Game Controller  
**Kind**: class

A profile that supports only the directional pad, without motion or rotation.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- tvOS 14.3+
- visionOS 1.0+

## Declaration

```swift
class GCDirectionalGamepad
```

#### Overview

The directional gamepad profile is similar to a micro gamepad profile except it doesn’t support motion or rotation. The controller’s [`motion`](gccontroller/motion.md) property is `nil` and the inherited [`allowsRotation`](gcmicrogamepad/allowsrotation.md) property is [`false`](https://developer.apple.com/documentation/swift/false).

If you select Micro Gamepad when you add the Game Controllers capability ([`GCSupportedGameControllers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers) ) to your project, and you also support the GCDirectionalGamepad profile, select Directional Gamepad as well.

If you support the second-generation Siri Remote and later, set the [`GCSupportsMultipleMicroGamepads`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsMultipleMicroGamepads) key to `YES` in the information property list in your project.

In addition, the directional pad element may report digital or analog values. If the directional pad’s [`isAnalog`](gccontrollerelement/isanalog.md) property is [`false`](https://developer.apple.com/documentation/swift/false), it reports absolute directional pad values (the [`reportsAbsoluteDpadValues`](gcmicrogamepad/reportsabsolutedpadvalues.md) property is [`true`](https://developer.apple.com/documentation/swift/true)).

## Topics

### Accessing Elements by Name
- [Directional Gamepad Input Names](directional-gamepad-input-names.md)
  Constants for names of directional pad elements.

## Relationships

### Inherits From
- [GCMicroGamepad](gcmicrogamepad.md)
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
- [class GCDualSenseGamepad](gcdualsensegamepad.md)
  A controller profile that supported the DualSense controller.
- [var microGamepad: GCMicroGamepad?](gccontroller/microgamepad.md)
  The micro gamepad profile.
- [class GCMicroGamepad](gcmicrogamepad.md)
  A controller profile that supports the Siri Remote.
- [var motion: GCMotion?](gccontroller/motion.md)
  The motion input profile.
- [var physicalInputProfile: GCPhysicalInputProfile](gccontroller/physicalinputprofile.md)
  The physical input profile for the controller.
- [var gamepad: GCGamepad?](gccontroller/gamepad.md)
  The gamepad profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdirectionalgamepad)*