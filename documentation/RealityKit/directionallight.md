# DirectionalLight

**Framework**: RealityKit  
**Kind**: class

An entity that casts a virtual light in a particular direction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency class DirectionalLight
```

#### Overview

During an AR session, RealityKit automatically lights your virtual objects to match real-world lighting. You can also explicitly add virtual lights that act upon your virtual content. This is typically most useful outside of an AR session on iOS or macOS, where your [`RealityViewCameraContent`](realityviewcameracontent.md) [`camera`](realityviewcameracontent/camera.md) property is set to [`virtual`](realityviewcamera/virtual.md).

A directional light uniformly casts light along its local z-axis—specifically, along `[0, 0, -1]`. This is equivalent to creating an [`Entity`](entity.md), and then adding a [`DirectionalLightComponent`](directionallightcomponent.md) to its [`components`](entity/components.md) set. Use the light’s [`look(at:from:upVector:relativeTo:)`](hastransform/look(at:from:upvector:relativeto:).md) method to aim the light in a particular direction.

You can configure the light’s color and intensity with the component properties in [`light`](hasdirectionallight/light.md). You can also control how or if it casts a [`shadow`](hasdirectionallight/shadow.md).

A RealityKit scene can contain up to eight dynamic lights, which are entities that contain a [`SpotLightComponent`](spotlightcomponent.md), [`PointLightComponent`](pointlightcomponent.md), or a [`DirectionalLightComponent`](directionallightcomponent.md). This limit doesn’t include light from image-based lighting.

## Topics

### Creating a directional light
- [init()](directionallight/init.md)
  Creates a new entity.

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasDirectionalLight](hasdirectionallight.md)
- [HasHierarchy](hashierarchy.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol HasPerspectiveCamera](hasperspectivecamera.md)
  An interface that enables you to configure a virtual camera that you can use to define the rendering perspective when you’re not in an AR session.
- [class PointLight](pointlight.md)
  An entity that produces an omnidirectional light for virtual objects.
- [protocol HasPointLight](haspointlight.md)
  An interface that defines a point light source component.
- [class SpotLight](spotlight.md)
  An entity that illuminates virtual content in a cone-shaped volume.
- [protocol HasSpotLight](hasspotlight.md)
  An interface that defines a spot light source component.
- [protocol HasDirectionalLight](hasdirectionallight.md)
  An interface that defines a directional light source component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallight)*