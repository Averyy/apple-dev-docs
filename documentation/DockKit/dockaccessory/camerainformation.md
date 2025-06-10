# DockAccessory.CameraInformation

**Framework**: DockKit  
**Kind**: struct

A collection of tracking information about the camera currently in use.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.1+

## Declaration

```swift
struct CameraInformation
```

#### Overview

Use this class in conjuction with [`track(_:cameraInformation:)`](dockaccessory/track(_:camerainformation:)-4yl9b.md) and [`track(_:cameraInformation:)`](dockaccessory/track(_:camerainformation:)-44mwn.md).

## Topics

### Creating the object
- [init(captureDevice: AVCaptureDevice.DeviceType, cameraPosition: AVCaptureDevice.Position, orientation: DockAccessory.CameraOrientation, cameraIntrinsics: matrix_float3x3?, referenceDimensions: CGSize?)](dockaccessory/camerainformation/init(capturedevice:cameraposition:orientation:cameraintrinsics:referencedimensions:).md)
  Creates an object that describes the camera in use for tracking.
### Getting camera information
- [let cameraPosition: AVCaptureDevice.Position](dockaccessory/camerainformation/cameraposition.md)
  The physical position of the capture device.
- [let cameraIntrinsics: matrix_float3x3?](dockaccessory/camerainformation/cameraintrinsics.md)
  A matrix that represents the characteristics of the lens.
- [let captureDevice: AVCaptureDevice.DeviceType](dockaccessory/camerainformation/capturedevice.md)
  The capture device generating the video.
- [let orientation: DockAccessory.CameraOrientation](dockaccessory/camerainformation/orientation.md)
  The orientation of the capture device.
- [let referenceDimensions: CGSize?](dockaccessory/camerainformation/referencedimensions.md)
  The size of the video frame.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func selectSubject(at: CGPoint) async throws](dockaccessory/selectsubject(at:).md)
  Selects a subject to track at the supplied coordinates.
- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-4yl9b.md)
  Automatically generate and send tracking vectors to the device.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-44mwn.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.Observation](dockaccessory/observation.md)
  An observation of the contents of a single video frame.
- [DockAccessory.CameraOrientation](dockaccessory/cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/camerainformation)*