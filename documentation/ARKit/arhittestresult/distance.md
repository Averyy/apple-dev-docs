# distance

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The distance, in meters, from the camera to the detected surface.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
var distance: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat distance;
```

## See Also

### Examining Result Geometry
- [var worldTransform: simd_float4x4](./worldtransform.md)
  The position and orientation of the result relative to the world coordinate system.
- [var localTransform: simd_float4x4](./localtransform.md)
  The position and orientation of the result relative to the nearest anchor or feature point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/distance)*