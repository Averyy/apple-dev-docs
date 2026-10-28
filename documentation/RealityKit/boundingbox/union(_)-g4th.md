# union(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates a bounding box containing the current bounds and the specified point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func union(_ point: SIMD3<Float>) -> BoundingBox
```

**Other overloads**:

```swift
func union(_ other: BoundingBox) -> BoundingBox
```

## Return Value

The new bounding box.

## Parameters

- `point`: A point in space.

## See Also

### Expanding boxes
- [func union(BoundingBox) -> BoundingBox](./union%28_%29-1y8hw.md)
  Creates a bounding box containing the current bounds and the specified bounds.
- [func formUnion(BoundingBox)](./formunion%28_%29-5iy03.md)
  Expands the bounding box to contain the specified bounds.
- [func formUnion(SIMD3<Float>)](./formunion%28_%29-6itj9.md)
  Expands the bounding box to contain the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/union(_:)-g4th)*