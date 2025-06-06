# LockedCameraCaptureManager.SessionContentUpdate

**Framework**: LockedCameraCapture  
**Kind**: enum

URLs provided by the [`sessionContentUpdates`](lockedcameracapturemanager/sessioncontentupdates.md) `AsyncSequence`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum SessionContentUpdate
```

## Topics

### Enumeration Cases
- [LockedCameraCaptureManager.SessionContentUpdate.added(url:)](lockedcameracapturemanager/sessioncontentupdate/added(url:).md)
  A URL to a directory of added session content.
- [LockedCameraCaptureManager.SessionContentUpdate.initial(urls:)](lockedcameracapturemanager/sessioncontentupdate/initial(urls:).md)
  URLs to directories of the current session content available when beginning observation of [`sessionContentUpdates`](lockedcameracapturemanager/sessioncontentupdates.md).
- [LockedCameraCaptureManager.SessionContentUpdate.removed(url:)](lockedcameracapturemanager/sessioncontentupdate/removed(url:).md)
  A URL to a directory of removed session content.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager/sessioncontentupdate)*