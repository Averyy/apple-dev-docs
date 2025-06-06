# ARPlaneAnchor.Classification.Status.unknown

**Framework**: ARKit  
**Kind**: case

ARKit has completed its classification process for the plane anchor, but the result is inconclusive.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case unknown
```

#### Discussion

ARKit attempts to classify detected planes using a finite set of common categories. However, a detected plane may not be a real object fitting any of those categories, or the plane classification process may not be able to recognize it. In such cases, the plane anchor’s [`classification`](arplaneanchor/classification-2hi2p.md) is [`ARPlaneAnchor.Classification.none(_:)`](arplaneanchor/classification-swift.enum/none(_:).md) with an associated value of [`ARPlaneAnchor.Classification.Status.unknown`](arplaneanchor/classification-swift.enum/status/unknown.md).

## See Also

- [ARPlaneAnchor.Classification.Status.notAvailable](arplaneanchor/classification-swift.enum/status/notavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneAnchor.Classification.Status.undetermined](arplaneanchor/classification-swift.enum/status/undetermined.md)
  ARKit has not yet produced a classification for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/status/unknown)*