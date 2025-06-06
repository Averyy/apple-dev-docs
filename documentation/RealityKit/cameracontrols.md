# CameraControls

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct CameraControls
```

## Topics

### Operators
- [static func == (CameraControls, CameraControls) -> Bool](cameracontrols/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](cameracontrols/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](cameracontrols/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var dolly: CameraControls](cameracontrols/dolly.md)
  Move the camera forward and backward by dragging a trackpad or mouse.
- [static var none: CameraControls](cameracontrols/none.md)
  Disable camera control via gestures.
- [static var orbit: CameraControls](cameracontrols/orbit.md)
  Move the camera around a target by dragging a trackpad or mouse.
- [static var pan: CameraControls](cameracontrols/pan.md)
  Move the viewport up, left, right, or down by dragging a trackpad or mouse.
- [static var tilt: CameraControls](cameracontrols/tilt.md)
  Change the viewing angle by dragging a trackpad or mouse.
### Default Implementations
- [Equatable Implementations](cameracontrols/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct RealityViewCamera](realityviewcamera.md)
  A camera for reality view scenes, that can be world tracking or virtual.
- [ARView.CameraMode](arview/cameramode-swift.enum.md)
  The available camera modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/cameracontrols)*