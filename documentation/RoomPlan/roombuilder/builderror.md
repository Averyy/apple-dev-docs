# RoomBuilder.BuildError

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

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

The room builder ([`RoomBuilder`](../roombuilder.md)) function [`capturedRoom(from:)`](./capturedroom%28from%29.md) can throw an error of this type.

## Topics

### Interpreting the error cause
- [RoomBuilder.BuildError.insufficientInput](./builderror/insufficientinput.md)
  An error that indicates the framework expects more captured room data.
- [RoomBuilder.BuildError.invalidInput](./builderror/invalidinput.md)
  An error that indicates the framework encounters invalid captured room data.
- [RoomBuilder.BuildError.exceedSceneSizeLimit](./builderror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomBuilder.BuildError.internalError](./builderror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
- [RoomBuilder.BuildError.deviceNotSupported](./builderror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
### Inspecting error information
- [var errorDescription: String?](./builderror/errordescription.md)
  A human-readable explanation of the error.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/builderror)*