# ObjectCaptureSession.Error

**Framework**: RealityKit  
**Kind**: enum

Errors associated with the top-level computation of this class.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [ObjectCaptureSession.Error.cancelled](objectcapturesession/error/cancelled.md)
  The user requested that the session be canceled and the session is now canceled.  Another session may now be created.
- [ObjectCaptureSession.Error.directoryNotEmpty(_:)](objectcapturesession/error/directorynotempty(_:).md)
  We cannot continue a pre-existing capture, so if an output directory is provided that already exists and it is not empty, this error is thrown.
- [ObjectCaptureSession.Error.insufficientStorage(requiredBytes:)](objectcapturesession/error/insufficientstorage(requiredbytes:).md)
  The session can’t be started since there is not enough storage space in the provided directories.
- [ObjectCaptureSession.Error.sensorFailed](objectcapturesession/error/sensorfailed.md)
  There was an ARKit failure in one of the sensors.
- [ObjectCaptureSession.Error.trackingFailed](objectcapturesession/error/trackingfailed.md)
  There was an unrecoverable error related to tracking the object or environment.
### Instance Properties
- [var localizedDescription: String](objectcapturesession/error/localizeddescription.md)
  Retrieve the localized description for this error.
### Default Implementations
- [LocalizedError Implementations](objectcapturesession/error/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ObjectCaptureSession.CaptureState](objectcapturesession/capturestate.md)
  State of the capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/error)*