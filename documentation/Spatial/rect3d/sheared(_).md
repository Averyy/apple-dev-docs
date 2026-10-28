# sheared(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a rectangle that results from shearing over an axis by shear factors for the other two axes.

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
func sheared(_ shear: AxisWithFactors) -> Rect3D
```

## Return Value

The rectangle that results from shearing over an axis by shear factors for the other two axes.

## Parameters

- `shear`: The shear axis and factors.

## See Also

### Transforming a 3D rectangle structure
- [func applying(Pose3D) -> Rect3D](./applying%28_%29-3qdiy.md)
  Returns a rectangle that results from applying the specified pose.
- [func applying(ScaledPose3D) -> Rect3D](./applying%28_%29-5hnif.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Rect3D](./applying%28_%29-5hnif.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [func rotated(by: Rotation3D, around: Point3D) -> Rect3D](./rotated%28by,around%29-3ih62.md)
  Returns a rectangle that results from applying the specified rotation around a pivot point.
- [func rotated(by: simd_quatd, around: Point3D) -> Rect3D](./rotated%28by,around%29-8g1c9.md)
  Returns a rectangle that results from rotating with the specified quaternion around a pivot point.
- [func scaledBy(x: Double, y: Double, z: Double) -> Rect3D](./scaledby%28x,y,z%29.md)
  Returns a rectangle that results from scaling with the specified double-precision values.
- [func unapplying(ProjectiveTransform3D) -> Rect3D](./unapplying%28_%29-1j6g7.md)
  Returns a rectangle that results from unapplying the specified projective transform.
- [func unapplying(ScaledPose3D) -> Rect3D](./unapplying%28_%29-1pbfn.md)
  Returns a rectangle that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(Pose3D) -> Rect3D](./unapplying%28_%29-2he5i.md)
  Returns a rectangle that results from unapplying the specified pose.
- [func unapplying(AffineTransform3D) -> Rect3D](./unapplying%28_%29-7eglq.md)
  Returns a rectangle that results from unapplying the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/sheared(_:))*