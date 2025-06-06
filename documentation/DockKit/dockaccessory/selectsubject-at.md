# selectSubject(at:)

**Framework**: DockKit  
**Kind**: method

Selects a subject to track at the supplied coordinates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final func selectSubject(at unitPoint: CGPoint) async throws
```

#### Discussion

There may be times when more than one subject is in a video frame. Use this method to track a specific subject within that frame by passing a  location within the frame. The coordinates are relative to the top left of the video frame, and are values between `0` and `1`. If the framework doesn’t detect a subject at the passed coordinates, the method throws an error.

If you disable system tracking, this configuration change applies to any custom tracking for this dock accessory. The configuration applies to any camera stream the app has open if system tracking is enabled.

Call this method when implementing your own custom tracking behavior.

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device isn’t docked, or other errors if no subject is found at the position.

[`DockKitError.notConnected`](dockkiterror/notconnected.md) if device isn’t docked, or other errors if no subject is found at the position.

## See Also

- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-4yl9b.md)
  Automatically generate and send tracking vectors to the device.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-44mwn.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.Observation](dockaccessory/observation.md)
  An observation of the contents of a single video frame.
- [DockAccessory.CameraInformation](dockaccessory/camerainformation.md)
  A collection of tracking information about the camera currently in use.
- [DockAccessory.CameraOrientation](dockaccessory/cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/selectsubject(at:))*