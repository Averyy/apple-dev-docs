# ARCamera.TrackingState.Reason.relocalizing

**Framework**: ARKit  
**Kind**: case

The AR session is attempting to resume after an interruption.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
case relocalizing
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

ARKit cannot track device position or orientation when the session has been interrupted (for example, by dismissing the view hosting an AR session or switching to another app). When resuming the session after an interruption, the world coordinate system (used for placing anchors) likely no longer match the device’s real-world environment.

If your session or view delegate implements the [`sessionShouldAttemptRelocalization(_:)`](arsessionobserver/sessionshouldattemptrelocalization(_:).md) method and returns [`true`](https://developer.apple.com/documentation/Swift/true), ARKit attempts to reconcile pre- and post-interruption world tracking state. During this process, called , world tracking quality is [`ARCamera.TrackingState.limited(_:)`](arcamera/trackingstate-swift.enum/limited(_:).md), with a resaon value of [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md), indicating that hit tests and anchor placement are less accurate.

If successful, relocalization ends after a short time, tracking quality returns to the [`ARCamera.TrackingState.normal`](arcamera/trackingstate-swift.enum/normal.md) state, and the world coordinate system and anchor positions reflect their state before the interruption.

For relocalization to succeed, the device must be returned to a position and orientation approximately near where it was when the session was interrupted. If these conditions never occur (or cannot occur; for example, if the device has moved to an entirely different environment), the session will remain in the [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) state indefinitely.

> ❗ **Important**:  When in the [`ARCamera.TrackingState.Reason.relocalizing`](arcamera/trackingstate-swift.enum/reason/relocalizing.md) state, offer the user a way out in case relocalization never succeeds. For example, offer a button for resetting the session, which appears after the relocalizing state has remained for a fixed amount of time.

## See Also

- [ARCamera.TrackingState.Reason.initializing](arcamera/trackingstate-swift.enum/reason/initializing.md)
  The AR session has not gathered enough camera or motion data to provide tracking information.
- [ARCamera.TrackingState.Reason.excessiveMotion](arcamera/trackingstate-swift.enum/reason/excessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARCamera.TrackingState.Reason.insufficientFeatures](arcamera/trackingstate-swift.enum/reason/insufficientfeatures.md)
  The scene visible to the camera doesn’t contain enough distinguishable features for image-based position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/trackingstate-swift.enum/reason/relocalizing)*