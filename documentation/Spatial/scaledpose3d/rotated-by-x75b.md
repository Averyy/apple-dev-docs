# rotated(by:)

**Framework**: Spatial  
**Kind**: method

Returns a scaled pose that results from applying the specified rotation.

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
func rotated(by rotation: Rotation3D) -> ScaledPose3D
```

## See Also

- [func flip(along: Axis3D)](scaledpose3d/flip(along:).md)
  Flips a scaled pose along the specified axis.
- [func flipped(along: Axis3D) -> ScaledPose3D](scaledpose3d/flipped(along:).md)
  Returns a scaled pose that results from flipping it along the specified axis.
- [func rotated(by: simd_quatd) -> ScaledPose3D](scaledpose3d/rotated(by:)-5mxbl.md)
  Returns a scaled pose that results from rotating with the specified quaternion.
- [func concatenating(ScaledPose3D) -> ScaledPose3D](scaledpose3d/concatenating(_:)-c38k.md)
  Returns a scaled pose that represents the concatenation of two scaled poses.
- [func concatenating(Pose3D) -> ScaledPose3D](scaledpose3d/concatenating(_:)-2xzgs.md)
  Returns a scaled pose that represents the concatenation of two poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/rotated(by:)-x75b)*