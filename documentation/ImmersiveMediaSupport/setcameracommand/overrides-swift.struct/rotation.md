# rotation

**Framework**: Immersive Media Support  
**Kind**: property

Camera rotation to override the rotation in [`pose`](immersivecamera/pose.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var rotation: Rotation3DFloat? { get set }
```

#### Discussion

This rotation is applied uniformly to both eyes of a stereo frame as an image reorientation. It does not remap eye assignment, reproject parallax, or account for the stereo baseline encoded in the source video.

For stereo content, only rotations that keep the stereo baseline horizontal in viewer space produce comfortable fusion:

- **Yaw** (rotation about the viewer-up axis) — safe at any magnitude, though yaw angles approaching ±180° invert the parallax sign (depth appears reversed).
- **Pitch** (rotation about the camera’s local right / baseline axis) — safe at any magnitude; the baseline is the rotation axis and remains invariant.
- **Roll** (rotation about the camera-forward axis) — rotates the baseline out of horizontal, creating vertical disparity between eyes. Small roll angles cause eye strain; larger angles (≥ a few degrees) prevent fusion entirely.
- Any mixed rotation that decomposes to a non-zero roll component exhibits the same failure proportional to the roll magnitude.

For mono content there are no stereo constraints and the full rotation space is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/overrides-swift.struct/rotation)*