# ObjectCaptureSession.Error

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

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
- [ObjectCaptureSession.Error.cancelled](./error/cancelled.md)
  The user requested that the session be canceled and the session is now canceled.  Another session may now be created.
- [ObjectCaptureSession.Error.directoryNotEmpty(_:)](./error/directorynotempty%28_%29.md)
  We cannot continue a pre-existing capture, so if an output directory is provided that already exists and it is not empty, this error is thrown.
- [ObjectCaptureSession.Error.insufficientStorage(requiredBytes:)](./error/insufficientstorage%28requiredbytes%29.md)
  The session can’t be started since there is not enough storage space in the provided directories.
- [ObjectCaptureSession.Error.sensorFailed](./error/sensorfailed.md)
  There was an ARKit failure in one of the sensors.
- [ObjectCaptureSession.Error.trackingFailed](./error/trackingfailed.md)
  There was an unrecoverable error related to tracking the object or environment.
### Instance Properties
- [var localizedDescription: String](./error/localizeddescription.md)
  Retrieve the localized description for this error.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring the session
- [ObjectCaptureSession.CaptureState](./capturestate.md)
  State of the capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/error)*