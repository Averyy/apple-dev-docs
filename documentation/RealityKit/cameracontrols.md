# CameraControls

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Options that determine how people use gestures to pan, orbit, tilt, or dolly a virtual camera.

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

### Type Properties
- [static var dolly: CameraControls](./cameracontrols/dolly.md)
  Move the camera forward and backward by dragging a trackpad or mouse.
- [static var none: CameraControls](./cameracontrols/none.md)
  Disable camera control via gestures.
- [static var orbit: CameraControls](./cameracontrols/orbit.md)
  Move the camera around a target by dragging a trackpad or mouse.
- [static var pan: CameraControls](./cameracontrols/pan.md)
  Move the viewport up, left, right, or down by dragging a trackpad or mouse.
- [static var tilt: CameraControls](./cameracontrols/tilt.md)
  Change the viewing angle by dragging a trackpad or mouse.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Camera mode settings
- [struct RealityViewCamera](./realityviewcamera.md)
  A camera for reality view scenes, that can be world tracking or virtual.
- [func realityViewCameraControls(CameraControls) -> some View
](../SwiftUI/view/realityviewcameracontrols%28_%29.md)
  Adds gestures that control the position and direction of a virtual camera.
- [var realityViewCameraControls: CameraControls](../SwiftUI/environmentvalues/realityviewcameracontrols.md)
  The camera controls for the reality view.
- [ARView.CameraMode](./arview/cameramode-swift.enum.md)
  The available camera modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/cameracontrols)*