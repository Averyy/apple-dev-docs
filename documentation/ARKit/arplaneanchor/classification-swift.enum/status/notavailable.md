# ARPlaneAnchor.Classification.Status.notAvailable

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

ARKit cannot currently provide plane classification information.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case notAvailable
```

#### Discussion

Plane classification is available only on iPhone XS and iPhone XS Max devices. On other devices, all plane anchors always indicate a classification status of [`ARPlaneAnchor.Classification.Status.notAvailable`](./notavailable.md).

A classification status of [`ARPlaneAnchor.Classification.Status.notAvailable`](./notavailable.md) can also occur if the plane classification process is temporarily unavilable.

## See Also

### Classification Status
- [ARPlaneAnchor.Classification.Status.undetermined](./undetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneAnchor.Classification.Status.unknown](./unknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/status/notavailable)*