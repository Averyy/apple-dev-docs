# ARCamera.TrackingState.Reason

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Causes of limited position-tracking quality.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
enum Reason
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](../../managing-session-life-cycle-and-tracking-quality.md)

## Topics

### Inhibitors of Tracking Quality
- [ARCamera.TrackingState.Reason.initializing](./reason/initializing.md)
  The AR session has not gathered enough camera or motion data to provide tracking information.
- [ARCamera.TrackingState.Reason.relocalizing](./reason/relocalizing.md)
  The AR session is attempting to resume after an interruption.
- [ARCamera.TrackingState.Reason.excessiveMotion](./reason/excessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARCamera.TrackingState.Reason.insufficientFeatures](./reason/insufficientfeatures.md)
  The scene visible to the camera doesn’t contain enough distinguishable features for image-based position tracking.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Determining the camera tracking status
- [ARCamera.TrackingState.notAvailable](./notavailable.md)
  Camera position tracking is not available.
- [case limited(ARCamera.TrackingState.Reason)](./limited%28_%29.md)
  Tracking is available, but the quality of results is questionable.
- [ARCamera.TrackingState.normal](./normal.md)
  Camera position tracking is providing optimal results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum/reason)*