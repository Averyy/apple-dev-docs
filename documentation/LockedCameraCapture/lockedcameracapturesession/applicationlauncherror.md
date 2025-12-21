# LockedCameraCaptureSession.ApplicationLaunchError

**Framework**: LockedCameraCapture  
**Kind**: enum

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
- [LockedCameraCaptureSession.ApplicationLaunchError.applicationNotFound](lockedcameracapturesession/applicationlauncherror/applicationnotfound.md)
  An error that the launch failed because the system didn’t find the application.
- [LockedCameraCaptureSession.ApplicationLaunchError.authenticationFailed](lockedcameracapturesession/applicationlauncherror/authenticationfailed.md)
  An error that the launch failed because authentication failed and the device is locked.
- [LockedCameraCaptureSession.ApplicationLaunchError.unknown](lockedcameracapturesession/applicationlauncherror/unknown.md)
  An error that the launch failed with an unknown error.
### Instance Properties
- [var errorCode: Int](lockedcameracapturesession/applicationlauncherror/errorcode.md)
  An integer value that represents the error code.
- [var failureReason: String?](lockedcameracapturesession/applicationlauncherror/failurereason.md)
  A string that describes the error that occurred.
### Type Properties
- [static var errorDomain: String](lockedcameracapturesession/applicationlauncherror/errordomain.md)
  The domain for errors that can occur when launching the extension’s containing app.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession/applicationlauncherror)*