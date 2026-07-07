# cameraTracking

**Framework**: RealityKit  
**Kind**: property

The current state of ARKit camera tracking.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var cameraTracking: ObjectCaptureSession.Tracking { get }
```

#### Discussion

The ARKit coaching overylay will be automatically show if this state moves away from `.normal` since the loss of ARKit tracking will cause many of the Object Capture algorithms to pause until the environmental tracking issue is resolved by the user. Also, the app may want to adjust its UI when this state is not `.normal` to allow proper visibility of the coaching overlay.

## See Also

- [var feedback: Set<ObjectCaptureSession.Feedback>](objectcapturesession/feedback-swift.property.md)
  The current set of active `Feedback` states.
- [ObjectCaptureSession.Feedback](objectcapturesession/feedback-swift.enum.md)
  Provides information about possible problems with the capture session.
- [var isPaused: Bool](objectcapturesession/ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var state: ObjectCaptureSession.CaptureState](objectcapturesession/state.md)
  The current state of the capture session.
- [ObjectCaptureSession.Tracking](objectcapturesession/tracking.md)
  A data structure that describes the current tracking state for the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/cameratracking)*