# apply(_:)

**Framework**: Spatial  
**Kind**: method

Applies the specified pose to the ray.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
mutating func apply(_ pose: Pose3D)
```

## Parameters

- `pose`: The pose that the function applies to the ray.

## See Also

- [func applying(AffineTransform3D) -> Ray3D](ray3d/applying(_:)-337n0.md)
  Returns a ray that results from applying the specified affine transform.
- [func applying(ProjectiveTransform3D) -> Ray3D](ray3d/applying(_:)-2aom9.md)
  Returns a ray that results from applying the specified projective transform.
- [func applying(Pose3D) -> Ray3D](ray3d/applying(_:)-34rqi.md)
  Returns a ray that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Ray3D](ray3d/unapplying(_:)-7bc37.md)
  Returns a ray that results from unapplying the specified affine transform.
- [func unapplying(ProjectiveTransform3D) -> Ray3D](ray3d/unapplying(_:)-6tj2w.md)
  Returns a ray that results from unapplying the specified projective transform.
- [func unapplying(Pose3D) -> Ray3D](ray3d/unapplying(_:)-928o9.md)
  Unapplies the specified pose to the ray.
- [func rotated(by: Rotation3D) -> Ray3D](ray3d/rotated(by:)-qxp0.md)
  Returns a ray that results from applying the specified rotation.
- [func rotated(by: simd_quatd) -> Ray3D](ray3d/rotated(by:)-81glv.md)
  Returns a ray that results from rotating with the specified quaternion.
- [func rotated(by: simd_quatd, around: Point3D) -> Ray3D](ray3d/rotated(by:around:)-uzon.md)
  Returns a ray that’s rotated by the specified quaternion around a specified pivot.
- [func rotated(by: Rotation3D, around: Point3D) -> Ray3D](ray3d/rotated(by:around:)-7h43.md)
  Returns a ray that’s rotated by the specified rotation around a specified pivot.
- [func applying(ScaledPose3D) -> Ray3D](ray3d/applying(_:)-6hfqw.md)
  Returns a ray that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Ray3D](ray3d/unapplying(_:)-9x164.md)
  Returns a ray that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/apply(_:))*