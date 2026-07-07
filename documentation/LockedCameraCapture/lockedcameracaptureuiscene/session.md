# session

**Framework**: LockedCameraCapture  
**Kind**: property

An object that can request to open the extension’s containing app and receives session configuration updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
let session: LockedCameraCaptureSession
```

#### Discussion

Provided during the initialization of the [`LockedCameraCaptureExtensionScene`](lockedcameracaptureextensionscene.md). Only the system can initialize this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracaptureuiscene/session)*