# ARPlaneClassificationStatusUndetermined

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

ARKit has not yet produced a classification for the plane anchor.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
ARPlaneClassificationStatusUndetermined
```

## Discussion

This status occurs when ARKit is still in the process of plane classification. To be notified when ARKit produces a classification, observe the same plane anchor in a later frame (for example, in the [`session(_:didUpdate:)`](../arsessiondelegate/session%28_,didupdate%29-3qtt8.md) or [`renderer(_:didUpdate:for:)`](../arscnviewdelegate/renderer%28_,didupdate,for%29.md) delegate method).

## See Also

### Classification Status
- [ARPlaneClassificationStatusNotAvailable](./arplaneclassificationstatusnotavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneClassificationStatusUnknown](./arplaneclassificationstatusunknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.
- [ARPlaneClassificationStatusKnown](./arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus/arplaneclassificationstatusundetermined)*