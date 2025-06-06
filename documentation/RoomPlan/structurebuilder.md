# StructureBuilder

**Framework**: RoomPlan  
**Kind**: class

An object that combines multiple scan sessions into a single captured result.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 16.0+

## Declaration

```swift
class StructureBuilder
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

This class in conjunction with [`CapturedStructure`](capturedstructure.md) enables an app to export a 3D model that consists of multiple [`CapturedRoom`](capturedroom.md) instances. First, combine the rooms into a single captured result by calling [`capturedStructure(from:)`](structurebuilder/capturedstructure(from:).md). Then, generate a 3D model of the whole structure by calling [`export(to:metadataURL:modelProvider:exportOptions:)`](capturedstructure/export(to:metadataurl:modelprovider:exportoptions:).md).

## Topics

### Creating a structure builder
- [init(options: StructureBuilder.ConfigurationOptions)](structurebuilder/init(options:).md)
  Creates a structure builder using the specified options.
- [StructureBuilder.ConfigurationOptions](structurebuilder/configurationoptions.md)
  Options that configure a structure builder.
### Building a captured structure
- [func capturedStructure(from: [CapturedRoom]) async throws -> CapturedStructure](structurebuilder/capturedstructure(from:).md)
  Combines the argument captured rooms into a single unit.
### Interpreting build errors
- [StructureBuilder.BuildError](structurebuilder/builderror.md)
  Errors that can occur capturedStructure merging processing.

## See Also

- [Providing custom models for captured rooms and structure exports](providing-custom-models-for-captured-rooms-and-structure-exports.md)
  Enhance the look of an exported 3D model by substituting object bounding boxes with detailed 3D renditions.
- [class RoomBuilder](roombuilder.md)
  An object that generates a 3D asset from room-capture data.
- [CapturedRoom.USDExportOptions](capturedroom/usdexportoptions.md)
  Options that determine the underlying data format of a scan export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/structurebuilder)*