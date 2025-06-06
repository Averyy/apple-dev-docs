# concatenating(_:)

**Framework**: Spatial  
**Kind**: method

Returns a pose that represents the concatenation of two poses.

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
func concatenating(_ transform: Pose3D) -> Pose3D
```

## Parameters

- `transform`: The second pose.

## See Also

- [func concatenating(ScaledPose3D) -> ScaledPose3D](pose3d/concatenating(_:)-4esra.md)
  Returns a pose that represents the concatenation of a scaled pose and a pose.
- [func flip(along: Axis3D)](pose3d/flip(along:).md)
  Flips a pose along the specified axis.
- [func flipped(along: Axis3D) -> Pose3D](pose3d/flipped(along:).md)
  Returns a pose that results from flipping it along the specified axis.
- [func rotated(by: simd_quatd) -> Pose3D](pose3d/rotated(by:)-10k2a.md)
  Returns a pose that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D) -> Pose3D](pose3d/rotated(by:)-377u.md)
  Returns a pose that results from applying the specified rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/concatenating(_:)-6dd2s)*