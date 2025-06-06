# ProjectiveTransformCameraComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines a virtual camera with a custom projection matrix.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ProjectiveTransformCameraComponent
```

#### Overview

Each scene requires a camera, which defines the viewpoint from which RealityKit renders the scene. The projective transform camera renders the entities in the scene based on a custom user defined matrix. To create a projective transform camera, add this component to an entity.

```swift
// Create an entity to hold the camera component.
let cameraEntity = Entity()

// Create a projective transform camera component with a custom matrix.
var projectiveCameraComponent = ProjectiveTransformCameraComponent(projectionMatrix: customMatrix)

// Add it to the camera entity.
cameraEntity.components.set(projectiveCameraComponent)

// Set the entity's position and orientation to look at the subject.
let cameraPosition: SIMD3<Float> = [0, 1, 3]

// The subject in this case is the origin.
let target: SIMD3<Float> = .zero
cameraEntity.look(at: target, from: cameraPosition, relativeTo: nil)

// Add the camera entity to your scene.
content.add(cameraEntity)
```

## Topics

### Operators
- [static func == (ProjectiveTransformCameraComponent, ProjectiveTransformCameraComponent) -> Bool](projectivetransformcameracomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(projectionMatrix: float4x4)](projectivetransformcameracomponent/init(projectionmatrix:).md)
  Creates a new custom matrix camera component with the given settings.
### Instance Properties
- [var transform: float4x4](projectivetransformcameracomponent/transform.md)
  The custom projection RealityKit applies to objects in the scene.
### Default Implementations
- [Component Implementations](projectivetransformcameracomponent/component-implementations.md)
- [Equatable Implementations](projectivetransformcameracomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct PerspectiveCameraComponent](perspectivecameracomponent.md)
  A component that defines a virtual camera and its controls.
- [struct OrthographicCameraComponent](orthographiccameracomponent.md)
  A component that defines an orthographic virtual camera and its settings.
- [enum CameraFieldOfViewOrientation](camerafieldofvieworientation.md)
  The orientations that a camera’s field-of-view degrees can apply.
- [class PerspectiveCamera](perspectivecamera.md)
  A virtual camera that establishes the rendering perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/projectivetransformcameracomponent)*