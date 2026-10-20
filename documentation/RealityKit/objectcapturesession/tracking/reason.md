# ObjectCaptureSession.Tracking.Reason

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The reason that tracking quality has degraded.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
enum Reason
```

## Topics

### Enumeration Cases
- [ObjectCaptureSession.Tracking.Reason.excessiveMotion](./reason/excessivemotion.md)
  The device is moving too fast for accurate tracking.
- [ObjectCaptureSession.Tracking.Reason.initializing](./reason/initializing.md)
  Tracking is still initializing, usually at the start of a new session.
- [ObjectCaptureSession.Tracking.Reason.insufficientFeatures](./reason/insufficientfeatures.md)
  The scene does not contain enough distinguishable features for accurate camera tracking.
- [ObjectCaptureSession.Tracking.Reason.relocalizing](./reason/relocalizing.md)
  The session is attempting to resume tracking after an interruption, such as the app being paused.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/tracking/reason)*