# init(_:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a projective transform from the specified 4 x 4 single-precision matrix.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(_ matrix: simd_float4x4)
```

## Parameters

- `matrix`: The source single-precision matrix.

## See Also

### Creating a 3D projective transform structure
- [init()](./init%28%29-1clia.md)
  Creates a projective transform.
- [init()](./init%28%29-6c4f4.md)
  Returns a new identity projective transform.
- [init(simd_double4x4)](./init%28_%29-6g88l.md)
  Creates a projective transform from the specified double-precision matrix.
- [init(matrix: simd_double4x4)](./init%28matrix%29-8eg5x.md)
  Creates a projective transform from the specified 4 x 4 double-precision matrix.
- [init(AffineTransform3D)](./init%28_%29-9t2jh.md)
  Creates a projective transform from the specified affine transform.
- [init(pose: Pose3D)](./init%28pose%29.md)
  Creates a projective transform from the specified pose structure.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](./init%28scale,rotation,translation%29-4h5wm.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](./init%28shear%29.md)
  Creates a projective transform from the specified shear transform.
- [init(leftTangent: Double, rightTangent: Double, topTangent: Double, bottomTangent: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./init%28lefttangent,righttangent,toptangent,bottomtangent,nearz,farz,reversez%29.md)
  Returns a projective transform from tangents for each side of its frustum.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double)](./init%28fovy,aspectratio,nearz,farz%29.md)
  Returns a projective transform with right-hand side perspective.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./init%28fovy,aspectratio,nearz,farz,reversez%29.md)
- [init(scaledPose: ScaledPose3D)](./init%28scaledpose%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(_:)-7b2bq)*