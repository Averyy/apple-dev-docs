# Input

**Framework**: Game Controller

Receive controller input in the way that best integrates with the flow of your game or game engine.

## Topics

### Essentials
- [Handling input events](handling-input-events.md)
  Receive controller input using either polling or callbacks.
- [protocol GCDevicePhysicalInput](gcdevicephysicalinput.md)
  The common properties and methods for objects that represent the input profile of a device.
- [protocol GCDevicePhysicalInputState](gcdevicephysicalinputstate.md)
  The common properties for physical devices with elements.
- [protocol GCDevicePhysicalInputStateDiff](gcdevicephysicalinputstatediff.md)
  The common functions for objects that contain the differences between a current and previous input state object.
### Elements
- [struct GCPhysicalInputElementCollection](gcphysicalinputelementcollection-swift.struct.md)
  A collection of physical input elements.
- [protocol GCPhysicalInputElement](gcphysicalinputelement.md)
  The common properties of physical input elements.
- [protocol GCButtonElement](gcbuttonelement.md)
  The common properties of an element that represents a momentary switch, such as a push button.
- [protocol GCAxisElement](gcaxiselement.md)
  The common properties for an element that represents an absolute or relative input value along an axis.
- [protocol GCSwitchElement](gcswitchelement.md)
  The common properties for an element that represents a switch.
- [protocol GCDirectionPadElement](gcdirectionpadelement.md)
  The common properties of elements that represent directional pads.
### Element inputs
- [protocol GCPhysicalInputSource](gcphysicalinputsource.md)
  A protocol for a description of an element without any system-level remapping of the controls.
### Element names
- [struct GCPhysicalInputElementName](gcphysicalinputelementname-swift.struct.md)
  The name of a physical input element.
- [protocol GCPhysicalInputElementTypedName](gcphysicalinputelementtypedname.md)
  A type-safe name for accessing elements of a physical input element collection.
- [struct GCButtonElementName](gcbuttonelementname-swift.struct.md)
  The names of the button elements.
- [struct GCAxisElementName](gcaxiselementname-swift.struct.md)
  The names for the elements that provide values along an axis.
- [struct GCSwitchElementName](gcswitchelementname-swift.struct.md)
  The name for an element that represents a switch.
- [struct GCDirectionPadElementName](gcdirectionpadelementname-swift.struct.md)
  The names for directional pad elements.
- [Extended gamepad input names](extended-gamepad-input-names.md)
  Constants for names of extended gamepad elements.
- [DualShock controller input names](dualshock-controller-input-names.md)
  Constants for names of DualShock 4 elements.
- [Xbox controller input names](xbox-controller-input-names.md)
  Constants for names of Xbox elements.
- [Micro gamepad input names](micro-gamepad-input-names.md)
  Constants for names of micro gamepad elements.
- [Directional Gamepad Input Names](directional-gamepad-input-names.md)
  Constants for names of directional pad elements.

## See Also

- [class GCMotion](gcmotion.md)
  A controller profile that supports orientation and motion.
- [class GCDeviceBattery](gcdevicebattery.md)
  The charge level and state of a device’s battery.
- [class GCDeviceHaptics](gcdevicehaptics.md)
  The locations of haptic actuators on a game controller.
- [class GCDeviceLight](gcdevicelight.md)
  The colored light on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/input)*