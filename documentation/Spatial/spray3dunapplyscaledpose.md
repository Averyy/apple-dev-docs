# SPRay3DUnapplyScaledPose

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a ray that’s transformed by the inverse of the specified scaled pose.

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
static SPRay3D SPRay3DUnapplyScaledPose(SPRay3D ray, SPScaledPose3D pose);
```

## See Also

### Transforming a 3D ray structure
- [SPRay3DApplyAffineTransform](./spray3dapplyaffinetransform.md)
  Returns a ray that results from applying the specified affine transform.
- [SPRay3DApplyProjectiveTransform](./spray3dapplyprojectivetransform.md)
  Returns a ray that results from applying the specified projective transform.
- [SPRay3DTranslate](./spray3dtranslate-13y4m.md)
  Returns a ray with an origin that’s offset by the specified size.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dunapplyscaledpose)*