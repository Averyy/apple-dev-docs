# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a rectangle that results from applying the specified pose.

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
func applying(_ pose: Pose3D) -> Rect3D
```

## Parameters

- `pose`: The pose that the function applies to the rectangle.

## See Also

- [func applying(ScaledPose3D) -> Rect3D](rect3d/applying(_:)-5hnif.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Rect3D](rect3d/applying(_:)-5hnif.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [func rotated(by: Rotation3D, around: Point3D) -> Rect3D](rect3d/rotated(by:around:)-3ih62.md)
  Returns a rectangle that results from applying the specified rotation around a pivot point.
- [func rotated(by: simd_quatd, around: Point3D) -> Rect3D](rect3d/rotated(by:around:)-8g1c9.md)
  Returns a rectangle that results from rotating with the specified quaternion around a pivot point.
- [func scaledBy(x: Double, y: Double, z: Double) -> Rect3D](rect3d/scaledby(x:y:z:).md)
  Returns a rectangle that results from scaling with the specified double-precision values.
- [func sheared(AxisWithFactors) -> Rect3D](rect3d/sheared(_:).md)
  Returns a rectangle that results from shearing over an axis by shear factors for the other two axes.
- [func unapplying(ProjectiveTransform3D) -> Rect3D](rect3d/unapplying(_:)-1j6g7.md)
  Returns a rectangle that results from unapplying the specified projective transform.
- [func unapplying(ScaledPose3D) -> Rect3D](rect3d/unapplying(_:)-1pbfn.md)
  Returns a rectangle that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(Pose3D) -> Rect3D](rect3d/unapplying(_:)-2he5i.md)
  Returns a rectangle that results from unapplying the specified pose.
- [func unapplying(AffineTransform3D) -> Rect3D](rect3d/unapplying(_:)-7eglq.md)
  Returns a rectangle that results from unapplying the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/applying(_:)-3qdiy)*