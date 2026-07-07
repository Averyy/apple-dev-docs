# sessionContentURL

**Framework**: LockedCameraCapture  
**Kind**: property

A temporary directory URL inside the extension’s data container.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final var sessionContentURL: URL { get }
```

#### Discussion

Store captured content during the current `LockedCameraCaptureSession` to this `URL`.

The system copies the contents of this directory to the extension’s containing app’s data container when the extension is suspended. The extension’s data container is erased once the system finishes copying the contents. Store all data that needs to be persisted past the lifetime of the extension process to this directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession/sessioncontenturl)*