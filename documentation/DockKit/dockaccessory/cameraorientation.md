# DockAccessory.CameraOrientation

**Framework**: DockKit  
**Kind**: enum  
**Role**: Enumeration

The set of camera orientations used to extract coordinates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum CameraOrientation
```

## Topics

### Getting camera orientation
- [DockAccessory.CameraOrientation.corrected](./cameraorientation/corrected.md)
  The orientation corresponds to the unit rectangle.
- [DockAccessory.CameraOrientation.faceUp](./cameraorientation/faceup.md)
  The orientation is facing up.
- [DockAccessory.CameraOrientation.faceDown](./cameraorientation/facedown.md)
  The orientation is facing down.
- [DockAccessory.CameraOrientation.landscapeLeft](./cameraorientation/landscapeleft.md)
  The orientation is landscape left.
- [DockAccessory.CameraOrientation.landscapeRight](./cameraorientation/landscaperight.md)
  The orientation is landscape right.
- [DockAccessory.CameraOrientation.portrait](./cameraorientation/portrait.md)
  The orientation is portrait.
- [DockAccessory.CameraOrientation.portraitUpsideDown](./cameraorientation/portraitupsidedown.md)
  The orientation is portrait, upside down.
- [DockAccessory.CameraOrientation.unknown](./cameraorientation/unknown.md)
  The orientation is unknown.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selecting and tracking
- [func selectSubject(at: CGPoint) async throws](./selectsubject%28at%29.md)
  Selects a subject to track at the supplied coordinates.
- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws](./track%28_,camerainformation%29-4yl9b.md)
  Automatically generate and send tracking vectors to the device.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws](./track%28_,camerainformation%29-44mwn.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.Observation](./observation.md)
  An observation of the contents of a single video frame.
- [DockAccessory.CameraInformation](./camerainformation.md)
  A collection of tracking information about the camera currently in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/cameraorientation)*