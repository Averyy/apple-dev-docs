# GCButtonElementName

**Framework**: Game Controller  
**Kind**: struct

The names of the button elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
struct GCButtonElementName
```

## Topics

### Getting extended gamepad shoulder button names
- [static let leftShoulder: GCButtonElementName](gcbuttonelementname-swift.struct/leftshoulder.md)
  The name of the left shoulder button.
- [static let rightShoulder: GCButtonElementName](gcbuttonelementname-swift.struct/rightshoulder.md)
  The name of the right shoulder button.
- [static let leftBumper: GCButtonElementName](gcbuttonelementname-swift.struct/leftbumper.md)
  The name of the additional left shoulder button.
- [static let rightBumper: GCButtonElementName](gcbuttonelementname-swift.struct/rightbumper.md)
  The name of the additional right shoulder button.
### Getting extended gamepad trigger names
- [static let leftTrigger: GCButtonElementName](gcbuttonelementname-swift.struct/lefttrigger.md)
  The name of the left trigger.
- [static let rightTrigger: GCButtonElementName](gcbuttonelementname-swift.struct/righttrigger.md)
  The name of the right trigger.
### Getting extended gamepad face button names
- [static let menu: GCButtonElementName](gcbuttonelementname-swift.struct/menu.md)
  The name of the primary menu button element.
- [static let options: GCButtonElementName](gcbuttonelementname-swift.struct/options.md)
  The name of the main options button element.
- [static let home: GCButtonElementName](gcbuttonelementname-swift.struct/home.md)
  The name of the main menu button element.
- [static let a: GCButtonElementName](gcbuttonelementname-swift.struct/a.md)
  The name for the controller’s A button.
- [static let b: GCButtonElementName](gcbuttonelementname-swift.struct/b.md)
  The name for the controller’s B button.
- [static let x: GCButtonElementName](gcbuttonelementname-swift.struct/x.md)
  The name for the controller’s X button.
- [static let y: GCButtonElementName](gcbuttonelementname-swift.struct/y.md)
  The name for the controller’s Y button.
### Getting extended gamepad thumbstick names
- [static let leftThumbstickButton: GCButtonElementName](gcbuttonelementname-swift.struct/leftthumbstickbutton.md)
  The name of the left thumbstick element.
- [static let rightThumbstickButton: GCButtonElementName](gcbuttonelementname-swift.struct/rightthumbstickbutton.md)
  The name of the right thumbstick element.
### Getting extended gamepad back button names
- [static func backLeftButton(position: Int) -> GCButtonElementName](gcbuttonelementname-swift.struct/backleftbutton(position:).md)
  Returns the name of the back left button at the specified location.
- [static func backRightButton(position: Int) -> GCButtonElementName](gcbuttonelementname-swift.struct/backrightbutton(position:).md)
  Returns the name of the back right button at the specified location.
### Getting steering wheel controller names
- [static let pedalClutch: GCButtonElementName](gcbuttonelementname-swift.struct/pedalclutch.md)
  The name of the controller’s clutch.
- [static let pedalBrake: GCButtonElementName](gcbuttonelementname-swift.struct/pedalbrake.md)
  The name of the controller’s brake pedal.
- [static let pedalAccelerator: GCButtonElementName](gcbuttonelementname-swift.struct/pedalaccelerator.md)
  The name of the controller’s accelerator pedal.
- [static let leftPaddle: GCButtonElementName](gcbuttonelementname-swift.struct/leftpaddle.md)
  The name of the controller’s left paddle.
- [static let rightPaddle: GCButtonElementName](gcbuttonelementname-swift.struct/rightpaddle.md)
  The name of the controller’s right paddle.
### Getting Xbox button names
- [static let share: GCButtonElementName](gcbuttonelementname-swift.struct/share.md)
  The name of the Xbox share button.
### Getting arcade stick button names
- [static func arcadeButton(row: Int, column: Int) -> GCButtonElementName](gcbuttonelementname-swift.struct/arcadebutton(row:column:).md)
  Returns the name of the arcade stick button at the specified location.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [GCPhysicalInputElementTypedName](gcphysicalinputelementtypedname.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct GCPhysicalInputElementName](gcphysicalinputelementname-swift.struct.md)
  The name of a physical input element.
- [protocol GCPhysicalInputElementTypedName](gcphysicalinputelementtypedname.md)
  A type-safe name for accessing elements of a physical input element collection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelementname-swift.struct)*