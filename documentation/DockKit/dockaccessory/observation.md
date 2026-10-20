# DockAccessory.Observation

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

An observation of the contents of a single video frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Observation
```

## Mentions

- [Track custom objects in a frame](../track-custom-objects-in-a-frame.md)

#### Overview

This object represents an observation about a single video frame, including information about the type of subject, the coordinates of the subject, and the angle of the subject’s face. DockKit generates tracking vectors from this frame information. When performing your own tracking, you provide one or more [`DockAccessory.Observation`](./observation.md) objects to [`track(_:cameraInformation:)`](./track%28_,camerainformation%29-44mwn.md).

## Topics

### Creating an observation
- [init(identifier: Int, type: DockAccessory.Observation.ObservationType, rect: CGRect, faceYawAngle: Measurement<UnitAngle>?)](./observation/init%28identifier,type,rect,faceyawangle%29.md)
  Creates a new observation.
### Getting properties
- [let faceYawAngle: Measurement<UnitAngle>?](./observation/faceyawangle.md)
  The angle of the face in radians.
- [let rect: CGRect](./observation/rect.md)
  The coordinates of the subject in the frame.
- [let type: DockAccessory.Observation.ObservationType](./observation/type.md)
  The type of subject in the frame.
- [let identifier: Int](./observation/identifier.md)
  A unique identifier representing the subject in the frame.
### Defining types
- [DockAccessory.Observation.ObservationType](./observation/observationtype.md)
  The available observation types.

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
- [DockAccessory.CameraInformation](./camerainformation.md)
  A collection of tracking information about the camera currently in use.
- [DockAccessory.CameraOrientation](./cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/observation)*