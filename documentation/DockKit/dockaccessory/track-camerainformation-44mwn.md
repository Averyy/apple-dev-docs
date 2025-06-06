# track(_:cameraInformation:)

**Framework**: Dockkit  
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
final func track(_ data: [DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws
```

#### Discussion

The device receives tracking vectors based on manually constructed observations.

Disable system tracking, then supply the observations at a fixed rate between 10 and 30 times per second. Any other rate is unsupported. Calling this method without first disabling system tracking is a fatal error.

> **Note**: [`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

## Parameters

- `data`: An array of   objects indicating the location of objects of interest in the frame.
- `cameraInformation`: The camera currently being used, and the orientation of the device.

## See Also

- [func selectSubject(at: CGPoint) async throws](dockaccessory/selectsubject(at:).md)
  Selects a subject to track at the supplied coordinates.
- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-4yl9b.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.Observation](dockaccessory/observation.md)
  An observation of the contents of a single video frame.
- [DockAccessory.CameraInformation](dockaccessory/camerainformation.md)
  A collection of tracking information about the camera currently in use.
- [DockAccessory.CameraOrientation](dockaccessory/cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/track(_:camerainformation:)-44mwn)*