# RoomBuilder

**Framework**: RoomPlan  
**Kind**: class

An object that generates a 3D asset from room-capture data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
class RoomBuilder
```

#### Overview

This class processes data from an earlier scan to generate a detailed [`CapturedRoom`](capturedroom.md) object.

Your app receives raw captured room data ([`CapturedRoomData`](capturedroomdata.md)) through:

- The view delegate ([`RoomCaptureViewDelegate`](roomcaptureviewdelegate.md)) callback [`captureView(shouldPresent:error:)`](roomcaptureviewdelegate/captureview(shouldpresent:error:).md) for an app that provides room-scanning features through the framework-provided view ([`RoomCaptureView`](roomcaptureview.md)).
- The scan session ([`RoomCaptureSession`](roomcapturesession.md)) callback [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md) for an app that provides room-scanning features by displaying its own view.

Your app generates a detailed captured room object by calling [`capturedRoom(from:)`](roombuilder/capturedroom(from:).md) on the raw data. Your app can then inspect or modify this data before exporting the scanned room to a USDZ file.

## Topics

### Creating a room builder
- [init(options: RoomBuilder.ConfigurationOptions)](roombuilder/init(options:).md)
  Creates a room builder using the specified options.
- [RoomBuilder.ConfigurationOptions](roombuilder/configurationoptions.md)
  Options that configure a room builder.
### Processing a prior scan
- [func capturedRoom(from: CapturedRoomData) async throws -> CapturedRoom](roombuilder/capturedroom(from:).md)
  Processes the specified raw scan results and returns a detailed representation of the room.
### Handling errors
- [RoomBuilder.BuildError](roombuilder/builderror.md)
  Errors that can occur during captured room-data processing.

## See Also

- [Providing custom models for captured rooms and structure exports](providing-custom-models-for-captured-rooms-and-structure-exports.md)
  Enhance the look of an exported 3D model by substituting object bounding boxes with detailed 3D renditions.
- [class StructureBuilder](structurebuilder.md)
  An object that combines multiple scan sessions into a single captured result.
- [CapturedRoom.USDExportOptions](capturedroom/usdexportoptions.md)
  Options that determine the underlying data format of a scan export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder)*