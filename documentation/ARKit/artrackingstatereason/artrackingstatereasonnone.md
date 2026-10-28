# ARTrackingStateReasonNone

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

The current tracking state is not limited.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
ARTrackingStateReasonNone
```

## Discussion

This value occurs when the [`trackingState`](../arcamera/trackingstate-9pgmq.md) property is [`ARTrackingStateNotAvailable`](../artrackingstate/artrackingstatenotavailable.md) or [`ARTrackingStateNormal`](../artrackingstate/artrackingstatenormal.md).

## See Also

### Reason Values
- [ARTrackingStateReasonInitializing](./artrackingstatereasoninitializing.md)
  The AR session has not yet gathered enough camera or motion data to provide tracking information.
- [ARTrackingStateReasonRelocalizing](./artrackingstatereasonrelocalizing.md)
  The AR session is attempting to resume after an interruption.
- [ARTrackingStateReasonExcessiveMotion](./artrackingstatereasonexcessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARTrackingStateReasonInsufficientFeatures](./artrackingstatereasoninsufficientfeatures.md)
  The scene visible to the camera does not contain enough distinguishable features for image-based position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackingstatereason/artrackingstatereasonnone)*