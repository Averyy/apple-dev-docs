# SPSize3DApplyProjectiveTransform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a size that results from applying the specified projective transform.

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
static SPSize3D SPSize3DApplyProjectiveTransform(SPSize3D size, SPProjectiveTransform3D transform);
```

#### Return Value

The size that results from applying the specified projective transform.

## Parameters

- `size`: The size object to transform.
- `transform`: The projective transform that the function applies to the size.

## See Also

### Transforming a 3D size structure
- [SPSize3DScaleBySize](./spsize3dscalebysize.md)
  Returns a size that results from scaling with the specified size structure.
- [SPSize3DScaleUniform](./spsize3dscaleuniform.md)
  Returns a size that results from uniformly scaling with the specified double-precision value.
- [SPSize3DRotate](./spsize3drotate.md)
  Returns a size that results from applying the specified rotation.
- [SPSize3DRotateByQuaternion](./spsize3drotatebyquaternion.md)
  Returns a size that results from rotating with the specified quaternion.
- [SPSize3DApplyPose](./spsize3dapplypose.md)
  Returns a size that results from applying the specified pose.
- [SPSize3DUnapplyPose](./spsize3dunapplypose.md)
  Returns a size that results from unapplying the specified pose.
- [SPSize3DApplyAffineTransform](./spsize3dapplyaffinetransform.md)
  Returns a size that results from applying the specified affine transform.
- [SPSize3DUnapplyAffineTransform](./spsize3dunapplyaffinetransform.md)
  Returns a size that results from unapplying the specified affine transform.
- [SPSize3DUnapplyProjectiveTransform](./spsize3dunapplyprojectivetransform.md)
  Returns a size that results from unapplying the specified projective transform.
- [SPSize3DScaleBy](./spsize3dscaleby.md)
  Returns a size that results from scaling with the specified double-precision values.
- [SPSize3DShear](./spsize3dshear.md)
  Returns a size that results from shearing over an axis by shear factors for the other two axes.
- [SPSize3DApplyScaledPose](./spsize3dapplyscaledpose.md)
  Returns a size that’s transformed by the specified scaled pose.
- [SPSize3DUnapplyScaledPose](./spsize3dunapplyscaledpose.md)
  Returns a size that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dapplyprojectivetransform)*