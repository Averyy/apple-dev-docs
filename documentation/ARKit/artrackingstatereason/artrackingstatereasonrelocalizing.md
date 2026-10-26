# ARTrackingStateReasonRelocalizing

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

The AR session is attempting to resume after an interruption.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```c
ARTrackingStateReasonRelocalizing
```

#### Discussion

ARKit cannot track device position or orientation when the session has been interrupted (for example, by dismissing the view hosting an AR session or switching to another app). When resuming the session after an interruption, you cannot be certain that the world coordinate system (used for placing anchors) matches the device’s real-world environment.

If your session or view delegate implements the [`sessionShouldAttemptRelocalization(_:)`](../arsessionobserver/sessionshouldattemptrelocalization%28_%29.md) method and returns [`true`](../../Swift/true.md), ARKit attempts to reconcile pre- and post-interruption world tracking state. During this process, called *relocalization*, world tracking quality is [`ARTrackingStateLimited`](../artrackingstate/artrackingstatelimited.md), with [`ARTrackingStateReasonRelocalizing`](./artrackingstatereasonrelocalizing.md) as the reason for limited quality.

If successful, the relocalization process ends after a short time, tracking quality returns to the [`ARTrackingStateNormal`](../artrackingstate/artrackingstatenormal.md) state, and the world coordinate system and anchor positions generally reflect their state before the interruption.

However, the speed and success rate of relocalization can vary depending on real-world conditions. You may wish to hide AR content or disable UI during relocalization, and reset tracking if relocalization doesn’t succeed within a time frame appropriate for your app.

## See Also

### Reason Values
- [ARTrackingStateReasonNone](./artrackingstatereasonnone.md)
  The current tracking state is not limited.
- [ARTrackingStateReasonInitializing](./artrackingstatereasoninitializing.md)
  The AR session has not yet gathered enough camera or motion data to provide tracking information.
- [ARTrackingStateReasonExcessiveMotion](./artrackingstatereasonexcessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARTrackingStateReasonInsufficientFeatures](./artrackingstatereasoninsufficientfeatures.md)
  The scene visible to the camera does not contain enough distinguishable features for image-based position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackingstatereason/artrackingstatereasonrelocalizing)*