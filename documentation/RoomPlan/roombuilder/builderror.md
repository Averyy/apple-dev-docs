# RoomBuilder.BuildError

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur during captured room-data processing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum BuildError
```

#### Overview

The room builder ([`RoomBuilder`](roombuilder.md)) function [`capturedRoom(from:)`](roombuilder/capturedroom(from:).md) can throw an error of this type.

## Topics

### Interpreting the error cause
- [RoomBuilder.BuildError.insufficientInput](roombuilder/builderror/insufficientinput.md)
  An error that indicates the framework expects more captured room data.
- [RoomBuilder.BuildError.invalidInput](roombuilder/builderror/invalidinput.md)
  An error that indicates the framework encounters invalid captured room data.
- [RoomBuilder.BuildError.exceedSceneSizeLimit](roombuilder/builderror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomBuilder.BuildError.internalError](roombuilder/builderror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
- [RoomBuilder.BuildError.deviceNotSupported](roombuilder/builderror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
### Inspecting error information
- [var errorDescription: String?](roombuilder/builderror/errordescription.md)
  A human-readable explanation of the error.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/builderror)*