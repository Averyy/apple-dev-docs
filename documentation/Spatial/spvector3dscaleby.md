# SPVector3DScaleBy

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a vector that results from scaling with the specified double-precision values.

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
static SPVector3D SPVector3DScaleBy(SPVector3D vector, double x, double y, double z);
```

## See Also

### Transforming a vector
- [SPVector3DApplyAffineTransform](./spvector3dapplyaffinetransform.md)
  Returns a vector that results from applying the specified affine transform.
- [SPVector3DApplyProjectiveTransform](./spvector3dapplyprojectivetransform.md)
  Returns a vector that results from applying the specified projective transform.
- [SPVector3DApplyPose](./spvector3dapplypose.md)
  Returns a vector that results from applying the specified pose.
- [SPVector3DUnapplyAffineTransform](./spvector3dunapplyaffinetransform.md)
  Returns a vector that results from unapplying the specified affine transform.
- [SPVector3DUnapplyProjectiveTransform](./spvector3dunapplyprojectivetransform.md)
  Returns a vector that results from unapplying the specified projective transform.
- [SPVector3DUnapplyPose](./spvector3dunapplypose.md)
  Returns a vector that results from unapplying the specified pose.
- [SPVector3DRotate](./spvector3drotate.md)
  Returns a vector that results from applying the specified rotation.
- [SPVector3DRotateByQuaternion](./spvector3drotatebyquaternion.md)
  Returns a vector that results from rotating with the specified quaternion.
- [SPVector3DScaleBySize](./spvector3dscalebysize.md)
  Returns a vector that results from scaling with the specified size structure.
- [SPVector3DScaleUniform](./spvector3dscaleuniform.md)
  Returns a vector that results from uniformly scaling with the specified double-precision value.
- [SPVector3DShear](./spvector3dshear.md)
  Returns a vector that results from shearing over an axis by shear factors for the other two axes.
- [SPVector3DApplyScaledPose](./spvector3dapplyscaledpose.md)
  Returns a vector that’s transformed by the specified scaled pose.
- [SPVector3DUnapplyScaledPose](./spvector3dunapplyscaledpose.md)
  Returns a vector that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3dscaleby)*