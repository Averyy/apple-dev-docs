# SPPoint3DApplyProjectiveTransform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a point that results from applying the specified projective transform.

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
static SPPoint3D SPPoint3DApplyProjectiveTransform(SPPoint3D point, SPProjectiveTransform3D transform);
```

## Return Value

The point that results from applying the specified projective transform.

## Parameters

- `point`: The point to transform.
- `transform`: The projective transform that the function applies to the point.

## See Also

### Transforming a 3D point structure
- [SPPoint3DApplyAffineTransform](./sppoint3dapplyaffinetransform.md)
  Returns a point that results from applying the specified affine transform.
- [SPPoint3DApplyPose](./sppoint3dapplypose.md)
  Returns a point that results from applying the specified pose.
- [SPPoint3DApplyScaledPose](./sppoint3dapplyscaledpose.md)
  Returns a point that’s transformed by the specified scaled pose.
- [SPPoint3DRotate](./sppoint3drotate.md)
  Returns a point that results from applying the specified rotation.
- [func rotated(by: Rotation3D, around: Point3D) -> Point3D](./point3d/rotated%28by,around%29-4tmfq.md)
  Returns a point that results from applying a rotation around the specified point.
- [SPPoint3DRotateByQuaternion](./sppoint3drotatebyquaternion.md)
  Returns a point that results from rotating with the specified quaternion.
- [func rotated(by: simd_quatd, around: Point3D) -> Point3D](./point3d/rotated%28by,around%29-chuy.md)
  Returns a point that results from rotating with a quaternion around the specified point.
- [SPPoint3DTranslate](./sppoint3dtranslate-8xo6b.md)
  Returns a point with an origin that’s offset by the specified size.
- [SPPoint3DTranslate](./sppoint3dtranslate-9aj4h.md)
  Returns a point with an origin that’s offset by the specified vector.
- [SPPoint3DUnapplyAffineTransform](./sppoint3dunapplyaffinetransform.md)
  Returns a point that results from unapplying the specified affine transform.
- [SPPoint3DUnapplyPose](./sppoint3dunapplypose.md)
  Returns a point that results from unapplying the specified pose.
- [SPPoint3DUnapplyProjectiveTransform](./sppoint3dunapplyprojectivetransform.md)
  Returns a point that results from unapplying the specified projective transform.
- [SPPoint3DUnapplyScaledPose](./sppoint3dunapplyscaledpose.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dapplyprojectivetransform)*