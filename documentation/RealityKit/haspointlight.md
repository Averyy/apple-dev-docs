# HasPointLight

**Framework**: RealityKit  
**Kind**: protocol

An interface that defines a point light source component.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasPointLight : HasTransform
```

## Topics

### Getting the point light component
- [var light: PointLightComponent](haspointlight/light.md)
  A point light component for the entity.

## Relationships

### Inherits From
- [HasTransform](hastransform.md)
### Conforming Types
- [PointLight](pointlight.md)

## See Also

- [protocol HasPerspectiveCamera](hasperspectivecamera.md)
  An interface that enables you to configure a virtual camera that you can use to define the rendering perspective when you’re not in an AR session.
- [class PointLight](pointlight.md)
  An entity that produces an omnidirectional light for virtual objects.
- [class SpotLight](spotlight.md)
  An entity that illuminates virtual content in a cone-shaped volume.
- [protocol HasSpotLight](hasspotlight.md)
  An interface that defines a spot light source component.
- [class DirectionalLight](directionallight.md)
  An entity that casts a virtual light in a particular direction.
- [protocol HasDirectionalLight](hasdirectionallight.md)
  An interface that defines a directional light source component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/haspointlight)*