# worldTransform

**Framework**: ARKit  
**Kind**: property

The position and orientation of the result relative to the world coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var worldTransform: simd_float4x4 { get }
```

#### Discussion

This transform matrix indicates the intersection point between the detected surface and the ray that created the hit-test result. A hit-test projects a 2D point in the image or view coordinate system along a ray into the 3D world space and reports results where that line intersects detected surfaces.

The session configuration’s [`worldAlignment`](arconfiguration/worldalignment-swift.property.md) property defines the world coordinate system.

## See Also

- [var distance: CGFloat](arhittestresult/distance.md)
  The distance, in meters, from the camera to the detected surface.
- [var localTransform: simd_float4x4](arhittestresult/localtransform.md)
  The position and orientation of the result relative to the nearest anchor or feature point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/worldtransform)*