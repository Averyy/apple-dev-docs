# union(_:)

**Framework**: RealityKit  
**Kind**: method

Creates a bounding box containing the current bounds and the specified point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
func union(_ point: SIMD3<Float>) -> BoundingBox
```

#### Return Value

The new bounding box.

## Parameters

- `point`: A point in space.

## See Also

- [func union(BoundingBox) -> BoundingBox](boundingbox/union(_:)-1y8hw.md)
  Creates a bounding box containing the current bounds and the specified bounds.
- [func formUnion(BoundingBox)](boundingbox/formunion(_:)-5iy03.md)
  Expands the bounding box to contain the specified bounds.
- [func formUnion(SIMD3<Float>)](boundingbox/formunion(_:)-6itj9.md)
  Expands the bounding box to contain the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/union(_:)-g4th)*