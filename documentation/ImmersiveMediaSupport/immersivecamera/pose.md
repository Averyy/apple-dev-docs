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

The rotation component of the pose decomposes into three axis rotations, applied intrinsically in this order:

1. **Roll** — rotation around the camera’s local z-axis (the optical axis; the camera looks toward −Z).
2. **Yaw** — rotation around the camera’s (post-roll) local y-axis.
3. **Pitch** — rotation around the camera’s (post-roll, post-yaw) local x-axis (the right / baseline axis).

This matches Spatial’s `EulerAngleOrder.xyz`, which composes intrinsically as roll, then yaw, then pitch (equivalently, extrinsically as pitch, then yaw, then roll). The composition order matters — the same angle values under a different order produce a different orientation. In particular, this does **not** match `RealityKit.Transform(pitch:yaw:roll:)`, which composes intrinsically as yaw, then pitch, then roll.

##### Stereo Fusion Constraints

The rotation component is applied uniformly to both eyes as an image reorientation; it does not remap eye assignment, reproject parallax, or account for the stereo baseline encoded in the source video. For stereo (`stereoCamera`) content, only rotations that keep the stereo baseline horizontal in viewer space produce comfortable fusion:

- **Roll** — rotates the baseline out of horizontal, creating vertical disparity between eyes. Small roll angles cause eye strain; larger angles (≥ a few degrees) prevent fusion entirely.
- **Yaw** — may be safe in some circumstances but increasingly likely to cause anomalous parallax perception at larger angles.
- **Pitch** — the baseline is the rotation axis and the invariant of the rotation depends on the projection.
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