# GCPhysicalInputElementTypedName

**Framework**: Game Controller  
**Kind**: protocol

A type-safe name for accessing elements of a physical input element collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
protocol GCPhysicalInputElementTypedName : Hashable, RawRepresentable, Sendable where Self.RawValue == String
```

## Topics

### Associated type
- [associatedtype PhysicalInputElement : GCPhysicalInputElement](gcphysicalinputelementtypedname/physicalinputelement.md)
  A placeholder for the type that adopts this protocol.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [GCAxisElementName](gcaxiselementname-swift.struct.md)
- [GCButtonElementName](gcbuttonelementname-swift.struct.md)
- [GCDirectionPadElementName](gcdirectionpadelementname-swift.struct.md)
- [GCPhysicalInputElementName](gcphysicalinputelementname-swift.struct.md)
- [GCSwitchElementName](gcswitchelementname-swift.struct.md)

## See Also

- [struct GCPhysicalInputElementName](gcphysicalinputelementname-swift.struct.md)
  The name of a physical input element.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelementtypedname)*