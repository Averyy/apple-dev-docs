# fullExtents

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The full extents of the optional axis-aligned bounding box.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var fullExtents: SIMD3<Float>? { get set }
```

## Discussion

The full extents are equal to twice the [`halfExtents`](./halfextents.md).

## See Also

### Accessing the dimensions
- [var center: SIMD3<Float>](./center.md)
  The center of the bounding volume in model space.
- [var halfExtents: SIMD3<Float>?](./halfextents.md)
  The half-extents of the optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingspherebox/fullextents)*