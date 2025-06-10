# init(scale:rotation:translation:)

**Framework**: Spatial  
**Kind**: init

Creates a projective transform from the specified scale, rotate, and translate transforms.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(scale: Size3D = Size3D(width: 1.0, height: 1, depth: 1), rotation: Rotation3D = .zero, translation: Vector3D = .zero)
```

## Parameters

- `scale`: A size structure that specifies the scale.
- `rotation`: A rotation structure that specifies the rotation.
- `translation`: A vector that specifies the translation.

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
- [init(shear: AxisWithFactors)](projectivetransform3d/init(shear:).md)
  Creates a projective transform from the specified shear transform.
- [init(leftTangent: Double, rightTangent: Double, topTangent: Double, bottomTangent: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(lefttangent:righttangent:toptangent:bottomtangent:nearz:farz:reversez:).md)
  Returns a projective transform from tangents for each side of its frustum.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double)](projectivetransform3d/init(fovy:aspectratio:nearz:farz:).md)
  Returns a projective transform with right-hand side perspective.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](projectivetransform3d/init(fovy:aspectratio:nearz:farz:reversez:).md)
- [init(scaledPose: ScaledPose3D)](projectivetransform3d/init(scaledpose:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/init(scale:rotation:translation:)-4h5wm)*