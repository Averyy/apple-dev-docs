# GCExtendedGamepad

**Framework**: Game Controller  
**Kind**: class

A controller profile that supports the extended set of gamepad controls.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCExtendedGamepad
```

#### Overview

The extended gamepad controller profile represents a physical or virtual controller with the following input elements:

- Two shoulder buttons
- Two trigger buttons
- Four face buttons in a diamond pattern
- One directional pad
- Two thumbsticks with optional thumbstick buttons
- Optional Home and Options buttons
- A Menu button

![An illustration of an extended gamepad controller with callouts for the buttons and controls.](https://docs-assets.developer.apple.com/published/74601dd72896727165a38539cc713b0a/media-3850406%402x.png)

If a [`GCController`](gccontroller.md) object supports this type of profile, get the input values of the elements from the controller’s [`extendedGamepad`](gccontroller/extendedgamepad.md) property or use the profile’s [`valueChangedHandler`](gcextendedgamepad/valuechangedhandler.md) method to receive a callback when the input values change. Alternatively, use the [`saveSnapshot()`](gcextendedgamepad/savesnapshot().md) method to capture the input values at a moment in time.

If the controller’s [`extendedGamepad`](gccontroller/extendedgamepad.md) property is `nil`, the controller doesn’t support this type of profile. See [`GCController`](gccontroller.md) for other profiles you can use.

## Topics

### Getting the controller
- [var controller: GCController?](gcextendedgamepad/controller.md)
  The controller for the profile.
### Getting change information
- [var valueChangedHandler: GCExtendedGamepadValueChangedHandler?](gcextendedgamepad/valuechangedhandler.md)
  The block that the profile calls when an element’s value changes.
- [typealias GCExtendedGamepadValueChangedHandler](gcextendedgamepadvaluechangedhandler.md)
  The signature for the block that the profile calls when an element’s value changes.
### Getting shoulder button inputs
- [var leftShoulder: GCControllerButtonInput](gcextendedgamepad/leftshoulder.md)
  The controller’s left shoulder button element.
- [var rightShoulder: GCControllerButtonInput](gcextendedgamepad/rightshoulder.md)
  The controller’s right shoulder button element.
### Getting trigger inputs
- [var leftTrigger: GCControllerButtonInput](gcextendedgamepad/lefttrigger.md)
  The controller’s left trigger element.
- [var rightTrigger: GCControllerButtonInput](gcextendedgamepad/righttrigger.md)
  The controller’s right trigger element.
### Getting face button inputs
- [var buttonMenu: GCControllerButtonInput](gcextendedgamepad/buttonmenu.md)
  The primary menu button element that players use to enter the main menu and pause the game.
- [var buttonOptions: GCControllerButtonInput?](gcextendedgamepad/buttonoptions.md)
  The controller’s secondary menu button element.
- [var buttonHome: GCControllerButtonInput?](gcextendedgamepad/buttonhome.md)
  The main menu button element that players use to enter the secondary menu and pause the game.
- [var buttonA: GCControllerButtonInput](gcextendedgamepad/buttona.md)
  The bottom face button that uses  or another indicator as its label.
- [var buttonB: GCControllerButtonInput](gcextendedgamepad/buttonb.md)
  The right face button that uses  or another indicator as its label.
- [var buttonX: GCControllerButtonInput](gcextendedgamepad/buttonx.md)
  The left face button that uses  or another indicator as its label.
- [var buttonY: GCControllerButtonInput](gcextendedgamepad/buttony.md)
  The top face button that uses  or another indicator as its label.
### Getting directional pad inputs
- [var dpad: GCControllerDirectionPad](gcextendedgamepad/dpad.md)
  The controller’s directional pad element.
### Getting thumbstick and thumbstick button inputs
- [var leftThumbstick: GCControllerDirectionPad](gcextendedgamepad/leftthumbstick.md)
  The controller’s left thumbstick element.
- [var rightThumbstick: GCControllerDirectionPad](gcextendedgamepad/rightthumbstick.md)
  The controller’s right thumbstick element.
- [var leftThumbstickButton: GCControllerButtonInput?](gcextendedgamepad/leftthumbstickbutton.md)
  The button on the left thumbstick of the controller.
- [var rightThumbstickButton: GCControllerButtonInput?](gcextendedgamepad/rightthumbstickbutton.md)
  The button on the right thumbstick of the controller.
### Accessing elements by name
- [Extended gamepad input names](extended-gamepad-input-names.md)
  Constants for names of extended gamepad elements.
### Setting snapshot values
- [func setStateFrom(GCExtendedGamepad)](gcextendedgamepad/setstatefrom(_:).md)
  Copies the input values from a specified extended gamepad to a snapshot of an extended gamepad.
- [func saveSnapshot() -> GCExtendedGamepadSnapshot](gcextendedgamepad/savesnapshot.md)
  Saves a snapshot of all of the profile’s elements.

## Relationships

### Inherits From
- [GCPhysicalInputProfile](gcphysicalinputprofile.md)
### Inherited By
- [GCDualSenseGamepad](gcdualsensegamepad.md)
- [GCDualShockGamepad](gcdualshockgamepad.md)
- [GCExtendedGamepadSnapshot](gcextendedgamepadsnapshot.md)
- [GCXboxGamepad](gcxboxgamepad.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad)*