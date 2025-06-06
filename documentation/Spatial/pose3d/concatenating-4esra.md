# concatenating(_:)

**Framework**: Spatial  
**Kind**: method

Returns a pose that represents the concatenation of a scaled pose and a pose.

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
func concatenating(_ transform: ScaledPose3D) -> ScaledPose3D
```

## See Also

- [func concatenating(Pose3D) -> Pose3D](pose3d/concatenating(_:)-6dd2s.md)
  Returns a pose that represents the concatenation of two poses.
- [func flip(along: Axis3D)](pose3d/flip(along:).md)
  Flips a pose along the specified axis.
- [func flipped(along: Axis3D) -> Pose3D](pose3d/flipped(along:).md)
  Returns a pose that results from flipping it along the specified axis.
- [func rotated(by: simd_quatd) -> Pose3D](pose3d/rotated(by:)-10k2a.md)
  Returns a pose that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D) -> Pose3D](pose3d/rotated(by:)-377u.md)
  Returns a pose that results from applying the specified rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/concatenating(_:)-4esra)*