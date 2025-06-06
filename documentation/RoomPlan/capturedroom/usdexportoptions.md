# CapturedRoom.USDExportOptions

**Framework**: RoomPlan  
**Kind**: struct

Options that determine the underlying data format of a scan export.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct USDExportOptions
```

#### Overview

The `exportOptions` parameter of the captured room ([`CapturedRoom`](capturedroom.md)) and captured structure ([`CapturedStructure`](capturedstructure.md)) functions `export(to:metadataURL:modelProvider:exportOptions:)` are of this type.

The following table lists the features that each export option supports in the output result.

| Feature per export option | Parametric | Mesh | Model |
| --- | --- | --- | --- |
| Changing the size or position of objects, windows, or doors | ✔ |  |  |
| Boolean operations | ✔ |  |  |
| Section positions and labels | ✔ | ✔ | ✔ |
| Polygonal walls |  | ✔ | ✔ |
| Windows, doors, and other openings cut out of wall geometry |  | ✔ | ✔ |
| The recessed areas of a sink or fireplace |  | ✔ | ✔ |
| ModelProvider models |  |  | ✔ |

## Topics

### Choosing an export option
- [static let parametric: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/parametric.md)
  An export option that formats the output file as a collection of size-dependent primitives.
- [static let mesh: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/mesh.md)
  An export option that formats the output file as a collection of size-independant triangles that connect to form a mesh.
- [static let model: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/model.md)
  An export option that formats the output file as a collection of 3D models.
### Creating an export option
- [init(rawValue: Int32)](capturedroom/usdexportoptions/init(rawvalue:).md)
  Creates an export option with the specified raw value.
- [let rawValue: Int32](capturedroom/usdexportoptions/rawvalue-swift.property.md)
  A raw value for the export option.
### Type Aliases
- [CapturedRoom.USDExportOptions.ArrayLiteralElement](capturedroom/usdexportoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [CapturedRoom.USDExportOptions.Element](capturedroom/usdexportoptions/element.md)
  The element type of the option set.
- [CapturedRoom.USDExportOptions.RawValue](capturedroom/usdexportoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](capturedroom/usdexportoptions/equatable-implementations.md)
- [OptionSet Implementations](capturedroom/usdexportoptions/optionset-implementations.md)
- [SetAlgebra Implementations](capturedroom/usdexportoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Providing custom models for captured rooms and structure exports](providing-custom-models-for-captured-rooms-and-structure-exports.md)
  Enhance the look of an exported 3D model by substituting object bounding boxes with detailed 3D renditions.
- [class RoomBuilder](roombuilder.md)
  An object that generates a 3D asset from room-capture data.
- [class StructureBuilder](structurebuilder.md)
  An object that combines multiple scan sessions into a single captured result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/usdexportoptions)*