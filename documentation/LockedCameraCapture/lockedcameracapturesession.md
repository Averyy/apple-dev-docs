# LockedCameraCaptureSession

**Framework**: LockedCameraCapture  
**Kind**: class

An object that can request to open the extension’s containing app and receives session configuration updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final class LockedCameraCaptureSession
```

#### Overview

Provided during the initialization of the [`LockedCameraCaptureExtensionScene`](lockedcameracaptureextensionscene.md). Only the system can initialize this object.

## Topics

### Instance Properties
- [var sessionContentURL: URL](lockedcameracapturesession/sessioncontenturl.md)
  A temporary directory URL inside the extension’s data container.
### Instance Methods
- [func invalidateSessionContent() async throws](lockedcameracapturesession/invalidatesessioncontent.md)
  Invalidates the contents of the session contents URL, deleting them. Note this does not remove the contents directory itself. This is useful in case the extension has already ingested its contents via PhotoKit and wishes to not persist any data (but can still use this directory as a working directory to recover from an unexpected termination).
- [func openApplication(for: NSUserActivity) async throws](lockedcameracapturesession/openapplication(for:).md)
  Initiates a request to open the extension’s containing app.
### Enumerations
- [LockedCameraCaptureSession.ApplicationLaunchError](lockedcameracapturesession/applicationlauncherror.md)
  Indicates why launching the extension’s containing app failed.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct LockedCameraCaptureUIScene](lockedcameracaptureuiscene.md)
  A structure that contains the session object and UI to display for the locked camera capture extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession)*