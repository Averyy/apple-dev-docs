# feedback

**Framework**: RealityKit  
**Kind**: property

The current set of active `Feedback` states.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var feedback: Set<ObjectCaptureSession.Feedback> { get }
```

## See Also

- [ObjectCaptureSession.Feedback](objectcapturesession/feedback-swift.enum.md)
  Provides information about possible problems with the capture session.
- [var isPaused: Bool](objectcapturesession/ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var state: ObjectCaptureSession.CaptureState](objectcapturesession/state.md)
  The current state of the capture session.
- [var cameraTracking: ObjectCaptureSession.Tracking](objectcapturesession/cameratracking.md)
  The current state of ARKit camera tracking.
- [ObjectCaptureSession.Tracking](objectcapturesession/tracking.md)
  A data structure that describes the current tracking state for the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/feedback-swift.property)*