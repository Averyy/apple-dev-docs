# SPRay3DTranslate

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a ray with an origin that’s offset by the specified size.

**Availability**:
- iOS 16.0+ - Deprecated in 16.0
- iPadOS 16.0+ - Deprecated in 16.0
- Mac Catalyst 16.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 13.0
- tvOS 16.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 9.0

> **Deprecated**: Use `Vector3D` variant.

## Declaration

```c
static SPRay3D SPRay3DTranslate(SPRay3D ray, SPSize3D offset);
```

#### Return Value

The ray with an origin that’s offset by the specified size.

## Parameters

- `ray`: The ray to translate.
- `offset`: The size that defines the translation.

## See Also

### Transforming a 3D ray structure
- [SPRay3DApplyAffineTransform](./spray3dapplyaffinetransform.md)
  Returns a ray that results from applying the specified affine transform.
- [SPRay3DApplyProjectiveTransform](./spray3dapplyprojectivetransform.md)
  Returns a ray that results from applying the specified projective transform.
- [SPRay3DTranslate](./spray3dtranslate-2t6zr.md)
  Returns a ray with an origin that’s offset by the specified vector.
- [SPRay3DApplyPose](./spray3dapplypose.md)
  Returns a ray that results from applying the specified pose.
- [SPRay3DUnapplyAffineTransform](./spray3dunapplyaffinetransform.md)
  Returns a ray that results from unapplying the specified affine transform.
- [SPRay3DUnapplyProjectiveTransform](./spray3dunapplyprojectivetransform.md)
  Returns a ray that results from unapplying the specified projective transform.
- [SPRay3DUnapplyPose](./spray3dunapplypose.md)
  Returns a ray that results from unapplying the specified projective transform.
- [SPRay3DRotate](./spray3drotate.md)
  Returns a ray that results from applying the specified rotation.
- [SPRay3DRotateAroundPoint](./spray3drotatearoundpoint.md)
  Returns a ray that’s rotated by the specified rotation around a specified pivot.
- [SPRay3DRotateByQuaternion](./spray3drotatebyquaternion.md)
  Returns a ray that results from rotating with the specified quaternion.
- [SPRay3DRotateByQuaternionAroundPoint](./spray3drotatebyquaternionaroundpoint.md)
  Returns a ray that’s rotated by the specified quaternion around a specified pivot.
- [SPRay3DApplyScaledPose](./spray3dapplyscaledpose.md)
  Returns a ray that’s transformed by the specified scaled pose.
- [SPRay3DUnapplyScaledPose](./spray3dunapplyscaledpose.md)
  Returns a ray that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dtranslate-13y4m)*