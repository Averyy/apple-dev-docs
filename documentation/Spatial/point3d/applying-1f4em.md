# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a point that’s transformed by the specified scaled pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
func applying(_ scaledPose: ScaledPose3D) -> Point3D
```

## See Also

- [func applying(Pose3D) -> Point3D](point3d/applying(_:)-7ulww.md)
  Returns a point that results from applying the specified pose.
- [func clamp(to: Rect3D)](point3d/clamp(to:).md)
  Clamps the mutable point to the specified rectangle.
- [func scale(by: Double)](point3d/scale(by:).md)
- [func rotated(by: Rotation3D, around: Point3D) -> Point3D](point3d/rotated(by:around:)-4tmfq.md)
  Returns a point that results from applying a rotation around the specified point.
- [func rotated(by: simd_quatd, around: Point3D) -> Point3D](point3d/rotated(by:around:)-chuy.md)
  Returns a point that results from rotating with a quaternion around the specified point.
- [func unapplying(Pose3D) -> Point3D](point3d/unapplying(_:)-5hk6t.md)
  Returns a point that results from unapplying the specified pose.
- [func unapplying(ScaledPose3D) -> Point3D](point3d/unapplying(_:)-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Point3D](point3d/unapplying(_:)-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/applying(_:)-1f4em)*