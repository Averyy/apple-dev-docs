# DockAccessory.CameraOrientation

**Framework**: DockKit  
**Kind**: enum

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
- [DockAccessory.CameraOrientation.corrected](dockaccessory/cameraorientation/corrected.md)
  The orientation corresponds to the unit rectangle.
- [DockAccessory.CameraOrientation.faceUp](dockaccessory/cameraorientation/faceup.md)
  The orientation is facing up.
- [DockAccessory.CameraOrientation.faceDown](dockaccessory/cameraorientation/facedown.md)
  The orientation is facing down.
- [DockAccessory.CameraOrientation.landscapeLeft](dockaccessory/cameraorientation/landscapeleft.md)
  The orientation is landscape left.
- [DockAccessory.CameraOrientation.landscapeRight](dockaccessory/cameraorientation/landscaperight.md)
  The orientation is landscape right.
- [DockAccessory.CameraOrientation.portrait](dockaccessory/cameraorientation/portrait.md)
  The orientation is portrait.
- [DockAccessory.CameraOrientation.portraitUpsideDown](dockaccessory/cameraorientation/portraitupsidedown.md)
  The orientation is portrait, upside down.
- [DockAccessory.CameraOrientation.unknown](dockaccessory/cameraorientation/unknown.md)
  The orientation is unknown.
### Operators
- [static func == (DockAccessory.CameraOrientation, DockAccessory.CameraOrientation) -> Bool](dockaccessory/cameraorientation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](dockaccessory/cameraorientation/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/cameraorientation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/cameraorientation/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [DockAccessory.CameraInformation](dockaccessory/camerainformation.md)
  A collection of tracking information about the camera currently in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/cameraorientation)*