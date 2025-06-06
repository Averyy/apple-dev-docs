# track(_:cameraInformation:)

**Framework**: DockKit  
**Kind**: method

Automatically generate and send tracking vectors to the device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.1+

## Declaration

```swift
final func track(_ metadata: [AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws
```

## Mentions

- [Track custom objects in a frame](track-custom-objects-in-a-frame.md)

#### Discussion

The vectors are based on metadata coming from the camera.

Disable system tracking, then supply the observations at a fixed rate between 10 and 30 times per second. Any other rate is unsupported.

> **Note**: [`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

[`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

## Parameters

- `metadata`: An array of   objects indicating the location of objects within the frame.
- `cameraInformation`: The camera in current use and its orientation.

## See Also

- [func selectSubject(at: CGPoint) async throws](dockaccessory/selectsubject(at:).md)
  Selects a subject to track at the supplied coordinates.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-44mwn.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.Observation](dockaccessory/observation.md)
  An observation of the contents of a single video frame.
- [DockAccessory.CameraInformation](dockaccessory/camerainformation.md)
  A collection of tracking information about the camera currently in use.
- [DockAccessory.CameraOrientation](dockaccessory/cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/track(_:camerainformation:)-4yl9b)*