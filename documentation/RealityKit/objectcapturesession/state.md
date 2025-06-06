# state

**Framework**: RealityKit  
**Kind**: property

The current state of the capture session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var state: ObjectCaptureSession.CaptureState { get }
```

## See Also

- [var feedback: Set<ObjectCaptureSession.Feedback>](objectcapturesession/feedback-swift.property.md)
  The current set of active `Feedback` states.
- [ObjectCaptureSession.Feedback](objectcapturesession/feedback-swift.enum.md)
  Provides information about possible problems with the capture session.
- [var isPaused: Bool](objectcapturesession/ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var cameraTracking: ObjectCaptureSession.Tracking](objectcapturesession/cameratracking.md)
  The current state of ARKit camera tracking.
- [ObjectCaptureSession.Tracking](objectcapturesession/tracking.md)
  A data structure that describes the current tracking state for the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/state)*