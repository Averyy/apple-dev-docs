# ARView.Environment.SceneUnderstanding.Options

**Framework**: RealityKit  
**Kind**: struct

Available scene-understanding options.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+

## Declaration

```swift
struct Options
```

## Topics

### Type Properties
- [static let collision: ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/collision.md)
  The `.collision` option means that the reconstructed geometry can be used for collision queries (i.e. raycasting)
- [static let `default`: ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/default.md)
  The `.default` options is a sentinel value that indicates the user wants whatever scene-understanding features work with the current device and are supported. It overrides other options in the options set.
- [static let occlusion: ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/occlusion.md)
  The `.occlusion` option means that the reconstructed geometry will be used for rendering, but only to update the depth buffer. Parts of virtual objects which are behind the reconstructed geometry are not rendered.
- [static let physics: ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/physics.md)
  No abstract
- [static let receivesLighting: ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/receiveslighting.md)
  The `.receivesLighting` option means that the virtual lights will interact with real world surfaces causing them to shine. The properties  of the mesh will be set to a default material.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [struct SceneUnderstandingComponent](sceneunderstandingcomponent.md)
  A component that specifies an entity is participating in the system’s scene-understanding features.
- [ARView.Environment.SceneUnderstanding](arview/environment-swift.struct/sceneunderstanding-swift.struct.md)
  An object that holds scene-understanding options for the view.
- [protocol HasSceneUnderstanding](hassceneunderstanding.md)
  A specification that detects and reacts to features of the physical environment.
- [final class SceneReconstructionProvider](../ARKit/SceneReconstructionProvider.md)
  A source of live data about the shape of a person’s surroundings.
- [class ARSession](../ARKit/ARSession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct)*