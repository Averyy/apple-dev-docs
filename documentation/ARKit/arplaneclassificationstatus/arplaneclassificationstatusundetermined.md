# ARPlaneClassificationStatusUndetermined

**Framework**: ARKit  
**Kind**: case

ARKit has not yet produced a classification for the plane anchor.

## Declaration

```swift
ARPlaneClassificationStatusUndetermined
```

#### Discussion

This status occurs when ARKit is still in the process of plane classification. To be notified when ARKit produces a classification, observe the same plane anchor in a later frame (for example, in the [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) or [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md) delegate method).

## See Also

- [ARPlaneClassificationStatusNotAvailable](arplaneclassificationstatus/arplaneclassificationstatusnotavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneClassificationStatusUnknown](arplaneclassificationstatus/arplaneclassificationstatusunknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.
- [ARPlaneClassificationStatusKnown](arplaneclassificationstatus/arplaneclassificationstatusknown.md)
  ARKit has completed its classfication process for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassificationstatus/arplaneclassificationstatusundetermined)*