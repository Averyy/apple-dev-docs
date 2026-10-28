# ARTrackingStateReasonInitializing

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

The AR session has not yet gathered enough camera or motion data to provide tracking information.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
ARTrackingStateReasonInitializing
```

## Discussion

This value occurs temporarily after starting a new AR session or changing configurations.

## See Also

### Reason Values
- [ARTrackingStateReasonNone](./artrackingstatereasonnone.md)
  The current tracking state is not limited.
- [ARTrackingStateReasonRelocalizing](./artrackingstatereasonrelocalizing.md)
  The AR session is attempting to resume after an interruption.
- [ARTrackingStateReasonExcessiveMotion](./artrackingstatereasonexcessivemotion.md)
  The device is moving too fast for accurate image-based position tracking.
- [ARTrackingStateReasonInsufficientFeatures](./artrackingstatereasoninsufficientfeatures.md)
  The scene visible to the camera does not contain enough distinguishable features for image-based position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackingstatereason/artrackingstatereasoninitializing)*