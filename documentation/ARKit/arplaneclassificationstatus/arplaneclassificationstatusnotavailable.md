# ARPlaneClassificationStatusNotAvailable

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

ARKit cannot currently provide plane classification information.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
ARPlaneClassificationStatusNotAvailable
```

## Discussion

Plane classification is available only on iPhone XS, iPhone XS Max, and iPhone XR. On other devices, all plane anchors always indicate a classification status of [`ARPlaneClassificationStatusNotAvailable`](./arplaneclassificationstatusnotavailable.md).

A classification status of [`ARPlaneClassificationStatusNotAvailable`](./arplaneclassificationstatusnotavailable.md) can also occur if the plane classification process is temporarily unavilable.

## See Also

### Classification Status
- [ARPlaneClassificationStatusUndetermined](./arplaneclassificationstatusundetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneClassificationStatusUnknown](./arplaneclassificationstatusunknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.
- [ARPlaneClassificationStatusKnown](./arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus/arplaneclassificationstatusnotavailable)*