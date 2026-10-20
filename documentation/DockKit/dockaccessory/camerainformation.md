# DockAccessory.CameraInformation

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

A collection of tracking information about the camera currently in use.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct CameraInformation
```

#### Overview

Use this class in conjuction with [`track(_:cameraInformation:)`](./track%28_,camerainformation%29-4yl9b.md) and [`track(_:cameraInformation:)`](./track%28_,camerainformation%29-44mwn.md).

## Topics

### Creating the object
- [init(captureDevice: AVCaptureDevice.DeviceType, cameraPosition: AVCaptureDevice.Position, orientation: DockAccessory.CameraOrientation, cameraIntrinsics: matrix_float3x3?, referenceDimensions: CGSize?)](./camerainformation/init%28capturedevice,cameraposition,orientation,cameraintrinsics,referencedimensions%29.md)
  Creates an object that describes the camera in use for tracking.
### Getting camera information
- [let cameraPosition: AVCaptureDevice.Position](./camerainformation/cameraposition.md)
  The physical position of the capture device.
- [let cameraIntrinsics: matrix_float3x3?](./camerainformation/cameraintrinsics.md)
  A matrix that represents the characteristics of the lens.
- [let captureDevice: AVCaptureDevice.DeviceType](./camerainformation/capturedevice.md)
  The capture device generating the video.
- [let orientation: DockAccessory.CameraOrientation](./camerainformation/orientation.md)
  The orientation of the capture device.
- [let referenceDimensions: CGSize?](./camerainformation/referencedimensions.md)
  The size of the video frame.

## Relationships

### Conforms To
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
- [DockAccessory.CameraOrientation](./cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/camerainformation)*