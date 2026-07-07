# LockedCameraCaptureUIScene

**Framework**: LockedCameraCapture  
**Kind**: struct

A structure that contains the session object and UI to display for the locked camera capture extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
struct LockedCameraCaptureUIScene<Content> where Content : View
```

## Topics

### Initializers
- [init(content: (LockedCameraCaptureSession) -> Content)](lockedcameracaptureuiscene/init(content:).md)
  Creates a locked camera capture extension scene.
### Instance Properties
- [var body: some AppExtensionScene](lockedcameracaptureuiscene/body.md)
  The content and behavior of the locked camera capture extension’s UI.
- [let session: LockedCameraCaptureSession](lockedcameracaptureuiscene/session.md)
  An object that can request to open the extension’s containing app and receives session configuration updates.

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
- [LockedCameraCaptureExtensionScene](lockedcameracaptureextensionscene.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class LockedCameraCaptureSession](lockedcameracapturesession.md)
  An object that can request to open the extension’s containing app and receives session configuration updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracaptureuiscene)*