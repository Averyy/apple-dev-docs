# RoomCaptureSession.CaptureError.internalError

**Framework**: RoomPlan  
**Kind**: case  
**Role**: Case

An error that indicates when the framework encounters an unexpected error case.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
case internalError
```

## See Also

### Identifying the error cause
- [RoomCaptureSession.CaptureError.deviceNotSupported](./devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [RoomCaptureSession.CaptureError.deviceTooHot](./devicetoohot.md)
  An error that indicates when the device thermal metrics surpass the framework’s limitations.
- [RoomCaptureSession.CaptureError.exceedSceneSizeLimit](./exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomCaptureSession.CaptureError.invalidARConfiguration](./invalidarconfiguration.md)
  An error that indicates when the ARKit session runs an unsupported configuration.
- [RoomCaptureSession.CaptureError.worldTrackingFailure](./worldtrackingfailure.md)
  An error that indicates an issue with the underlying ARKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/captureerror/internalerror)*