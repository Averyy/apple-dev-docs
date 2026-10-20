# formUnion(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Expands the bounding box to contain the specified point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
mutating func formUnion(_ point: SIMD3<Float>)
```

**Other overloads**:

```swift
mutating func formUnion(_ other: BoundingBox)
```

## Parameters

- `point`: A point in space.

## See Also

### Expanding boxes
- [func union(BoundingBox) -> BoundingBox](./union%28_%29-1y8hw.md)
  Creates a bounding box containing the current bounds and the specified bounds.
- [func formUnion(BoundingBox)](./formunion%28_%29-5iy03.md)
  Expands the bounding box to contain the specified bounds.
- [func union(SIMD3<Float>) -> BoundingBox](./union%28_%29-g4th.md)
  Creates a bounding box containing the current bounds and the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/formunion(_:)-6itj9)*