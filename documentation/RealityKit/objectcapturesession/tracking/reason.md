# ObjectCaptureSession.Tracking.Reason

**Framework**: RealityKit  
**Kind**: enum

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
- [ObjectCaptureSession.Tracking.Reason.excessiveMotion](objectcapturesession/tracking/reason/excessivemotion.md)
  The device is moving too fast for accurate tracking.
- [ObjectCaptureSession.Tracking.Reason.initializing](objectcapturesession/tracking/reason/initializing.md)
  Tracking is still initializing, usually at the start of a new session.
- [ObjectCaptureSession.Tracking.Reason.insufficientFeatures](objectcapturesession/tracking/reason/insufficientfeatures.md)
  The scene does not contain enough distinguishable features for accurate camera tracking.
- [ObjectCaptureSession.Tracking.Reason.relocalizing](objectcapturesession/tracking/reason/relocalizing.md)
  The session is attempting to resume tracking after an interruption, such as the app being paused.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/tracking/reason)*