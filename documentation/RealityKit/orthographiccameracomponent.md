# OrthographicCameraComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines an orthographic virtual camera and its settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct OrthographicCameraComponent
```

#### Overview

Each scene requires a camera that defines the viewpoint from which RealityKit renders the scene. The orthographic camera renders the entities in the scene without the perspective of depth, meaning faraway objects don’t look smaller.

To create an orthographic camera, add this component to an entity.

|  |  |
| --- | --- |
| ![An illustration of three cubes, one behind the other, rendered with a perspective camera. The cube farthest away appears smaller than the closest one.](https://docs-assets.developer.apple.com/published/ccf81006872074acd2f1735dc3a9ed96/orthocamera-perspective-cubes.png) | ![A screenshot of three cubes, one behind the other, rendered with a orthographic camera. The cubes appear the same size, regardless of their distance.](https://docs-assets.developer.apple.com/published/6a06251fd3a6fe3a7dca37a87da85cc4/orthocamera-orthographic-cubes.png) |

You can add an `OrthographicCameraComponent` to an entity’s component set, and orient that entity so that it looks at a specific target using [`look(at:from:upVector:relativeTo:)`](entity/look(at:from:upvector:relativeto:).md).

```swift
// Create an entity to hold the camera component.
let cameraEntity = Entity()

// Create an orthographic camera component and add it to the camera entity.
cameraEntity.components.set(OrthographicCameraComponent())

// Set the entity's position and orientation to look at the subject.
let cameraPosition: SIMD3<Float> = [0, 1, 3]

// The subject in this case is the origin.
let target: SIMD3<Float> = .zero
cameraEntity.look(at: target, from: cameraPosition, relativeTo: nil)

// Add the camera entity to your scene.
content.add(cameraEntity)
```

In AR scenarios, the system provides the camera automatically; however, in non-AR scenarios, the app needs to set the camera. If the app doesn’t provide a camera, the system uses the default perspective camera.

## Topics

### Creating a camera component
- [init()](orthographiccameracomponent/init.md)
  Creates an orthographic camera component with default values.
### Setting focal points
- [var far: Float](orthographiccameracomponent/far.md)
  The maximum distance in meters from the camera that the camera can see.
- [var near: Float](orthographiccameracomponent/near.md)
  The minimum distance in meters from the camera that the camera can see.
### Setting the camera scale
- [var scale: Float](orthographiccameracomponent/scale.md)
  A floating-point value the camera uses to scale entities.
- [var scaleDirection: CameraFieldOfViewOrientation](orthographiccameracomponent/scaledirection.md)
  The direction in which the camera applies scaling.
### Comparing orthographic camera components
- [static func == (OrthographicCameraComponent, OrthographicCameraComponent) -> Bool](orthographiccameracomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](orthographiccameracomponent/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Component Implementations](orthographiccameracomponent/component-implementations.md)
- [Equatable Implementations](orthographiccameracomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct PerspectiveCameraComponent](perspectivecameracomponent.md)
  A component that defines a virtual camera and its controls.
- [enum CameraFieldOfViewOrientation](camerafieldofvieworientation.md)
  The orientations that a camera’s field-of-view degrees can apply.
- [struct ProjectiveTransformCameraComponent](projectivetransformcameracomponent.md)
  A component that defines a virtual camera with a custom projection matrix.
- [class PerspectiveCamera](perspectivecamera.md)
  A virtual camera that establishes the rendering perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orthographiccameracomponent)*