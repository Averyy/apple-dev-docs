# SPSize3DApplyScaledPose

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a size that’s transformed by the specified scaled pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static SPSize3D SPSize3DApplyScaledPose(SPSize3D size, SPScaledPose3D pose);
```

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
- [SPSize3DApplyProjectiveTransform](./spsize3dapplyprojectivetransform.md)
  Returns a size that results from applying the specified projective transform.
- [SPSize3DUnapplyAffineTransform](./spsize3dunapplyaffinetransform.md)
  Returns a size that results from unapplying the specified affine transform.
- [SPSize3DUnapplyProjectiveTransform](./spsize3dunapplyprojectivetransform.md)
  Returns a size that results from unapplying the specified projective transform.
- [SPSize3DScaleBy](./spsize3dscaleby.md)
  Returns a size that results from scaling with the specified double-precision values.
- [SPSize3DShear](./spsize3dshear.md)
  Returns a size that results from shearing over an axis by shear factors for the other two axes.
- [SPSize3DUnapplyScaledPose](./spsize3dunapplyscaledpose.md)
  Returns a size that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dapplyscaledpose)*