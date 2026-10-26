# ARTrackingStateReason

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Possible causes for limited position-tracking quality.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
enum ARTrackingStateReason : NSInteger;
```

## Topics

### Reason Values
- [ARTrackingStateReasonNone](./artrackingstatereason/artrackingstatereasonnone.md)
  The current tracking state is not limited.
- [ARTrackingStateReasonInitializing](./artrackingstatereason/artrackingstatereasoninitializing.md)
  The AR session has not yet gathered enough camera or motion data to provide tracking information.
- [ARTrackingStateReasonRelocalizing](./artrackingstatereason/artrackingstatereasonrelocalizing.md)
  The AR session is attempting to resume after an interruption.
- [ARTrackingStateReasonExcessiveMotion](./artrackingstatereason/artrackingstatereasonexcessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARTrackingStateReasonInsufficientFeatures](./artrackingstatereason/artrackingstatereasoninsufficientfeatures.md)
  The scene visible to the camera does not contain enough distinguishable features for image-based position tracking.

## See Also

### Handling Tracking Status
- [trackingState](./arcamera/trackingstate-9pgmq.md)
  The general quality of position tracking available when the camera captured a frame.
- [ARTrackingState](./artrackingstate.md)
  Possible values for position-tracking quality.
- [trackingStateReason](./arcamera/trackingstatereason.md)
  A possible diagnosis for limited position-tracking quality as of when the camera captured a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackingstatereason)*