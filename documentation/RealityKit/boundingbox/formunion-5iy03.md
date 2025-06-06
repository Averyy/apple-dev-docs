# formUnion(_:)

**Framework**: RealityKit  
**Kind**: method

Expands the bounding box to contain the specified bounds.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
mutating func formUnion(_ other: BoundingBox)
```

## Parameters

- `other`: Another bounding box.

## See Also

- [func union(BoundingBox) -> BoundingBox](boundingbox/union(_:)-1y8hw.md)
  Creates a bounding box containing the current bounds and the specified bounds.
- [func union(SIMD3<Float>) -> BoundingBox](boundingbox/union(_:)-g4th.md)
  Creates a bounding box containing the current bounds and the specified point.
- [func formUnion(SIMD3<Float>)](boundingbox/formunion(_:)-6itj9.md)
  Expands the bounding box to contain the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/formunion(_:)-5iy03)*