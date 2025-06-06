# CapturedRoom

**Framework**: RoomPlan  
**Kind**: struct

A structure that provides the key details of a scanned room.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct CapturedRoom
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

This structure represents the post-processed result of the room-scanning process.

Your app receives an instance of this structure through:

- The view delegate ([`RoomCaptureViewDelegate`](roomcaptureviewdelegate.md)) callback [`captureView(didPresent:error:)`](roomcaptureviewdelegate/captureview(didpresent:error:).md) for an app that scans rooms using the framework-provided view ([`RoomCaptureView`](roomcaptureview.md)).
- A room builder object ([`RoomBuilder`](roombuilder.md)) by calling [`capturedRoom(from:)`](roombuilder/capturedroom(from:).md) for an app that provides its own room-scanning view, or processes the saved results of a prior scan.

With the room details, an app can provide custom features, such as rendering the room and enabling the user to modify the position of its objects. You can export the current state of the room at any time to a USDZ file by calling [`export(to:metadataURL:modelProvider:exportOptions:)`](capturedroom/export(to:metadataurl:modelprovider:exportoptions:).md).

## Topics

### Creating a captured room
- [init(from: any Decoder) throws](capturedroom/init(from:).md)
  Creates a captured room by deserializing the decoder of a previously captured room.
### Inspecting room details
- [var identifier: UUID](capturedroom/identifier.md)
  A unique alphanumeric value that the framework assigns the room.
- [var story: Int](capturedroom/story.md)
  The story, floor number, or level on which the captured room resides within a larger structure.
- [var floors: [CapturedRoom.Surface]](capturedroom/floors.md)
  An array of floors that the framework identifies during a scan.
- [CapturedRoom.Surface](capturedroom/surface.md)
  A 2D area in a room that the framework identifies as a surface.
- [var doors: [CapturedRoom.Surface]](capturedroom/doors.md)
  An array of doors that the framework identifies during a scan.
- [var objects: [CapturedRoom.Object]](capturedroom/objects.md)
  An array of objects that the framework identifies during a scan.
- [CapturedRoom.Object](capturedroom/object.md)
  A 3D area in a room that the framework identifies as an object.
- [var openings: [CapturedRoom.Surface]](capturedroom/openings.md)
  An array of openings that the framework identifies during a scan.
- [var walls: [CapturedRoom.Surface]](capturedroom/walls.md)
  An array of walls that the framework identifies during a scan.
- [var windows: [CapturedRoom.Surface]](capturedroom/windows.md)
  An array of windows that the framework identifies during a scan.
- [var sections: [CapturedRoom.Section]](capturedroom/sections.md)
  One or more room types that the framework observes in the room.
- [CapturedRoom.Section](capturedroom/section.md)
  An object that identifies a particular area in a captured room in relation to common types of room areas in a building.
- [CapturedRoom.Confidence](capturedroom/confidence.md)
  Levels of certainty in the classification of a particular detail in a scan.
- [var version: Int](capturedroom/version.md)
  A version number for the captured room.
### Serializing a captured room
- [func encode(to: any Encoder) throws](capturedroom/encode(to:).md)
  Serializes a captured room to the specified encoder.
- [CapturedRoom.AttributesCodableRepresentation](capturedroom/attributescodablerepresentation.md)
  A serializable set of details that describe an object in the room.
### Generating a USDZ file
- [func export(to: URL, exportOptions: CapturedRoom.USDExportOptions) throws](capturedroom/export(to:exportoptions:).md)
  Produces a 3D asset from the captured room.
- [func export(to: URL, metadataURL: URL?, modelProvider: CapturedRoom.ModelProvider?, exportOptions: CapturedRoom.USDExportOptions) throws](capturedroom/export(to:metadataurl:modelprovider:exportoptions:).md)
  Produces a 3D asset from the captured room with the given metadata output URL and model provider.
- [CapturedRoom.USDExportOptions](capturedroom/usdexportoptions.md)
  Options that determine the underlying data format of a scan export.
- [CapturedRoom.ModelProvider](capturedroom/modelprovider.md)
  A structure that assigns detailed 3D models to captured objects for an export.
### Handling errors
- [CapturedRoom.Error](capturedroom/error.md)
  Errors that can occur during a captured room export.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Merging multiple scans into a single structure](merging-multiple-scans-into-a-single-structure.md)
  Export a 3D model that consists of multiple rooms captured in the same physical vicinity.
- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)
  Create an AR experience that enables people to scan a building that contains multiple rooms.
- [struct CapturedStructure](capturedstructure.md)
  An object that holds the results of the merger of multiple capture sessions.
- [struct CapturedRoomData](capturedroomdata.md)
  An opaque object that holds the raw results of a scan.
- [Captured Object Attributes](captured-object-attributes.md)
  Determine details about the objects and surfaces that the framework identifies in a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom)*