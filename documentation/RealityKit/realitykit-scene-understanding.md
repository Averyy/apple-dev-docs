# Implementing scene understanding and reconstruction in your RealityKit app

**Framework**: RealityKit

Detect real-world objects and surfaces to create precise AR interactions.

#### Overview

RealityKit can detect planes in the real-world environment on any device, allowing virtual objects to interact with real-world surfaces. On devices with a LiDAR sensor, RealityKit can create a detailed reconstruction of the surrounding environment for more precise interactions between virtual content and the real world. With scene understanding enabled, RealityKit not only reconstructs the environment, it also recognizes many real-world object types like tables, walls, and floors.

##### Configure Scene Understanding with Realityview

To enable scene understanding in a [`RealityView`](realityview.md), configure a [`SpatialTrackingSession`](spatialtrackingsession.md).

```swift
let session = SpatialTrackingSession()
let config = SpatialTrackingSession.Configuration(
    tracking: [],
    sceneUnderstanding: [
        .occlusion,
        .physics,
        .collision,
        .shadow
])
await session.run(config)
```

In iOS and macOS, all scene-understanding capabilities are available, including [`occlusion`](spatialtrackingsession/configuration/sceneunderstandingcapability/occlusion.md), [`physics`](spatialtrackingsession/configuration/sceneunderstandingcapability/physics.md), [`collision`](spatialtrackingsession/configuration/sceneunderstandingcapability/collision.md), and [`shadow`](spatialtrackingsession/configuration/sceneunderstandingcapability/shadow.md). In visionOS, you can only enable [`physics`](spatialtrackingsession/configuration/sceneunderstandingcapability/physics.md) and [`collision`](spatialtrackingsession/configuration/sceneunderstandingcapability/collision.md).

##### Configure Scene Understanding with Arview

For existing iOS and macOS apps that use [`ARView`](arview.md), enable these features by inserting options into [`sceneUnderstanding`](arview/environment-swift.struct/sceneunderstanding-swift.property.md).

```swift
arView.environment.sceneUnderstanding.options.insert(.occlusion)
arView.environment.sceneUnderstanding.options.insert(.physics)
arView.environment.sceneUnderstanding.options.insert(.collision)
arView.environment.sceneUnderstanding.options.insert(.receivesLighting)
```

##### Use Scene Understanding Meshes

After enabling scene-understanding options, RealityKit automatically generates entities representing real-world geometry with a [`SceneUnderstandingComponent`](sceneunderstandingcomponent.md).

Retrieve these entities using an [`EntityQuery`](entityquery.md). The following code example renders a custom debug material with scene-understanding meshes:

```swift
var debugMaterial = UnlitMaterial(color: .green)
debugMaterial.triangleFillMode = .lines

let sceneUnderstandingQuery = EntityQuery(where: .has(SceneUnderstandingComponent.self) && .has(ModelComponent.self))
let queryResult = scene.performQuery(sceneUnderstandingQuery)
for entity in queryResult {
    entity.components[ModelComponent.self]?.materials = [debugMaterial]
}
```

With the physics and collision capabilities enabled, scene-understanding meshes participate in physics simulations and collision events.

The following code example identifies scene-understanding meshes in a collision event:

```swift
let _ = content.subscribe(to: CollisionEvents.Began.self) { event in
    if event.entityA.components.has(SceneUnderstandingComponent.self) {
        // The entityA is a scene-understanding mesh.
    }
}
```

##### Add Virtual Scene Understanding Meshes in Visionos

You can add [`SceneUnderstandingComponent`](sceneunderstandingcomponent.md) to your custom entities to make them behave as virtual scene-understanding meshes. A virtual scene-understanding mesh participates in system rendering features, such as shadows and depth mitigation, just like real-world geometry.

Custom virtual scene-understanding meshes only work in [`progressive`](https://developer.apple.com/documentation/swiftui/immersionstyle/progressive) or [`full`](https://developer.apple.com/documentation/swiftui/immersionstyle/full) immersive space. They don’t work in [`mixed`](https://developer.apple.com/documentation/swiftui/immersionstyle/mixed) space, or in a window or volume in the Shared Space.

##### Use Scene Reconstruction in Visionos

To enable scene reconstruction for a visionOS app, use a [`SceneReconstructionProvider`](https://developer.apple.com/documentation/arkit/scenereconstructionprovider).

```swift
let arSession = ARKitSession()
let sceneReconstruction = SceneReconstructionProvider(modes: [])

Task {
    do {
        try await arSession.run([sceneReconstruction])
    } catch {
        // Handle the error.
    }
}
```

## See Also

- [Creating a game with scene understanding](creating-a-game-with-scene-understanding.md)
  Create AR games and experiences that interact with real-world objects on LiDAR-equipped iOS devices.
- [Visualizing and interacting with a reconstructed scene](../arkit/visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [var sceneReconstruction: ARConfiguration.SceneReconstruction](../arkit/arworldtrackingconfiguration/scenereconstruction.md)
  A flag that enables scene reconstruction.
- [class func supportsSceneReconstruction(ARConfiguration.SceneReconstruction) -> Bool](../arkit/arworldtrackingconfiguration/supportsscenereconstruction(_:).md)
  Checks if the device supports scene reconstruction.
- [struct SceneUnderstandingComponent](sceneunderstandingcomponent.md)
  A component that specifies an entity is participating in the system’s scene-understanding features.
- [ARView.Environment.SceneUnderstanding](arview/environment-swift.struct/sceneunderstanding-swift.struct.md)
  An object that holds scene-understanding options for the view.
- [ARView.Environment.SceneUnderstanding.Options](arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct.md)
  Available scene-understanding options.
- [protocol HasSceneUnderstanding](hassceneunderstanding.md)
  A specification that detects and reacts to features of the physical environment.
- [class SceneReconstructionProvider](../arkit/scenereconstructionprovider.md)
  A source of live data about the shape of a person’s surroundings.
- [class ARSession](../arkit/arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitykit-scene-understanding)*