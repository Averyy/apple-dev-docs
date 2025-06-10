# LockedCameraCaptureManager

**Framework**: LockedCameraCapture  
**Kind**: class

An object that provides handling of captured content and transitioning to the extension’s containing app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final class LockedCameraCaptureManager
```

## Topics

### Instance Properties
- [var sessionContentURLs: [URL]](lockedcameracapturemanager/sessioncontenturls.md)
  An array of URLs that each point to a directory containing captured content.
- [var sessionContentUpdates: some AsyncSequence<LockedCameraCaptureManager.SessionContentUpdate, Never>](lockedcameracapturemanager/sessioncontentupdates.md)
  An `AsyncSequence` to process captured content from your capture extension.
### Instance Methods
- [func beginDelayingAppearance()](lockedcameracapturemanager/begindelayingappearance.md)
  Tells the system that the application wants to delay the application launch during a transition between the extension and the application
- [func endDelayingAppearance()](lockedcameracapturemanager/enddelayingappearance.md)
  Tells the system that the application is ready to appear after delaying the appearance during a transition between the extension and the application
- [func invalidateSessionContent(at: URL) async throws](lockedcameracapturemanager/invalidatesessioncontent(at:).md)
  Tells the system that the app no longer needs the directory at the URL and it can be deleted.
### Type Properties
- [static let shared: LockedCameraCaptureManager](lockedcameracapturemanager/shared.md)
  The shared instance of the manager.
### Enumerations
- [LockedCameraCaptureManager.SessionContentUpdate](lockedcameracapturemanager/sessioncontentupdate.md)
  URLs provided by the [`sessionContentUpdates`](lockedcameracapturemanager/sessioncontentupdates.md) `AsyncSequence`.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let NSUserActivityTypeLockedCameraCapture: String](nsuseractivitytypelockedcameracapture.md)
  A type to use when opening your app from the capture extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager)*