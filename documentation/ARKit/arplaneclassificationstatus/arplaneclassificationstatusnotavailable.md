# ARPlaneClassificationStatusNotAvailable

**Framework**: ARKit  
**Kind**: case

ARKit cannot currently provide plane classification information.

## Declaration

```swift
ARPlaneClassificationStatusNotAvailable
```

#### Discussion

Plane classification is available only on iPhone XS, iPhone XS Max, and iPhone XR. On other devices, all plane anchors always indicate a classification status of [`ARPlaneClassificationStatusNotAvailable`](arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md).

A classification status of [`ARPlaneClassificationStatusNotAvailable`](arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md) can also occur if the plane classification process is temporarily unavilable.

## See Also

- [ARPlaneClassificationStatusUndetermined](arplaneclassificationstatus/arplaneclassificationstatusundetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneClassificationStatusUnknown](arplaneclassificationstatus/arplaneclassificationstatusunknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.
- [ARPlaneClassificationStatusKnown](arplaneclassificationstatus/arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus/arplaneclassificationstatusnotavailable)*