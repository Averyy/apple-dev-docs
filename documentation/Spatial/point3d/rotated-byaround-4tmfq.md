# rotated(by:around:)

**Framework**: Spatial  
**Kind**: method

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

#### Return Value

The point that results from applying the specified rotation.

## Parameters

- `rotation`: A point that defines the rotation pivot.
- `pivot`: The rotation structure that defines the rotation’s angle and axis.

## See Also

- [func applying(ScaledPose3D) -> Point3D](point3d/applying(_:)-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Point3D](point3d/applying(_:)-1f4em.md)
  Returns a point that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Point3D](point3d/applying(_:)-7ulww.md)
  Returns a point that results from applying the specified pose.
- [func clamp(to: Rect3D)](point3d/clamp(to:).md)
  Clamps the mutable point to the specified rectangle.
- [func clamped(to: Rect3D) -> Point3D](point3d/clamped(to:).md)
  Returns a point with coordinates that clamp to the specified rectangle.
- [func scale(by: Double)](point3d/scale(by:).md)
- [func rotated(by: simd_quatd, around: Point3D) -> Point3D](point3d/rotated(by:around:)-chuy.md)
  Returns a point that results from rotating with a quaternion around the specified point.
- [func unapplying(Pose3D) -> Point3D](point3d/unapplying(_:)-5hk6t.md)
  Returns a point that results from unapplying the specified pose.
- [func unapplying(ScaledPose3D) -> Point3D](point3d/unapplying(_:)-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Point3D](point3d/unapplying(_:)-7wdtv.md)
  Returns a point that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/rotated(by:around:)-4tmfq)*