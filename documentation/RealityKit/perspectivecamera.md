# PerspectiveCamera

**Framework**: RealityKit  
**Kind**: class

A virtual camera that establishes the rendering perspective.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class PerspectiveCamera
```

#### Overview

During an AR session, RealityKit automatically uses the device’s camera to define the perspective from which to render the scene. When rendering a scene outside of an AR session (with the view’s [`cameraMode`](arview/cameramode-swift.property.md) property set to [`ARView.CameraMode.nonAR`](arview/cameramode-swift.enum/nonar.md)), RealityKit uses a [`PerspectiveCamera`](perspectivecamera.md) instead. You can add a perspective camera anywhere in your scene to control the point of view. If you don’t explicitly provide one, RealityKit creates a default camera for you.

## Topics

### Creating a camera
- [init()](perspectivecamera/init.md)
  Creates a perspective camera entity.

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../spatial/coordinatespace3d.md)
- [CoordinateSpace3DFloat](../spatial/coordinatespace3dfloat.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [EventSource](eventsource.md)
- [HasHierarchy](hashierarchy.md)
- [HasPerspectiveCamera](hasperspectivecamera.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Observable](../observation/observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct PerspectiveCameraComponent](perspectivecameracomponent.md)
  A component that defines a virtual camera and its controls.
- [struct OrthographicCameraComponent](orthographiccameracomponent.md)
  A component that defines an orthographic virtual camera and its settings.
- [enum CameraFieldOfViewOrientation](camerafieldofvieworientation.md)
  The orientations that a camera’s field-of-view degrees can apply.
- [struct ProjectiveTransformCameraComponent](projectivetransformcameracomponent.md)
  A component that defines a virtual camera with a custom projection matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perspectivecamera)*