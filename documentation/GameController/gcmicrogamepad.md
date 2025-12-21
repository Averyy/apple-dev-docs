# GCMicroGamepad

**Framework**: Game Controller  
**Kind**: class

A controller profile that supports the Siri Remote.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCMicroGamepad
```

#### Overview

The micro gamepad controller profile supports the following input elements:

- Two digital face buttons (A and X).
- One analog directional pad (D-pad) that functions as a touchpad.

Users can rotate game controllers that support the micro gamepad profile, switching them between landscape and portrait orientation. If you want to get directional values according to the orientation, set the [`allowsRotation`](gcmicrogamepad/allowsrotation.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

![An illustration of a Siri Remote with callouts for the digital face buttons, the Button menu, and the analog directional pad.](https://docs-assets.developer.apple.com/published/484a6ffc804aba9b7e2d68ed5f16ad37/media-3830807%402x.png)

## Topics

### Getting the controller
- [var controller: GCController?](gcmicrogamepad/controller.md)
  The controller associated with this profile.
### Receiving a callback when input values change
- [var valueChangedHandler: GCMicroGamepadValueChangedHandler?](gcmicrogamepad/valuechangedhandler.md)
  The block that this profile calls when an element’s value changes.
- [typealias GCMicroGamepadValueChangedHandler](gcmicrogamepadvaluechangedhandler.md)
  Signature for the block that this profile calls when an element’s value changes.
### Getting face button inputs
- [var buttonMenu: GCControllerButtonInput](gcmicrogamepad/buttonmenu.md)
  The menu face button that players use to enter the main menu and pause the game.
- [var buttonA: GCControllerButtonInput](gcmicrogamepad/buttona.md)
  The button that the user activates by pressing harder on the touchpad.
- [var buttonX: GCControllerButtonInput](gcmicrogamepad/buttonx.md)
  The second face button element.
### Getting directional pad inputs
- [var dpad: GCControllerDirectionPad](gcmicrogamepad/dpad.md)
  The controller’s directional pad element.
- [var reportsAbsoluteDpadValues: Bool](gcmicrogamepad/reportsabsolutedpadvalues.md)
  A Boolean value that indicates whether the directional pad reports absolute or relative values.
- [var allowsRotation: Bool](gcmicrogamepad/allowsrotation.md)
  A Boolean value that indicates whether the profile reports the directional pad values relative to its current orientation.
### Accessing elements by name
- [Micro gamepad input names](micro-gamepad-input-names.md)
  Constants for names of micro gamepad elements.
### Setting snapshot avlues
- [func setStateFrom(GCMicroGamepad)](gcmicrogamepad/setstatefrom(_:).md)
  Copies the input values from a specified micro gamepad to a snapshot of a micro gamepad.
- [func saveSnapshot() -> GCMicroGamepadSnapshot](gcmicrogamepad/savesnapshot.md)
  Saves a snapshot of all of the profile’s elements.

## Relationships

### Inherits From
- [GCPhysicalInputProfile](gcphysicalinputprofile.md)
### Inherited By
- [GCDirectionalGamepad](gcdirectionalgamepad.md)
- [GCMicroGamepadSnapshot](gcmicrogamepadsnapshot.md)
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
- [class GCDirectionalGamepad](gcdirectionalgamepad.md)
  A profile that supports only the directional pad, without motion or rotation.
- [var motion: GCMotion?](gccontroller/motion.md)
  The motion input profile.
- [var physicalInputProfile: GCPhysicalInputProfile](gccontroller/physicalinputprofile.md)
  The physical input profile for the controller.
- [var gamepad: GCGamepad?](gccontroller/gamepad.md)
  The gamepad profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad)*