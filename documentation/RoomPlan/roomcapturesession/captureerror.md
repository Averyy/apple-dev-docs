# RoomCaptureSession.CaptureError

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur during a room-capture session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
enum CaptureError
```

#### Overview

The `error` argument of a room-capture session delgate’s  [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md) function is of this type.

## Topics

### Identifying the error cause
- [RoomCaptureSession.CaptureError.deviceNotSupported](roomcapturesession/captureerror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [RoomCaptureSession.CaptureError.deviceTooHot](roomcapturesession/captureerror/devicetoohot.md)
  An error that indicates when the device thermal metrics surpass the framework’s limitations.
- [RoomCaptureSession.CaptureError.exceedSceneSizeLimit](roomcapturesession/captureerror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomCaptureSession.CaptureError.invalidARConfiguration](roomcapturesession/captureerror/invalidarconfiguration.md)
  An error that indicates when the ARKit session runs an unsupported configuration.
- [RoomCaptureSession.CaptureError.worldTrackingFailure](roomcapturesession/captureerror/worldtrackingfailure.md)
  An error that indicates an issue with the underlying ARKit session.
- [RoomCaptureSession.CaptureError.internalError](roomcapturesession/captureerror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
### Inspecting error information
- [var errorDescription: String?](roomcapturesession/captureerror/errordescription.md)
  A human-readable explanation for the error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any RoomCaptureSessionDelegate)?](roomcapturesession/delegate.md)
  An object that observes important events in the room-scanning process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/captureerror)*