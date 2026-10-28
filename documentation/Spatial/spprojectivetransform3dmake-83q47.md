# SPProjectiveTransform3DMake

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPProjectiveTransform3D SPProjectiveTransform3DMake(SPSize3D scale, SPRotation3D rotation, SPVector3D translation);
```

## Return Value

A new affine transform structure.

## Discussion

Returns a new scale, rotate, translate affine transform.

## Parameters

- `scale`: The scale.
- `rotation`: The rotation.
- `translation`: The translation.

## See Also

### Creating a 3D projective transform structure
- [init(simd_double4x4)](./projectivetransform3d/init%28_%29-6g88l.md)
  Creates a projective transform from the specified double-precision matrix.
- [init(AffineTransform3D)](./projectivetransform3d/init%28_%29-9t2jh.md)
  Creates a projective transform from the specified affine transform.
- [init(leftTangent: Double, rightTangent: Double, topTangent: Double, bottomTangent: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./projectivetransform3d/init%28lefttangent,righttangent,toptangent,bottomtangent,nearz,farz,reversez%29.md)
  Returns a projective transform from tangents for each side of its frustum.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double)](./projectivetransform3d/init%28fovy,aspectratio,nearz,farz%29.md)
  Returns a projective transform with right-hand side perspective.
- [init(fovY: Angle2D, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./projectivetransform3d/init%28fovy,aspectratio,nearz,farz,reversez%29.md)
- [SPProjectiveTransform3DMake](./spprojectivetransform3dmake-6aldt.md)
  Creates a projective transform from the specified scale, rotate, and translate transforms.
- [SPProjectiveTransform3DMakeShear](./spprojectivetransform3dmakeshear.md)
  Creates an affine transform from the specified shear transform.
- [SPProjectiveTransform3DMakeWithPose](./spprojectivetransform3dmakewithpose.md)
  Creates a projective transform from the specified pose structure.
- [SPProjectiveTransform3DMakeWithScaledPose](./spprojectivetransform3dmakewithscaledpose.md)
  Returns a new projective transform structure from the specified scaled pose structure.
- [SPProjectiveTransform3DMakeWithRHPerspective](./spprojectivetransform3dmakewithrhperspective-97qwp.md)
  Returns a projective transform with right-hand side perspective.
- [SPProjectiveTransform3DMakeWithRHPerspective](./spprojectivetransform3dmakewithrhperspective-9gl97.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dmake-83q47)*