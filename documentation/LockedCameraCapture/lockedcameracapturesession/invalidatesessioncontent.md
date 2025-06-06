# invalidateSessionContent()

**Framework**: LockedCameraCapture  
**Kind**: method

Invalidates the contents of the session contents URL, deleting them. Note this does not remove the contents directory itself. This is useful in case the extension has already ingested its contents via PhotoKit and wishes to not persist any data (but can still use this directory as a working directory to recover from an unexpected termination).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final func invalidateSessionContent() async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession/invalidatesessioncontent())*