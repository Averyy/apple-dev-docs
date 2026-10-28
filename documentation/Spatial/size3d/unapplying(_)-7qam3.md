# unapplying(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a size that results from unapplying the specified affine transform.

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
func unapplying(_ transform: AffineTransform3D) -> Size3D
```

## Return Value

The size that results from unapplying the specified affine transform.

## Parameters

- `transform`: The affine transform that the function unapplies to the size.

## See Also

### Transforming a 3D size structure
- [func applying(Pose3D) -> Size3D](./applying%28_%29-85mlm.md)
  Returns a size that results from applying the specified pose.
- [func applying(ScaledPose3D) -> Size3D](./applying%28_%29-7e2pf.md)
  Returns a size that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Size3D](./applying%28_%29-85mlm.md)
  Returns a size that results from applying the specified pose.
- [func unapplying(ProjectiveTransform3D) -> Size3D](./unapplying%28_%29-yock.md)
  Returns a size that results from unapplying the specified projective transform.
- [func unapplying(Pose3D) -> Size3D](./unapplying%28_%29-3ip2e.md)
  Returns a size that results from unapplying the specified pose.
- [func sheared(AxisWithFactors) -> Size3D](./sheared%28_%29.md)
  Returns a size that results from shearing over an axis by shear factors for the other two axes.
- [func applying(ScaledPose3D) -> Size3D](./applying%28_%29-7e2pf.md)
  Returns a size that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Size3D](./unapplying%28_%29-42rsa.md)
  Returns a size that’s transformed by the inverse of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3d/unapplying(_:)-7qam3)*