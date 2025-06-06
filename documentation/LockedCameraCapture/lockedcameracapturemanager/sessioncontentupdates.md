# sessionContentUpdates

**Framework**: LockedCameraCapture  
**Kind**: property

An `AsyncSequence` to process captured content from your capture extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final var sessionContentUpdates: some AsyncSequence<LockedCameraCaptureManager.SessionContentUpdate, Never> { get }
```

#### Discussion

Use this to process captured content as soon as it is available after your app launches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager/sessioncontentupdates)*