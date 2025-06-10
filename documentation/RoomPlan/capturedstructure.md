# CapturedStructure

**Framework**: RoomPlan  
**Kind**: struct

An object that holds the results of the merger of multiple capture sessions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct CapturedStructure
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

This structure combines the data from multiple [`CapturedRoom`](capturedroom.md) instances that a user scans in the same physical vicinity. The [`StructureBuilder`](structurebuilder.md) class’s function merges the captured rooms with the [`capturedStructure(from:)`](structurebuilder/capturedstructure(from:).md) function, which returns an object of this type.

## Topics

### Creating a captured room
- [init(from: any Decoder) throws](capturedstructure/init(from:).md)
  Creates a captured structure by deserializing the decoder of a prior captured structure.
### Inspecting structure details
- [var identifier: UUID](capturedstructure/identifier.md)
  A unique alphanumeric value that the framework assigns the structure.
- [var rooms: [CapturedRoom]](capturedstructure/rooms.md)
  An array of all the captured rooms in the structure.
- [var floors: [CapturedStructure.Surface]](capturedstructure/floors.md)
  An array of all the floors in the structure.
- [CapturedStructure.Surface](capturedstructure/surface.md)
  The type a captured structure assigns to surfaces.
- [var doors: [CapturedStructure.Surface]](capturedstructure/doors.md)
  An array of all the doors in the structure.
- [var objects: [CapturedStructure.Object]](capturedstructure/objects.md)
  An array of all the objects in the structure.
- [CapturedStructure.Object](capturedstructure/object.md)
  The type a captured structure assigns to objects.
- [var openings: [CapturedStructure.Surface]](capturedstructure/openings.md)
  An array of all the openings in the structure.
- [var walls: [CapturedStructure.Surface]](capturedstructure/walls.md)
  An array of all the walls in the structure.
- [var windows: [CapturedStructure.Surface]](capturedstructure/windows.md)
  An array of all the windows in the structure.
- [var sections: [CapturedStructure.Section]](capturedstructure/sections.md)
  One or more room types that the framework identifies in the structure.
- [CapturedStructure.Section](capturedstructure/section.md)
  The type a captured structure assigns to distinct room areas.
- [var version: Int](capturedstructure/version.md)
  A version number for the captured structure.
### Serializing a captured structure
- [func encode(to: any Encoder) throws](capturedstructure/encode(to:).md)
  Serializes a captured structure to the specified encoder.
### Generating a USDZ file
- [func export(to: URL, metadataURL: URL?, modelProvider: CapturedStructure.ModelProvider?, exportOptions: CapturedStructure.USDExportOptions) throws](capturedstructure/export(to:metadataurl:modelprovider:exportoptions:).md)
  Produces a 3D asset from the captured structure.
- [CapturedStructure.USDExportOptions](capturedstructure/usdexportoptions.md)
  The type a captured structure uses to configure exports.
- [CapturedStructure.ModelProvider](capturedstructure/modelprovider.md)
  The type a captured structure uses to output sophisticated 3D models.
### Handling errors
- [CapturedStructure.Error](capturedstructure/error.md)
  Errors that can occur during a captured structure export.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Merging multiple scans into a single structure](merging-multiple-scans-into-a-single-structure.md)
  Export a 3D model that consists of multiple rooms captured in the same physical vicinity.
- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)
  Create an AR experience that enables people to scan a building that contains multiple rooms.
- [struct CapturedRoom](capturedroom.md)
  A structure that provides the key details of a scanned room.
- [struct CapturedRoomData](capturedroomdata.md)
  An opaque object that holds the raw results of a scan.
- [Captured Object Attributes](captured-object-attributes.md)
  Determine details about the objects and surfaces that the framework identifies in a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedstructure)*