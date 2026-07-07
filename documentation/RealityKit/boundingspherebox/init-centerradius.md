# init(center:radius:)

**Framework**: RealityKit  
**Kind**: init

Creates a bounding sphere with the given center and radius.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(center: SIMD3<Float>, radius: Float)
```

## Parameters

- `center`: The center of the bounding sphere in model space.
- `radius`: The radius of the bounding sphere.

## See Also

- [init(center: SIMD3<Float>, halfExtents: SIMD3<Float>)](boundingspherebox/init(center:halfextents:).md)
  Creates a bounding box with the given center and half-extents, with a circumscribed sphere.
- [init(center: SIMD3<Float>, fullExtents: SIMD3<Float>)](boundingspherebox/init(center:fullextents:).md)
  Creates a bounding box with the given center and full extents, with a circumscribed sphere.
- [init(boxMin: SIMD3<Float>, boxMax: SIMD3<Float>)](boundingspherebox/init(boxmin:boxmax:).md)
  Creates a bounding box from minimum and maximum corner positions, with a circumscribed sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingspherebox/init(center:radius:))*