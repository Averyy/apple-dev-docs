# state

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

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

### Configuring a session
- [var feedback: Set<ObjectCaptureSession.Feedback>](./feedback-swift.property.md)
  The current set of active `Feedback` states.
- [ObjectCaptureSession.Feedback](./feedback-swift.enum.md)
  Provides information about possible problems with the capture session.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var cameraTracking: ObjectCaptureSession.Tracking](./cameratracking.md)
  The current state of ARKit camera tracking.
- [ObjectCaptureSession.Tracking](./tracking.md)
  A data structure that describes the current tracking state for the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/state)*