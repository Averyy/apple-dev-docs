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

The rotation decomposes into three axis rotations, applied intrinsically in this order:

1. **Roll** — rotation around the camera’s local z-axis (the optical axis; the camera looks toward −Z).
2. **Yaw** — rotation around the camera’s (post-roll) local y-axis.
3. **Pitch** — rotation around the camera’s (post-roll, post-yaw) local x-axis (the right / baseline axis).

This matches Spatial’s `EulerAngleOrder.xyz`, which composes intrinsically as roll, then yaw, then pitch (equivalently, extrinsically as pitch, then yaw, then roll). The composition order matters — the same angle values under a different order produce a different orientation. In particular, this does **not** match `RealityKit.Transform(pitch:yaw:roll:)`, which composes intrinsically as yaw, then pitch, then roll.

##### Stereo Fusion Constraints

The rotation is applied uniformly to both eyes as an image reorientation; it does not remap eye assignment, reproject parallax, or account for the stereo baseline encoded in the source video. For stereo content, only rotations that keep the stereo baseline horizontal in viewer space produce comfortable fusion:

- **Roll** — rotates the baseline out of horizontal, creating vertical disparity between eyes. Small roll angles cause eye strain; larger angles (≥ a few degrees) prevent fusion entirely.
- **Yaw** — may be safe in some circumstances but increasingly likely to cause anomalous parallax perception at larger angles.
- **Pitch** — the baseline is the rotation axis and the invariant of the rotation depends on the projection.
- Any mixed rotation that decomposes to a non-zero roll component exhibits the same failure proportional to the roll magnitude.

For mono content there are no stereo constraints and the full rotation space is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand/overrides-swift.struct/rotation)*