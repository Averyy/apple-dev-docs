# GCPhysicalInputProfile

**Framework**: Game Controller  
**Kind**: class

The base class for controller profiles that support physical buttons, thumbsticks, and directional pads.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCPhysicalInputProfile
```

#### Overview

This class provides properties and methods for accessing common elements of controllers, and for creating snapshots of profiles.

## Topics

### Getting the device
- [var device: (any GCDevice)?](gcphysicalinputprofile/device.md)
  The physical device that the profile represents.
### Getting change information
- [var lastEventTimestamp: TimeInterval](gcphysicalinputprofile/lasteventtimestamp.md)
  The time of the most recent change to an element’s value.
- [var valueDidChangeHandler: ((GCPhysicalInputProfile, GCControllerElement) -> Void)?](gcphysicalinputprofile/valuedidchangehandler.md)
  The block that the profile calls when an element’s value changes.
### Accessing elements by name or key
- [var elements: [String : GCControllerElement]](gcphysicalinputprofile/elements.md)
  The elements in the profile as key-value pairs for lookup by name.
- [var buttons: [String : GCControllerButtonInput]](gcphysicalinputprofile/buttons.md)
  The buttons in the profile as key-value pairs for lookup by name.
- [var axes: [String : GCControllerAxisInput]](gcphysicalinputprofile/axes.md)
  The axes in the profile as key-value pairs for lookup by name.
- [var dpads: [String : GCControllerDirectionPad]](gcphysicalinputprofile/dpads.md)
  The directional pads in the profile as key-value pairs for lookup by name.
- [var touchpads: [String : GCControllerTouchpad]](gcphysicalinputprofile/touchpads.md)
  The touchpads in the profile as key-value pairs for lookup by name.
- [subscript(String) -> GCControllerElement?](gcphysicalinputprofile/subscript(_:).md)
  Returns the element that the key specifies.
### Getting elements by type
- [var allElements: Set<GCControllerElement>](gcphysicalinputprofile/allelements.md)
  The elements in the profile.
- [var allButtons: Set<GCControllerButtonInput>](gcphysicalinputprofile/allbuttons.md)
  The buttons in the profile.
- [var allAxes: Set<GCControllerAxisInput>](gcphysicalinputprofile/allaxes.md)
  The axes in the profile.
- [var allDpads: Set<GCControllerDirectionPad>](gcphysicalinputprofile/alldpads.md)
  The directional pads in the profile.
- [var allTouchpads: Set<GCControllerTouchpad>](gcphysicalinputprofile/alltouchpads.md)
  The touchpads in the profile.
### Setting snapshot values
- [func capture() -> Self](gcphysicalinputprofile/capture.md)
  Returns a snapshot of the profile with its current element values.
- [func setStateFromPhysicalInput(GCPhysicalInputProfile)](gcphysicalinputprofile/setstatefromphysicalinput(_:).md)
  Copies the input values from a specified physical input profile to a snapshot of the profile.
### Remapping input elements
- [var hasRemappedElements: Bool](gcphysicalinputprofile/hasremappedelements.md)
  A Boolean value that indicates whether the user remaps elements in this profile.
- [func mappedElementAlias(forPhysicalInputName: String) -> String](gcphysicalinputprofile/mappedelementalias(forphysicalinputname:).md)
  Returns the name of the input element to which the user remaps the given physical element.
- [func mappedPhysicalInputNames(forElementAlias: String) -> Set<String>](gcphysicalinputprofile/mappedphysicalinputnames(forelementalias:).md)
  Returns the physical input elements to which the user remaps the given input element.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerUserCustomizationsDidChange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GCExtendedGamepad](gcextendedgamepad.md)
- [GCGamepad](gcgamepad.md)
- [GCKeyboardInput](gckeyboardinput.md)
- [GCMicroGamepad](gcmicrogamepad.md)
- [GCMouseInput](gcmouseinput.md)
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
- [var motion: GCMotion?](gccontroller/motion.md)
  The motion input profile.
- [var physicalInputProfile: GCPhysicalInputProfile](gccontroller/physicalinputprofile.md)
  The physical input profile for the controller.
- [var gamepad: GCGamepad?](gccontroller/gamepad.md)
  The gamepad profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile)*