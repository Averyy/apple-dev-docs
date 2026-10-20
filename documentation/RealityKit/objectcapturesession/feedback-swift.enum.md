# ObjectCaptureSession.Feedback

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Provides information about possible problems with the capture session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
enum Feedback
```

## Topics

### Enumeration Cases
- [ObjectCaptureSession.Feedback.environmentLowLight](./feedback-swift.enum/environmentlowlight.md)
  The lighting in the environment is low, which can degrade reconstruction quality. Auto-capture still proceeds but reconstruction quality may suffer.  It is advised to increase lighting.
- [ObjectCaptureSession.Feedback.environmentTooDark](./feedback-swift.enum/environmenttoodark.md)
  The lighting in the environment is too dark to proceed.  Auto-capture will stop and the user will need to increase lighting levels to resolve this condition in order to continue capture.
- [ObjectCaptureSession.Feedback.movingTooFast](./feedback-swift.enum/movingtoofast.md)
  The user is moving too quickly for clear images and the capturing may be paused to ensure quality.
- [ObjectCaptureSession.Feedback.objectNotDetected](./feedback-swift.enum/objectnotdetected.md)
  If the detection of the object fails and a default manual box is presented instead, this element will be in the feedback to allow relevant information to be provided to the user for selecting a manual scanning volume and describing the operational envelope for the automatic object detection.
- [ObjectCaptureSession.Feedback.objectNotFlippable](./feedback-swift.enum/objectnotflippable.md)
  It is not recommended to flip this object since is is unlikely the algorithm will be able to stitch the flipped orientation.  This is usually due to feature-less, low-texture objects.  In this case, multiple passes at different heights leaving object at its original orientation are recommended instead of flipping.
- [ObjectCaptureSession.Feedback.objectTooClose](./feedback-swift.enum/objecttooclose.md)
  The camera is too close to the object and it cannot be tracked well.
- [ObjectCaptureSession.Feedback.objectTooFar](./feedback-swift.enum/objecttoofar.md)
  The camera is too far from the object and it cannot be captured well.
- [ObjectCaptureSession.Feedback.outOfFieldOfView](./feedback-swift.enum/outoffieldofview.md)
  The bounding box of the object is not in the field of view of the camera so auto-capture will not operate.
- [ObjectCaptureSession.Feedback.overCapturing](./feedback-swift.enum/overcapturing.md)
  If the `numberOfShotsTaken > maximumNumberOfInputImages` then any additional shots will not be used in an on-device reconstruction and reconstruction is recommended to be done on a Mac that can support a greater number of images.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring a session
- [var feedback: Set<ObjectCaptureSession.Feedback>](./feedback-swift.property.md)
  The current set of active `Feedback` states.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var state: ObjectCaptureSession.CaptureState](./state.md)
  The current state of the capture session.
- [var cameraTracking: ObjectCaptureSession.Tracking](./cameratracking.md)
  The current state of ARKit camera tracking.
- [ObjectCaptureSession.Tracking](./tracking.md)
  A data structure that describes the current tracking state for the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/feedback-swift.enum)*