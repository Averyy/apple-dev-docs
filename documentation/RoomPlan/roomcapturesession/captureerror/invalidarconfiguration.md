# RoomCaptureSession.CaptureError.invalidARConfiguration

**Framework**: RoomPlan  
**Kind**: case

An error that indicates when the ARKit session runs an unsupported configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
case invalidARConfiguration
```

#### Discussion

The system throws this error if the app attempts to set a value for the room-capture session’s[`arSession`](roomcapturesession/arsession.md) object.

## See Also

- [RoomCaptureSession.CaptureError.deviceNotSupported](roomcapturesession/captureerror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [RoomCaptureSession.CaptureError.deviceTooHot](roomcapturesession/captureerror/devicetoohot.md)
  An error that indicates when the device thermal metrics surpass the framework’s limitations.
- [RoomCaptureSession.CaptureError.exceedSceneSizeLimit](roomcapturesession/captureerror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomCaptureSession.CaptureError.worldTrackingFailure](roomcapturesession/captureerror/worldtrackingfailure.md)
  An error that indicates an issue with the underlying ARKit session.
- [RoomCaptureSession.CaptureError.internalError](roomcapturesession/captureerror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/captureerror/invalidarconfiguration)*