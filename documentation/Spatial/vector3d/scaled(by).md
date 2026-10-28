# scaled(by:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns the vector scaled by the specified size.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func scaled(by size: Size3D) -> Vector3D
```

## Discussion

- Returns The scaled vector.

## Parameters

- `size`: The size structure that defines that scale.

## See Also

### Transforming a vector
- [func applying(AffineTransform3D) -> Vector3D](./applying%28_%29-1d0mh.md)
  Returns the vector that results from applying an affine transform to the vector.
- [func applying(ProjectiveTransform3D) -> Vector3D](./applying%28_%29-5y3xb.md)
  Returns the vector that results from applying a projective transform to the vector.
- [func applying(Pose3D) -> Vector3D](./applying%28_%29-4k2qi.md)
  Returns a vector that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Vector3D](./unapplying%28_%29-6vl3o.md)
  Returns the vector that results from unapplying an affine transform to the vector.
- [func unapplying(ProjectiveTransform3D) -> Vector3D](./unapplying%28_%29-8ookb.md)
  Returns the vector that results from unapplying a projective transform to the vector.
- [func unapplying(Pose3D) -> Vector3D](./unapplying%28_%29-1gzyd.md)
  Returns a vector that results from unapplying the specified pose.
- [func rotated(by: Rotation3D) -> Vector3D](./rotated%28by%29-2gcq4.md)
  Returns the vector rotated by the specified rotation around the origin.
- [func rotated(by: simd_quatd) -> Vector3D](./rotated%28by%29-8bwna.md)
  Returns the vector rotated by the specified quaternion around the origin.
- [func scaledBy(x: Double, y: Double, z: Double) -> Vector3D](./scaledby%28x,y,z%29.md)
  Returns a vector that results from scaling with the specified double-precision values.
- [func uniformlyScaled(by: Double) -> Vector3D](./uniformlyscaled%28by%29.md)
  Returns the entity uniformly scaled by the specified scalar value.
- [func sheared(AxisWithFactors) -> Vector3D](./sheared%28_%29.md)
  Returns a vector that results from shearing over an axis by shear factors for the other two axes.
- [func applying(ScaledPose3D) -> Vector3D](./applying%28_%29-8fn6a.md)
  Returns a vector that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Vector3D](./unapplying%28_%29-4uxr2.md)
  Returns a vector that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/scaled(by:))*