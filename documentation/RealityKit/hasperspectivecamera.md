# HasPerspectiveCamera

**Framework**: RealityKit  
**Kind**: protocol

An interface that enables you to configure a virtual camera that you can use to define the rendering perspective when you’re not in an AR session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasPerspectiveCamera : HasTransform
```

## Topics

### Getting the camera
- [var camera: PerspectiveCameraComponent](hasperspectivecamera/camera.md)
  A camera component for the perspective camera entity.

## Relationships

### Inherits From
- [HasTransform](hastransform.md)
### Conforming Types
- [PerspectiveCamera](perspectivecamera.md)

## See Also

- [class PointLight](pointlight.md)
  An entity that produces an omnidirectional light for virtual objects.
- [protocol HasPointLight](haspointlight.md)
  An interface that defines a point light source component.
- [class SpotLight](spotlight.md)
  An entity that illuminates virtual content in a cone-shaped volume.
- [protocol HasSpotLight](hasspotlight.md)
  An interface that defines a spot light source component.
- [class DirectionalLight](directionallight.md)
  An entity that casts a virtual light in a particular direction.
- [protocol HasDirectionalLight](hasdirectionallight.md)
  An interface that defines a directional light source component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasperspectivecamera)*