# sessionContentURLs

**Framework**: LockedCameraCapture  
**Kind**: property

An array of URLs that each point to a directory containing captured content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final var sessionContentURLs: [URL] { get }
```

#### Discussion

Content in the URLs is captured during a capture extension’s [`LockedCameraCaptureSession`](lockedcameracapturesession.md). These directories are located within the capture extension’s containing app’s data container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager/sessioncontenturls)*