# GCMouseInput

**Framework**: Game Controller  
**Kind**: class

A controller profile that tracks input from a mouse.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCMouseInput
```

#### Overview

This profile supports a mouse with the following features:

- A two-axis cursor and scroll
- A left button
- An optional right button
- An optional middle button
- An optional set of auxiliarly buttons

This profile provides only raw mouse movement delta values. For the cursor position at a specific time, use the [`UIHoverGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UIHoverGestureRecognizer) class and the `NSEvent` [`mouseLocation`](https://developer.apple.com/documentation/AppKit/NSEvent/mouseLocation) method.

## Topics

### Getting Change Information
- [var mouseMovedHandler: GCMouseMoved?](gcmouseinput/mousemovedhandler.md)
  The block that the profile calls when the mouse moves.
- [typealias GCMouseMoved](gcmousemoved.md)
  The signature for the block that the mouse input profile calls when the mouse moves.
### Accessing Buttons
- [var leftButton: GCControllerButtonInput](gcmouseinput/leftbutton.md)
  The left button on the mouse.
- [var rightButton: GCControllerButtonInput?](gcmouseinput/rightbutton.md)
  The optional right button on the mouse.
- [var middleButton: GCControllerButtonInput?](gcmouseinput/middlebutton.md)
  The optional middle button on the mouse.
- [var auxiliaryButtons: [GCControllerButtonInput]?](gcmouseinput/auxiliarybuttons.md)
  The optional additional buttons on the mouse.
### Scrolling
- [var scroll: GCDeviceCursor](gcmouseinput/scroll.md)
  The location of the directional pad cursor with an undefined range.

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
- [class GCKeyboardInput](gckeyboardinput.md)
  A controller profile that uses the keyboard as the input device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouseinput)*