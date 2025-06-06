# rotated(by:)

**Framework**: Spatial  
**Kind**: method

Returns a pose that results from applying the specified rotation.

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
func rotated(by rotation: Rotation3D) -> Pose3D
```

## Parameters

- `rotation`: The rotation structure that defines the rotation’s angle and axis.

## See Also

- [func concatenating(ScaledPose3D) -> ScaledPose3D](pose3d/concatenating(_:)-4esra.md)
  Returns a pose that represents the concatenation of a scaled pose and a pose.
- [func concatenating(Pose3D) -> Pose3D](pose3d/concatenating(_:)-6dd2s.md)
  Returns a pose that represents the concatenation of two poses.
- [func flip(along: Axis3D)](pose3d/flip(along:).md)
  Flips a pose along the specified axis.
- [func flipped(along: Axis3D) -> Pose3D](pose3d/flipped(along:).md)
  Returns a pose that results from flipping it along the specified axis.
- [func rotated(by: simd_quatd) -> Pose3D](pose3d/rotated(by:)-10k2a.md)
  Returns a pose that results from rotating with the specified quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/rotated(by:)-377u)*