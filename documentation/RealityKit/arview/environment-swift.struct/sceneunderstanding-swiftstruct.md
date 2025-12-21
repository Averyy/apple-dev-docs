# ARView.Environment.SceneUnderstanding

**Framework**: RealityKit  
**Kind**: struct

An object that holds scene-understanding options for the view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+

## Declaration

```swift
struct SceneUnderstanding
```

## Topics

### Structures
- [ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct.md)
  Available scene-understanding options.
### Instance Properties
- [var options: ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.property.md)

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
- [ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct.md)
  Available scene-understanding options.
- [protocol HasSceneUnderstanding](hassceneunderstanding.md)
  A specification that detects and reacts to features of the physical environment.
- [final class SceneReconstructionProvider](../ARKit/SceneReconstructionProvider.md)
  A source of live data about the shape of a person’s surroundings.
- [class ARSession](../ARKit/ARSession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.struct/sceneunderstanding-swift.struct)*