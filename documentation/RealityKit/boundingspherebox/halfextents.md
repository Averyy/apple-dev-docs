# halfExtents

**Framework**: RealityKit  
**Kind**: property

The half-extents of the optional axis-aligned bounding box.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var halfExtents: SIMD3<Float>? { get set }
```

#### Discussion

When non-`nil`, the renderer uses the box for culling. Setting this to a value expands `radius` to circumscribe the box.

## See Also

- [var center: SIMD3<Float>](boundingspherebox/center.md)
  The center of the bounding volume in model space.
- [var fullExtents: SIMD3<Float>?](boundingspherebox/fullextents.md)
  The full extents of the optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingspherebox/halfextents)*