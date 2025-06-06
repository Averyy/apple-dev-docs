# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a size that results from unapplying the specified pose.

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
func unapplying(_ pose: Pose3D) -> Size3D
```

## Parameters

- `pose`: The pose that the function unapplies to the size.

## See Also

- [func applying(Pose3D) -> Size3D](size3d/applying(_:)-85mlm.md)
  Returns a size that results from applying the specified pose.
- [func applying(ScaledPose3D) -> Size3D](size3d/applying(_:)-7e2pf.md)
  Returns a size that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Size3D](size3d/applying(_:)-85mlm.md)
  Returns a size that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Size3D](size3d/unapplying(_:)-7qam3.md)
  Returns a size that results from unapplying the specified affine transform.
- [func unapplying(ProjectiveTransform3D) -> Size3D](size3d/unapplying(_:)-yock.md)
  Returns a size that results from unapplying the specified projective transform.
- [func sheared(AxisWithFactors) -> Size3D](size3d/sheared(_:).md)
  Returns a size that results from shearing over an axis by shear factors for the other two axes.
- [func applying(ScaledPose3D) -> Size3D](size3d/applying(_:)-7e2pf.md)
  Returns a size that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Size3D](size3d/unapplying(_:)-42rsa.md)
  Returns a size that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3d/unapplying(_:)-3ip2e)*