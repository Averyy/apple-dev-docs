# ARPlaneClassificationStatusUnknown

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

ARKit has completed its classification process for the plane anchor, but the result is inconclusive.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
ARPlaneClassificationStatusUnknown
```

## Discussion

ARKit attempts to classify detected planes using a finite set of common categories. However, a detected plane may not be a real object fitting any of those categories, or the plane classification process may not be able to recognize it. In such cases, the plane anchor’s [`classification`](../arplaneanchor/classification-2hi2p.md) is [`ARPlaneClassificationNone`](../arplaneclassification/arplaneclassificationnone.md) and its [`classificationStatus`](../arplaneanchor/classificationstatus.md) is [`ARPlaneClassificationStatusUnknown`](./arplaneclassificationstatusunknown.md).

## See Also

### Classification Status
- [ARPlaneClassificationStatusNotAvailable](./arplaneclassificationstatusnotavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneClassificationStatusUndetermined](./arplaneclassificationstatusundetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneClassificationStatusKnown](./arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus/arplaneclassificationstatusunknown)*