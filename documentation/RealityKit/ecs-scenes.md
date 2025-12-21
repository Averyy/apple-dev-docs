# Scenes

**Framework**: RealityKit

The context that holds all RealityKit entities.

#### Overview

The system adds an [`Entity`](entity.md) to a [`Scene`](scene.md) when you add it to a [`RealityView`](realityview.md) with a [`RealityViewCameraContent`](realityviewcameracontent.md) or [`RealityViewContent`](realityviewcontent.md) instance. These scenes contain anchors and a hierarchy of entities that make up your RealityKit content.

The [`Scene`](scene.md) instance has helpful methods to perform ray casts to help you better understand your scene, and methods that find entities either by name or by components they own.

## Topics

### Scene management
- [class Scene](scene.md)
  A container that holds the collection of entities that an AR view renders.
- [struct AnchorCollection](scene/anchorcollection.md)
  A collection of anchor entities.
### Entity searches
- [struct QueryPredicate](querypredicate.md)
  An object that defines the criteria for an entity query.
- [struct PixelCastHit](pixelcasthit.md)
### Event publishers and subscription
- [enum SceneEvents](sceneevents.md)
  Events the scene invokes.
- [struct Publisher](scene/publisher.md)
  A publisher for the given event type in the scene.
### Scene reconstructions and analysis
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
- [struct SceneUnderstandingComponent](sceneunderstandingcomponent.md)
  A component that specifies an entity is participating in the system’s scene-understanding features.
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

## See Also

- [Systems](ecs-systems.md)
  Apply behaviors and physical effects to the entities in a RealityKit scene.
- [Events](ecs-events.md)
  Respond to things happening in your RealityKit scene by subscribing to specific event types.
- [Entity actions](ecs-entity-actions.md)
  Create simple, reusable actions that can change your app state, RealityKit scene, or animate an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ecs-scenes)*