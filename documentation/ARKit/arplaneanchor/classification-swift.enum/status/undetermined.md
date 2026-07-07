# ARPlaneAnchor.Classification.Status.undetermined

**Framework**: ARKit  
**Kind**: case

ARKit has not yet produced a classification for the plane anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case undetermined
```

#### Discussion

This status occurs when ARKit is still in the process of plane classification. To be notified when ARKit produces a classification, observe the same plane anchor in a later frame (for example, in the [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) or [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md) delegate method).

## See Also

- [ARPlaneAnchor.Classification.Status.notAvailable](arplaneanchor/classification-swift.enum/status/notavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneAnchor.Classification.Status.unknown](arplaneanchor/classification-swift.enum/status/unknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/status/undetermined)*