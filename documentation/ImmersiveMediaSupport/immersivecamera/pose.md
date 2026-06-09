# pose

**Framework**: Immersive Media Support  
**Kind**: property

The pose of this immersive camera.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var pose: Pose3DFloat
```

#### Discussion

The rotation component of the pose is applied uniformly to both eyes of a stereo frame as an image reorientation. It does not remap eye assignment, reproject parallax, or account for the stereo baseline encoded in the source video.

For stereo (`stereoCamera`) content, only rotations that keep the stereo baseline horizontal in viewer space produce comfortable fusion:

- **Yaw** (rotation about the viewer-up axis) — safe at any magnitude, though yaw angles approaching ±180° invert the parallax sign (depth appears reversed).
- **Pitch** (rotation about the camera’s local right / baseline axis) — safe at any magnitude; the baseline is the rotation axis and remains invariant.
- **Roll** (rotation about the camera-forward axis) — rotates the baseline out of horizontal, creating vertical disparity between eyes. Small roll angles cause eye strain; larger angles (≥ a few degrees) prevent fusion entirely. A 90° roll makes the baseline orthogonal to the viewer’s eye baseline and breaks fusion completely.
- Any mixed rotation that decomposes to a non-zero roll component exhibits the same failure proportional to the roll magnitude.

For mono content there are no stereo constraints and the full rotation space is valid.

## See Also

- [var calibration: ImmersiveCameraCalibration](immersivecamera/calibration.md)
  Calibration details for this camera.
- [var id: String](immersivecamera/id.md)
  A unique and non empty identifier string for this immersive camera.
- [var presentationFrameRate: Int](immersivecamera/presentationframerate.md)
  Presentation frame rate suited for this immersive camera.
- [var type: ImmersiveCamera.CameraType](immersivecamera/type.md)
  Represents the type of the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamera/pose)*