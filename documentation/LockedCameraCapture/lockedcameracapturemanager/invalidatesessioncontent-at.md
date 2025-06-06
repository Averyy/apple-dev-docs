# invalidateSessionContent(at:)

**Framework**: LockedCameraCapture  
**Kind**: method

Tells the system that the app no longer needs the directory at the URL and it can be deleted.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final func invalidateSessionContent(at url: URL) async throws
```

#### Discussion

The directory at the `URL` contains captured content for a session. Store the captured content appropriately before calling this method, otherwise the system deletes it.

## Parameters

- `url`: A URL from   .   The system ignores other URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager/invalidatesessioncontent(at:))*