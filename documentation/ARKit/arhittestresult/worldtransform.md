# worldTransform

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The position and orientation of the result relative to the world coordinate system.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
var worldTransform: simd_float4x4 { get }
```

```objc
@property (nonatomic, readonly) simd_float4x4 worldTransform;
```

#### Discussion

This transform matrix indicates the intersection point between the detected surface and the ray that created the hit-test result. A hit-test projects a 2D point in the image or view coordinate system along a ray into the 3D world space and reports results where that line intersects detected surfaces.

The session configuration’s [`worldAlignment`](../arconfiguration/worldalignment-swift.property.md) property defines the world coordinate system.

## See Also

### Examining Result Geometry
- [var distance: CGFloat](./distance.md)
  The distance, in meters, from the camera to the detected surface.
- [var localTransform: simd_float4x4](./localtransform.md)
  The position and orientation of the result relative to the nearest anchor or feature point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/worldtransform)*