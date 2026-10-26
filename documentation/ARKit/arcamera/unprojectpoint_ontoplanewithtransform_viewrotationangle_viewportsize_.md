# unprojectPoint:ontoPlaneWithTransform:viewRotationAngle:viewportSize:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Unproject a 2D point from the viewport onto a plane in 3D world coordinates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```objc
- (simd_float3) unprojectPoint:(CGPoint) point ontoPlaneWithTransform:(simd_float4x4) planeTransform viewRotationAngle:(CGFloat) viewRotationAngle viewportSize:(CGSize) viewportSize;
```

#### Return Value

3D position in world coordinates or `NAN` values if unprojection is not possible.

#### Discussion

A 2D point in the viewport coordinate space can refer to any point along a line segment in the 3D coordinate space. Unprojecting calculates the 3D position of the point along this line segment that intersects the provided plane.

The view angle, in degrees, is the clockwise rotation needed to keep the camera image level with the horizon (`0` LandscapeRight, `90` Portrait, `180` LandscapeLeft, `270` PortraitUpsideDown). Obtain it from `ARSession.viewRotationAngle`.

## Parameters

- `point`: A point in the viewport coordinate system with origin at top-left.
- `planeTransform`: The transform used to define the coordinate system of the plane. The coordinate system’s positive Y axis is assumed to be the normal of the plane.
- `viewRotationAngle`: View rotation angle in degrees.
- `viewportSize`: The size of the viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/unprojectpoint:ontoplanewithtransform:viewrotationangle:viewportsize:)*