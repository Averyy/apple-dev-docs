# SPRect3DUnapplyScaledPose

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a rectangle that’s transformed by the inverse of the specified scaled pose.

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
static SPRect3D SPRect3DUnapplyScaledPose(SPRect3D rect, SPScaledPose3D pose);
```

## See Also

### Transforming a 3D rectangle structure
- [func rotated(by: Rotation3D, around: Point3D) -> Rect3D](./rect3d/rotated%28by,around%29-3ih62.md)
  Returns a rectangle that results from applying the specified rotation around a pivot point.
- [func rotated(by: simd_quatd, around: Point3D) -> Rect3D](./rect3d/rotated%28by,around%29-8g1c9.md)
  Returns a rectangle that results from rotating with the specified quaternion around a pivot point.
- [SPRect3DApplyAffineTransform](./sprect3dapplyaffinetransform.md)
  Returns a rectangle that results from applying the specified affine transform.
- [SPRect3DApplyPose](./sprect3dapplypose.md)
  Returns a rectangle that results from applying the specified pose.
- [SPRect3DApplyProjectiveTransform](./sprect3dapplyprojectivetransform.md)
- [SPRect3DApplyScaledPose](./sprect3dapplyscaledpose.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [SPRect3DRotate](./sprect3drotate.md)
  Returns a rectangle that results from applying the specified rotation.
- [SPRect3DRotateByQuaternion](./sprect3drotatebyquaternion.md)
  Returns a rectangle that results from rotating with the specified quaternion.
- [SPRect3DScaleBy](./sprect3dscaleby.md)
  Returns a rectangle that results from scaling with the specified double-precision values.
- [SPRect3DScaleBySize](./sprect3dscalebysize.md)
  Returns a rectangle that results from scaling with the specified size structure.
- [SPRect3DScaleUniform](./sprect3dscaleuniform.md)
  Returns a rectangle that results from uniformly scaling with the specified double-precision value.
- [SPRect3DShear](./sprect3dshear.md)
  Returns a rectangle that results from shearing over an axis by shear factors for the other two axes.
- [SPRect3DTranslate](./sprect3dtranslate-88ujj.md)
  Returns a rectangle with an origin that’s offset by the specified vector.
- [SPRect3DTranslate](./sprect3dtranslate-8amf1.md)
  Returns a rectangle with an origin that’s offset by the specified size.
- [SPRect3DUnapplyAffineTransform](./sprect3dunapplyaffinetransform.md)
  Returns a rectangle that results from unapplying the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dunapplyscaledpose)*