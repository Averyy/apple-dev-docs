# LockedCameraCapture

**Framework**: LockedCameraCapture  
**Kind**: module

Capture content with your app’s camera experience when the device is locked.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

#### Overview

Use the LockedCameraCapture framework to create an extension that allows people to launch your app’s camera experience and capture content quickly when the device is locked. This extension makes your camera experience accessible to people from Control Center, the Lock Screen, or the Action button.

![A conceptual image that shows a control with a camera icon on the Lock Screen on iPhone, in Control Center on iPhone, and being performed with the Action button on iPhone 15 Pro.](https://docs-assets.developer.apple.com/published/92356c4d536464fbcc88d5a37400d82a/locked-camera-capture-overview%402x.png)

## Topics

### Essentials
- [Creating a camera experience for the Lock Screen](creating-a-camera-experience-for-the-lock-screen.md)
  Offer your app’s camera experience on locked devices from Control Center, the Lock Screen, and the Action button.
### Capture and launch
- [struct LockedCameraCaptureUIScene](lockedcameracaptureuiscene.md)
  A structure that contains the session object and UI to display for the locked camera capture extension.
- [class LockedCameraCaptureSession](lockedcameracapturesession.md)
  An object that can request to open the extension’s containing app and receives session configuration updates.
### App integration
- [class LockedCameraCaptureManager](lockedcameracapturemanager.md)
  An object that provides handling of captured content and transitioning to the extension’s containing app.
- [let NSUserActivityTypeLockedCameraCapture: String](nsuseractivitytypelockedcameracapture.md)
  A type to use when opening your app from the capture extension.
### Extension
- [protocol LockedCameraCaptureExtension](lockedcameracaptureextension.md)
  A protocol that creates a locked camera capture extension.
- [protocol LockedCameraCaptureExtensionScene](lockedcameracaptureextensionscene.md)
  A protocol that provides the UI for the locked camera capture extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/LockedCameraCapture)*