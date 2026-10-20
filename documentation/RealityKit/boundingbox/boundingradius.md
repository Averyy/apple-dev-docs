# boundingRadius

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The radius of a bounding sphere that encompasses the bounding box.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var boundingRadius: Float { get }
```

#### Discussion

This value is 0 if the box is empty.

## See Also

### Getting the box characteristics
- [var max: SIMD3<Float>](./max.md)
  The position of the maximum corner of the box.
- [var min: SIMD3<Float>](./min.md)
  The position of the minimum corner of the box.
- [var center: SIMD3<Float>](./center.md)
  The center of the bounding box.
- [var extents: SIMD3<Float>](./extents.md)
  The extents of the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/boundingradius)*