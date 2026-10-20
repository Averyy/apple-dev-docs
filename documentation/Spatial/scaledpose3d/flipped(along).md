# flipped(along:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a scaled pose that results from flipping it along the specified axis.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
func flipped(along axis: Axis3D) -> ScaledPose3D
```

## See Also

### Transforming a 3D scaled-pose structure
- [func flip(along: Axis3D)](./flip%28along%29.md)
  Flips a scaled pose along the specified axis.
- [func rotated(by: simd_quatd) -> ScaledPose3D](./rotated%28by%29-5mxbl.md)
  Returns a scaled pose that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D) -> ScaledPose3D](./rotated%28by%29-x75b.md)
  Returns a scaled pose that results from applying the specified rotation.
- [func concatenating(ScaledPose3D) -> ScaledPose3D](./concatenating%28_%29-c38k.md)
  Returns a scaled pose that represents the concatenation of two scaled poses.
- [func concatenating(Pose3D) -> ScaledPose3D](./concatenating%28_%29-2xzgs.md)
  Returns a scaled pose that represents the concatenation of two poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/flipped(along:))*