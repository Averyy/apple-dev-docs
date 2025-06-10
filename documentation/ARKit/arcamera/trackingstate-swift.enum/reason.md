# ARCamera.TrackingState.Reason

**Framework**: ARKit  
**Kind**: enum

Causes of limited position-tracking quality.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
enum Reason
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

## Topics

### Inhibitors of Tracking Quality
- [ARCamera.TrackingState.Reason.initializing](arcamera/trackingstate-swift.enum/reason/initializing.md)
  The AR session has not gathered enough camera or motion data to provide tracking information.
- [ARCamera.TrackingState.Reason.relocalizing](arcamera/trackingstate-swift.enum/reason/relocalizing.md)
  The AR session is attempting to resume after an interruption.
- [ARCamera.TrackingState.Reason.excessiveMotion](arcamera/trackingstate-swift.enum/reason/excessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARCamera.TrackingState.Reason.insufficientFeatures](arcamera/trackingstate-swift.enum/reason/insufficientfeatures.md)
  The scene visible to the camera doesn’t contain enough distinguishable features for image-based position tracking.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ARCamera.TrackingState.notAvailable](arcamera/trackingstate-swift.enum/notavailable.md)
  Camera position tracking is not available.
- [case limited(ARCamera.TrackingState.Reason)](arcamera/trackingstate-swift.enum/limited(_:).md)
  Tracking is available, but the quality of results is questionable.
- [ARCamera.TrackingState.normal](arcamera/trackingstate-swift.enum/normal.md)
  Camera position tracking is providing optimal results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum/reason)*