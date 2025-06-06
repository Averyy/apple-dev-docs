# ARPlaneAnchor.Classification.none(_:)

**Framework**: ARKit  
**Kind**: case

No classification is available for the plane anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
case none(ARPlaneAnchor.Classification.Status)
```

#### Discussion

Plane classification can take longer than plane detection, and ARKit reports classifications only for planes where it has a high confidence in the result. See the associated [`ARPlaneAnchor.Classification.Status`](arplaneanchor/classification-swift.enum/status.md) value for the reason a plane anchor reports no classification.

## See Also

- [ARPlaneAnchor.Classification.Status](arplaneanchor/classification-swift.enum/status.md)
  Reasons ARKit is unable to classify a plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/none(_:))*