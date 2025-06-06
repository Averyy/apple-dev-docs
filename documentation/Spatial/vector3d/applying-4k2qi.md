# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a vector that results from applying the specified pose.

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
func applying(_ pose: Pose3D) -> Vector3D
```

## Parameters

- `pose`: The pose that the function applies to the vector.

## See Also

- [func applying(AffineTransform3D) -> Vector3D](vector3d/applying(_:)-1d0mh.md)
  Returns the vector resulting from applying an affine transform to the vector.
- [func applying(ProjectiveTransform3D) -> Vector3D](vector3d/applying(_:)-5y3xb.md)
  Returns the vector resulting from applying a projective transform to the vector.
- [func unapplying(AffineTransform3D) -> Vector3D](vector3d/unapplying(_:)-6vl3o.md)
  Returns the vector resulting from unapplying an affine transform to the vector.
- [func unapplying(ProjectiveTransform3D) -> Vector3D](vector3d/unapplying(_:)-8ookb.md)
  Returns the vector resulting from unapplying a projective transform to the vector.
- [func unapplying(Pose3D) -> Vector3D](vector3d/unapplying(_:)-1gzyd.md)
  Returns a vector that results from unapplying the specified pose.
- [func rotated(by: Rotation3D) -> Vector3D](vector3d/rotated(by:)-2gcq4.md)
  Returns the vector rotated by the specified rotation around the origin.
- [func rotated(by: simd_quatd) -> Vector3D](vector3d/rotated(by:)-8bwna.md)
  Returns the vector rotated by the specified quaternion around the origin.
- [func scaled(by: Size3D) -> Vector3D](vector3d/scaled(by:).md)
  Returns the vector scaled by the specified size.
- [func scaledBy(x: Double, y: Double, z: Double) -> Vector3D](vector3d/scaledby(x:y:z:).md)
  Returns a vector that results from scaling with the specified double-precision values.
- [func uniformlyScaled(by: Double) -> Vector3D](vector3d/uniformlyscaled(by:).md)
  Returns the entity uniformly scaled by the specified scalar value.
- [func sheared(AxisWithFactors) -> Vector3D](vector3d/sheared(_:).md)
  Returns a vector that results from shearing over an axis by shear factors for the other two axes.
- [func applying(ScaledPose3D) -> Vector3D](vector3d/applying(_:)-8fn6a.md)
  Returns a vector that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Vector3D](vector3d/unapplying(_:)-4uxr2.md)
  Returns a vector that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/applying(_:)-4k2qi)*