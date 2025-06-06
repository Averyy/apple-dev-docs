# ARPlaneClassificationStatusUnknown

**Framework**: ARKit  
**Kind**: case

ARKit has completed its classification process for the plane anchor, but the result is inconclusive.

## Declaration

```swift
ARPlaneClassificationStatusUnknown
```

#### Discussion

ARKit attempts to classify detected planes using a finite set of common categories. However, a detected plane may not be a real object fitting any of those categories, or the plane classification process may not be able to recognize it. In such cases, the plane anchor’s [`classification`](arplaneanchor/classification-2hi2p.md) is [`ARPlaneClassificationNone`](arplaneclassification/arplaneclassificationnone.md) and its [`classificationStatus`](arplaneanchor/classificationstatus.md) is [`ARPlaneClassificationStatusUnknown`](arplaneclassificationstatus/arplaneclassificationstatusunknown.md).

## See Also

- [ARPlaneClassificationStatusNotAvailable](arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneClassificationStatusUndetermined](arplaneclassificationstatus/arplaneclassificationstatusundetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneClassificationStatusKnown](arplaneclassificationstatus/arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus/arplaneclassificationstatusunknown)*