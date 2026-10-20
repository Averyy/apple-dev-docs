# RoomCaptureSession.CaptureError

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur during a room-capture session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum CaptureError
```

#### Overview

The `error` argument of a room-capture session delgate’s  [`captureSession(_:didEndWith:error:)`](../roomcapturesessiondelegate/capturesession%28_,didendwith,error%29.md) function is of this type.

## Topics

### Identifying the error cause
- [RoomCaptureSession.CaptureError.deviceNotSupported](./captureerror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [RoomCaptureSession.CaptureError.deviceTooHot](./captureerror/devicetoohot.md)
  An error that indicates when the device thermal metrics surpass the framework’s limitations.
- [RoomCaptureSession.CaptureError.exceedSceneSizeLimit](./captureerror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomCaptureSession.CaptureError.invalidARConfiguration](./captureerror/invalidarconfiguration.md)
  An error that indicates when the ARKit session runs an unsupported configuration.
- [RoomCaptureSession.CaptureError.worldTrackingFailure](./captureerror/worldtrackingfailure.md)
  An error that indicates an issue with the underlying ARKit session.
- [RoomCaptureSession.CaptureError.internalError](./captureerror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
### Inspecting error information
- [var errorDescription: String?](./captureerror/errordescription.md)
  A human-readable explanation for the error.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to events
- [var delegate: (any RoomCaptureSessionDelegate)?](./delegate.md)
  An object that observes important events in the room-scanning process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/captureerror)*