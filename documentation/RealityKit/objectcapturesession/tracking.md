# ObjectCaptureSession.Tracking

**Framework**: RealityKit  
**Kind**: enum

A data structure that describes the current tracking state for the camera.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
enum Tracking
```

#### Overview

During an object capture, many factors contribute to the session’s ability to accurately track the position and orientation of the camera and object, including lighting and enough texture on the object and background. The object capture session uses this data structure to report the current tracking state in the [`cameraTracking`](objectcapturesession/cameratracking.md) property.  Additionally, the ARKit coaching overlay will automatically appear when tracking is not `.normal` — the app may need to hide its UI at this time as well to allow proper visibility of the coaching overlay or to provide additional information to the user to correct the situation.

## Topics

### Operators
- [static func == (ObjectCaptureSession.Tracking, ObjectCaptureSession.Tracking) -> Bool](objectcapturesession/tracking/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [case limited(reason: ObjectCaptureSession.Tracking.Reason)](objectcapturesession/tracking/limited(reason:).md)
  Tracking is available but its quality is degraded. The ARKit coaching overlay will appear when [`cameraTracking`](objectcapturesession/cameratracking.md) enters this state.
- [ObjectCaptureSession.Tracking.normal](objectcapturesession/tracking/normal.md)
  Tracking is available and the session detects no problems..
- [ObjectCaptureSession.Tracking.notAvailable](objectcapturesession/tracking/notavailable.md)
  Tracking is not yet available.
### Enumerations
- [ObjectCaptureSession.Tracking.Reason](objectcapturesession/tracking/reason.md)
  The reason that tracking quality has degraded.
### Default Implementations
- [Equatable Implementations](objectcapturesession/tracking/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var feedback: Set<ObjectCaptureSession.Feedback>](objectcapturesession/feedback-swift.property.md)
  The current set of active `Feedback` states.
- [ObjectCaptureSession.Feedback](objectcapturesession/feedback-swift.enum.md)
  Provides information about possible problems with the capture session.
- [var isPaused: Bool](objectcapturesession/ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var state: ObjectCaptureSession.CaptureState](objectcapturesession/state.md)
  The current state of the capture session.
- [var cameraTracking: ObjectCaptureSession.Tracking](objectcapturesession/cameratracking.md)
  The current state of ARKit camera tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/tracking)*