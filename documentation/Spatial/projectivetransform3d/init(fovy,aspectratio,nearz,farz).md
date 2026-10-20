# init(fovY:aspectRatio:nearZ:farZ:)

**Framework**: Spatial  
**Kind**: init

Returns a projective transform with right-hand side perspective.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double)
```

#### Discussion

- fovyRadians: The field-of-view angle along the y-axis.
- aspectRatio: The aspect ratio.
- nearZ: The distance to the near clipping plane.
- farZ: The distance to the far clipping plane.

## See Also

- [init()](projectivetransform3d/init-1clia.md)
  Creates a projective transform.
- [init()](projectivetransform3d/init-6c4f4.md)
  Returns a new identity projective transform.
- [init(simd_float4x4)](projectivetransform3d/init(_:)-7b2bq.md)
  Creates a projective transform from the specified 4 x 4 single-precision matrix.
- [init(simd_double4x4)](projectivetransform3d/init(_:)-6g88l.md)
  Creates a projective transform from the specified double-precision matrix.
- [init(matrix: simd_double4x4)](projectivetransform3d/init(matrix:)-8eg5x.md)
  Creates a projective transform from the specified 4 x 4 double-precision matrix.
- [init(AffineTransform3D)](projectivetransform3d/init(_:)-9t2jh.md)
  Creates a projective transform from the specified affine transform.
- [init(pose: Pose3D)](projectivetransform3d/init(pose:).md)
  Creates a projective transform from the specified pose structure.
- [init(scale: Size3D, rotation: Rotation3D, translation: Vector3D)](projectivetransform3d/init(scale:rotation:translation:)-4h5wm.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [init(shear: AxisWithFactors)](projectivetransform3d/init(shear:).md)
  Creates a projective transform from the specified shear transform.
- [init(leftTangent: Double, rightTangent: Double, topTangent: Double, bottomTangent: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(lefttangent:righttangent:toptangent:bottomtangent:nearz:farz:reversez:).md)
  Returns a projective transform from tangents for each side of its frustum.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(fovy:aspectratio:nearz:farz:reversez:).md)
- [init(scaledPose: ScaledPose3D)](projectivetransform3d/init(scaledpose:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(fovy:aspectratio:nearz:farz:))*