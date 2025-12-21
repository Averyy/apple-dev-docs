# extents

**Framework**: RealityKit  
**Kind**: property

The extents of the bounding box.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var extents: SIMD3<Float> { get }
```

#### Discussion

This value is (0, 0, 0) if the box is empty.

## See Also

- [var max: SIMD3<Float>](boundingbox/max.md)
  The position of the maximum corner of the box.
- [var min: SIMD3<Float>](boundingbox/min.md)
  The position of the minimum corner of the box.
- [var center: SIMD3<Float>](boundingbox/center.md)
  The center of the bounding box.
- [var boundingRadius: Float](boundingbox/boundingradius.md)
  The radius of a bounding sphere that encompasses the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/extents)*