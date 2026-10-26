# rotated(by:around:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a point that results from applying a rotation around the specified point.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func rotated(by rotation: Rotation3D, around pivot: Point3D) -> Point3D
```

```c
static SPPoint3D SPPoint3DRotateAroundPoint(SPPoint3D point, SPRotation3D rotation, SPPoint3D pivot);
```

#### Return Value

The point that results from applying the specified rotation.

## Parameters

- `rotation`: A point that defines the rotation pivot.
- `pivot`: The rotation structure that defines the rotation’s angle and axis.

## See Also

### Transforming a 3D point structure
- [func applying(ScaledPose3D) -> Point3D](./applying%28_%29-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Point3D](./applying%28_%29-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Point3D](./applying%28_%29-7ulww.md)
  Returns a point that results from applying the specified pose.
- [func clamp(to: Rect3D)](./clamp%28to%29.md)
  Clamps the mutable point to the specified rectangle.
- [func scale(by: Double)](./scale%28by%29.md)
- [func rotated(by: simd_quatd, around: Point3D) -> Point3D](./rotated%28by,around%29-chuy.md)
  Returns a point that results from rotating with a quaternion around the specified point.
- [func unapplying(Pose3D) -> Point3D](./unapplying%28_%29-5hk6t.md)
  Returns a point that results from unapplying the specified pose.
- [func unapplying(ScaledPose3D) -> Point3D](./unapplying%28_%29-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Point3D](./unapplying%28_%29-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [SPPoint3DApplyAffineTransform](../sppoint3dapplyaffinetransform.md)
  Returns a point that results from applying the specified affine transform.
- [SPPoint3DApplyPose](../sppoint3dapplypose.md)
  Returns a point that results from applying the specified pose.
- [SPPoint3DApplyProjectiveTransform](../sppoint3dapplyprojectivetransform.md)
  Returns a point that results from applying the specified projective transform.
- [SPPoint3DApplyScaledPose](../sppoint3dapplyscaledpose.md)
  Returns a point that’s transformed by the specified scaled pose.
- [SPPoint3DRotate](../sppoint3drotate.md)
  Returns a point that results from applying the specified rotation.
- [SPPoint3DRotateByQuaternion](../sppoint3drotatebyquaternion.md)
  Returns a point that results from rotating with the specified quaternion.
- [SPPoint3DTranslate](../sppoint3dtranslate-8xo6b.md)
  Returns a point with an origin that’s offset by the specified size.
- [SPPoint3DTranslate](../sppoint3dtranslate-9aj4h.md)
  Returns a point with an origin that’s offset by the specified vector.
- [SPPoint3DUnapplyAffineTransform](../sppoint3dunapplyaffinetransform.md)
  Returns a point that results from unapplying the specified affine transform.
- [SPPoint3DUnapplyPose](../sppoint3dunapplypose.md)
  Returns a point that results from unapplying the specified pose.
- [SPPoint3DUnapplyProjectiveTransform](../sppoint3dunapplyprojectivetransform.md)
  Returns a point that results from unapplying the specified projective transform.
- [SPPoint3DUnapplyScaledPose](../sppoint3dunapplyscaledpose.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/rotated(by:around:)-4tmfq)*