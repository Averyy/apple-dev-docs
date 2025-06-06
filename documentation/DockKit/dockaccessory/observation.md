# DockAccessory.Observation

**Framework**: DockKit  
**Kind**: struct

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

- [Track custom objects in a frame](track-custom-objects-in-a-frame.md)

#### Overview

This object represents an observation about a single video frame, including information about the type of subject, the coordinates of the subject, and the angle of the subject’s face. DockKit generates tracking vectors from this frame information. When performing your own tracking, you provide one or more [`DockAccessory.Observation`](dockaccessory/observation.md) objects to [`track(_:cameraInformation:)`](dockaccessory/track(_:camerainformation:)-44mwn.md).

## Topics

### Creating an observation
- [init(identifier: Int, type: DockAccessory.Observation.ObservationType, rect: CGRect, faceYawAngle: Measurement<UnitAngle>?)](dockaccessory/observation/init(identifier:type:rect:faceyawangle:).md)
  Creates a new observation.
### Getting properties
- [let faceYawAngle: Measurement<UnitAngle>?](dockaccessory/observation/faceyawangle.md)
  The angle of the face in radians.
- [let rect: CGRect](dockaccessory/observation/rect.md)
  The coordinates of the subject in the frame.
- [let type: DockAccessory.Observation.ObservationType](dockaccessory/observation/type.md)
  The type of subject in the frame.
- [let identifier: Int](dockaccessory/observation/identifier.md)
  A unique identifier representing the subject in the frame.
### Defining types
- [DockAccessory.Observation.ObservationType](dockaccessory/observation/observationtype.md)
  The available observation types.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func selectSubject(at: CGPoint) async throws](dockaccessory/selectsubject(at:).md)
  Selects a subject to track at the supplied coordinates.
- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-4yl9b.md)
  Automatically generate and send tracking vectors to the device.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-44mwn.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.CameraInformation](dockaccessory/camerainformation.md)
  A collection of tracking information about the camera currently in use.
- [DockAccessory.CameraOrientation](dockaccessory/cameraorientation.md)
  The set of camera orientations used to extract coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/observation)*