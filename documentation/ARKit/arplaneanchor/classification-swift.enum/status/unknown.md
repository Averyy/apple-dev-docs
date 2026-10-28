# ARPlaneAnchor.Classification.Status.unknown

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

ARKit has completed its classification process for the plane anchor, but the result is inconclusive.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case unknown
```

## Discussion

ARKit attempts to classify detected planes using a finite set of common categories. However, a detected plane may not be a real object fitting any of those categories, or the plane classification process may not be able to recognize it. In such cases, the plane anchor’s [`classification`](../../classification-2hi2p.md) is [`ARPlaneAnchor.Classification.none(_:)`](../none%28_%29.md) with an associated value of [`ARPlaneAnchor.Classification.Status.unknown`](./unknown.md).

## See Also

### Classification Status
- [ARPlaneAnchor.Classification.Status.notAvailable](./notavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneAnchor.Classification.Status.undetermined](./undetermined.md)
  ARKit has not yet produced a classification for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/status/unknown)*