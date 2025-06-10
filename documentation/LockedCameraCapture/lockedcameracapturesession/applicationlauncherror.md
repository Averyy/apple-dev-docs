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

### Operators
- [static func == (LockedCameraCaptureSession.ApplicationLaunchError, LockedCameraCaptureSession.ApplicationLaunchError) -> Bool](lockedcameracapturesession/applicationlauncherror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
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
- [var hashValue: Int](lockedcameracapturesession/applicationlauncherror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](lockedcameracapturesession/applicationlauncherror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var errorDomain: String](lockedcameracapturesession/applicationlauncherror/errordomain.md)
  The domain for errors that can occur when launching the extension’s containing app.
### Default Implementations
- [CustomNSError Implementations](lockedcameracapturesession/applicationlauncherror/customnserror-implementations.md)
- [Equatable Implementations](lockedcameracapturesession/applicationlauncherror/equatable-implementations.md)
- [Error Implementations](lockedcameracapturesession/applicationlauncherror/error-implementations.md)
- [LocalizedError Implementations](lockedcameracapturesession/applicationlauncherror/localizederror-implementations.md)

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