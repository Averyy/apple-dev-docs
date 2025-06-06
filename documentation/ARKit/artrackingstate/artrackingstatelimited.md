# ARTrackingStateLimited

**Framework**: ARKit  
**Kind**: case

Tracking is available, but the quality of results is questionable.

## Declaration

```swift
ARTrackingStateLimited
```

#### Discussion

In this state, the positions and transforms of anchors in the scene (especially detected planes) may not be accurate or consistent from one captured frame to the next.

See the associated [`ARTrackingStateReason`](artrackingstatereason.md) value for information you can present to the user for improving tracking quality.

## See Also

- [ARTrackingStateNotAvailable](artrackingstate/artrackingstatenotavailable.md)
  Camera position tracking is not available.
- [ARTrackingStateNormal](artrackingstate/artrackingstatenormal.md)
  Camera position tracking is providing optimal results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackingstate/artrackingstatelimited)*