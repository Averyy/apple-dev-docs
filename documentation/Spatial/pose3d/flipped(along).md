# flipped(along:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a pose that results from flipping it along the specified axis.

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
func flipped(along axis: Axis3D) -> Pose3D
```

## Parameters

- `axis`: An axis structure that specifies the flip axis.

## See Also

### Transforming a 3D pose structure
- [func concatenating(ScaledPose3D) -> ScaledPose3D](./concatenating%28_%29-4esra.md)
  Returns a pose that represents the concatenation of a scaled pose and a pose.
- [func concatenating(Pose3D) -> Pose3D](./concatenating%28_%29-6dd2s.md)
  Returns a pose that represents the concatenation of two poses.
- [func flip(along: Axis3D)](./flip%28along%29.md)
  Flips a pose along the specified axis.
- [func rotated(by: simd_quatd) -> Pose3D](./rotated%28by%29-10k2a.md)
  Returns a pose that results from rotating with the specified quaternion.
- [func rotated(by: Rotation3D) -> Pose3D](./rotated%28by%29-377u.md)
  Returns a pose that results from applying the specified rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/flipped(along:))*