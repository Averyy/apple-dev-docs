# SceneUnderstandingComponent

**Framework**: RealityKit  
**Kind**: struct

A component that specifies an entity is participating in the system’s scene-understanding features.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
struct SceneUnderstandingComponent
```

## Mentions

- [Implementing scene understanding and reconstruction in your RealityKit app](realitykit-scene-understanding.md)

#### Overview

Scene understanding refers to RealityKit features like physics collision, shadows, and occlusion with real-world geometry. In iOS, `SceneUnderstandingComponent` is a read-only component. Manually adding it doesn’t have any effect.

In visionOS, `SceneUnderstandingComponent` is a write-only component. Add `SceneUnderstandingComponent` to your custom entities to let it behave as a virtual scene-understanding mesh.

For more information about scene-understanding features, see [`Implementing scene understanding and reconstruction in your RealityKit app`](realitykit-scene-understanding.md).

## Topics

### Initializing a scene-understanding component
- [init()](sceneunderstandingcomponent/init.md)
  Creates a component that makes an entity aware of certain aspects of the physical environment.
- [init(entityType: SceneUnderstandingComponent.EntityType?)](sceneunderstandingcomponent/init(entitytype:).md)
  Creates a component for the given entity type that makes an entity aware of certain aspects of the physical environment.
### Managing the component
- [var entityType: SceneUnderstandingComponent.EntityType?](sceneunderstandingcomponent/entitytype-swift.property.md)
  The type of real-world objects that the component models.
- [SceneUnderstandingComponent.EntityType](sceneunderstandingcomponent/entitytype-swift.enum.md)
  Types of real-world objects that a scene-understanding component models.
### Instance Properties
- [var origin: SceneUnderstandingComponent.Origin](sceneunderstandingcomponent/origin-swift.property.md)
  The origin that RealityKit creates the component from.
### Enumerations
- [SceneUnderstandingComponent.Origin](sceneunderstandingcomponent/origin-swift.enum.md)
  Types of scene-understanding origins this component lives in.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Creating a game with scene understanding](creating-a-game-with-scene-understanding.md)
  Create AR games and experiences that interact with real-world objects on LiDAR-equipped iOS devices.
- [Implementing scene understanding and reconstruction in your RealityKit app](realitykit-scene-understanding.md)
  Detect objects in an AR scene or create a detailed 3D reconstruction of the real-world environment.
- [Visualizing and interacting with a reconstructed scene](../ARKit/visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [var sceneReconstruction: ARConfiguration.SceneReconstruction { get set }](../ARKit/ARWorldTrackingConfiguration/sceneReconstruction.md)
  A flag that enables scene reconstruction.
- [class func supportsSceneReconstruction(_ sceneReconstruction: ARConfiguration.SceneReconstruction) -> Bool](../ARKit/ARWorldTrackingConfiguration/supportsSceneReconstruction(_:).md)
  Checks if the device supports scene reconstruction.
- [ARView.Environment.SceneUnderstanding](arview/environment-swift.struct/sceneunderstanding-swift.struct.md)
  An object that holds scene-understanding options for the view.
- [ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct.md)
  Available scene-understanding options.
- [protocol HasSceneUnderstanding](hassceneunderstanding.md)
  A specification that detects and reacts to features of the physical environment.
- [final class SceneReconstructionProvider](../ARKit/SceneReconstructionProvider.md)
  A source of live data about the shape of a person’s surroundings.
- [class ARSession](../ARKit/ARSession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneunderstandingcomponent)*