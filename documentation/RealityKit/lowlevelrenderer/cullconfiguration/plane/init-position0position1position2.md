# init(position0:position1:position2:)

**Framework**: RealityKit  
**Kind**: init

Creates a plane from three positions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(position0 p0: SIMD3<Float>, position1 p1: SIMD3<Float>, position2 p2: SIMD3<Float>)
```

#### Discussion

The plane’s outward normal is computed as `cross(p1 − p0, p2 − p1)`, so the three positions wind counterclockwise when viewed from the outward (culled) side of the plane.

## See Also

- [init(position: SIMD3<Float>, direction: SIMD3<Float>)](lowlevelrenderer/cullconfiguration/plane/init(position:direction:).md)
  Creates a plane from a point on the plane and an outward normal direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/plane/init(position0:position1:position2:))*