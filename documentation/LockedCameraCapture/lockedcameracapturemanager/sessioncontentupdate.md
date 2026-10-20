# LockedCameraCaptureManager.SessionContentUpdate

**Framework**: LockedCameraCapture  
**Kind**: enum  
**Role**: Enumeration

URLs provided by the [`sessionContentUpdates`](./sessioncontentupdates.md) `AsyncSequence`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum SessionContentUpdate
```

## Topics

### Enumeration Cases
- [LockedCameraCaptureManager.SessionContentUpdate.added(url:)](./sessioncontentupdate/added%28url%29.md)
  A URL to a directory of added session content.
- [LockedCameraCaptureManager.SessionContentUpdate.initial(urls:)](./sessioncontentupdate/initial%28urls%29.md)
  URLs to directories of the current session content available when beginning observation of [`sessionContentUpdates`](./sessioncontentupdates.md).
- [LockedCameraCaptureManager.SessionContentUpdate.removed(url:)](./sessioncontentupdate/removed%28url%29.md)
  A URL to a directory of removed session content.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager/sessioncontentupdate)*