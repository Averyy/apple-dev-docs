# LockedCameraCaptureSession.ApplicationLaunchError

**Framework**: LockedCameraCapture  
**Kind**: enum  
**Role**: Enumeration

Indicates why launching the extension’s containing app failed.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum ApplicationLaunchError
```

## Topics

### Enumeration Cases
- [LockedCameraCaptureSession.ApplicationLaunchError.applicationNotFound](./applicationlauncherror/applicationnotfound.md)
  An error that the launch failed because the system didn’t find the application.
- [LockedCameraCaptureSession.ApplicationLaunchError.authenticationFailed](./applicationlauncherror/authenticationfailed.md)
  An error that the launch failed because authentication failed and the device is locked.
- [LockedCameraCaptureSession.ApplicationLaunchError.unknown](./applicationlauncherror/unknown.md)
  An error that the launch failed with an unknown error.
### Instance Properties
- [var errorCode: Int](./applicationlauncherror/errorcode.md)
  An integer value that represents the error code.
- [var failureReason: String?](./applicationlauncherror/failurereason.md)
  A string that describes the error that occurred.
### Type Properties
- [static var errorDomain: String](./applicationlauncherror/errordomain.md)
  The domain for errors that can occur when launching the extension’s containing app.

## Relationships

### Conforms To
- [CustomNSError](../../Foundation/customnserror.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession/applicationlauncherror)*