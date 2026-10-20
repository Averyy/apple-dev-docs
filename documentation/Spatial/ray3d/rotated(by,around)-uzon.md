# rotated(by:around:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a ray that’s rotated by the specified quaternion around a specified pivot.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
func rotated(by quaternion: simd_quatd, around pivot: Point3D) -> Ray3D
```

## Parameters

- `quaternion`: The quaternion that defines the rotation.
- `pivot`: The center of the rotation.

## See Also

### Transforming a 3D ray structure
- [func apply(Pose3D)](./apply%28_%29.md)
  Applies the specified pose to the ray.
- [func applying(AffineTransform3D) -> Ray3D](./applying%28_%29-337n0.md)
  Returns a ray that results from applying the specified affine transform.
- [func applying(ProjectiveTransform3D) -> Ray3D](./applying%28_%29-2aom9.md)
  Returns a ray that results from applying the specified projective transform.
- [func applying(Pose3D) -> Ray3D](./applying%28_%29-34rqi.md)
  Returns a ray that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Ray3D](./unapplying%28_%29-7bc37.md)
  Returns a ray that results from unapplying the specified affine transform.
- [func unapplying(ProjectiveTransform3D) -> Ray3D](./unapplying%28_%29-6tj2w.md)
  Returns a ray that results from unapplying the specified projective transform.
- [func unapplying(Pose3D) -> Ray3D](./unapplying%28_%29-928o9.md)
  Unapplies the specified pose to the ray.
- [func rotated(by: Rotation3D) -> Ray3D](./rotated%28by%29-qxp0.md)
  Returns a ray that results from applying the specified rotation.
- [func rotated(by: simd_quatd) -> Ray3D](./rotated%28by%29-81glv.md)
  Returns a ray that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D, around: Point3D) -> Ray3D](./rotated%28by,around%29-7h43.md)
  Returns a ray that’s rotated by the specified rotation around a specified pivot.
- [func applying(ScaledPose3D) -> Ray3D](./applying%28_%29-6hfqw.md)
  Returns a ray that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Ray3D](./unapplying%28_%29-9x164.md)
  Returns a ray that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/rotated(by:around:)-uzon)*