# CapturedRoom.USDExportOptions

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

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

The `exportOptions` parameter of the captured room ([`CapturedRoom`](../capturedroom.md)) and captured structure ([`CapturedStructure`](../capturedstructure.md)) functions `export(to:metadataURL:modelProvider:exportOptions:)` are of this type.

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
- [static let parametric: CapturedRoom.USDExportOptions](./usdexportoptions/parametric.md)
  An export option that formats the output file as a collection of size-dependent primitives.
- [static let mesh: CapturedRoom.USDExportOptions](./usdexportoptions/mesh.md)
  An export option that formats the output file as a collection of size-independant triangles that connect to form a mesh.
- [static let model: CapturedRoom.USDExportOptions](./usdexportoptions/model.md)
  An export option that formats the output file as a collection of 3D models.
### Creating an export option
- [init(rawValue: Int32)](./usdexportoptions/init%28rawvalue%29.md)
  Creates an export option with the specified raw value.
- [let rawValue: Int32](./usdexportoptions/rawvalue.md)
  A raw value for the export option.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### 3D Asset Output
- [Providing custom models for captured rooms and structure exports](../providing-custom-models-for-captured-rooms-and-structure-exports.md)
  Enhance the look of an exported 3D model by substituting object bounding boxes with detailed 3D renditions.
- [class RoomBuilder](../roombuilder.md)
  An object that generates a 3D asset from room-capture data.
- [class StructureBuilder](../structurebuilder.md)
  An object that combines multiple scan sessions into a single captured result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/usdexportoptions)*