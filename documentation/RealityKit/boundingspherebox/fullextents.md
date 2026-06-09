# fullExtents

**Framework**: RealityKit  
**Kind**: property

The full extents of the optional axis-aligned bounding box.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var fullExtents: SIMD3<Float>? { get set }
```

#### Discussion

Equivalent to `halfExtents.map { $0 * 2 }`.

## See Also

- [var center: SIMD3<Float>](boundingspherebox/center.md)
  The center of the bounding volume in model space.
- [var halfExtents: SIMD3<Float>?](boundingspherebox/halfextents.md)
  The half-extents of the optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingspherebox/fullextents)*