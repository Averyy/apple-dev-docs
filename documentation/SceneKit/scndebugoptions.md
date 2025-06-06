# SCNDebugOptions

**Framework**: SceneKit  
**Kind**: struct

Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct SCNDebugOptions
```

#### Overview

Debug options are bit mask patterns. To display multiple debugging overlays, combine options using the bitwise OR operator.

## Topics

### Debugging Geometry and Animation
- [static var showBoundingBoxes: SCNDebugOptions](scndebugoptions/showboundingboxes.md)
  Display the bounding boxes for any nodes with content.
- [static var showWireframe: SCNDebugOptions](scndebugoptions/showwireframe.md)
  Display geometries in the scene with wireframe rendering.
- [static var renderAsWireframe: SCNDebugOptions](scndebugoptions/renderaswireframe.md)
  Display only wireframe placeholders for geometries in the scene.
- [static var showSkeletons: SCNDebugOptions](scndebugoptions/showskeletons.md)
  Display visualizations of the skeletal animation parameters for relevant geometries.
- [static var showCreases: SCNDebugOptions](scndebugoptions/showcreases.md)
  Display nonsmoothed crease regions for geometries affected by surface subdivision.
- [static var showConstraints: SCNDebugOptions](scndebugoptions/showconstraints.md)
  Display visualizations of the constraint objects acting on nodes in the scene.
### Debugging Cameras and Lighting
- [static var showCameras: SCNDebugOptions](scndebugoptions/showcameras.md)
  Display visualizations for nodes in the scene with attached cameras and their fields of view.
- [static var showLightInfluences: SCNDebugOptions](scndebugoptions/showlightinfluences.md)
  Display the locations of each [`SCNLight`](scnlight.md) object in the scene.
- [static var showLightExtents: SCNDebugOptions](scndebugoptions/showlightextents.md)
  Display the regions affected by each [`SCNLight`](scnlight.md) object in the scene.
### Debugging Physics
- [static var showPhysicsShapes: SCNDebugOptions](scndebugoptions/showphysicsshapes.md)
  Display the physics shapes for any nodes with attached [`SCNPhysicsBody`](scnphysicsbody.md) objects.
- [static var showPhysicsFields: SCNDebugOptions](scndebugoptions/showphysicsfields.md)
  Display the regions affected by each [`SCNPhysicsField`](scnphysicsfield.md) object in the scene.
### Initializers
- [init(rawValue: UInt)](scndebugoptions/init(rawvalue:).md)
### Type Properties
- [static let showFeaturePoints: SCNDebugOptions](scndebugoptions/showfeaturepoints.md)
  Display a point cloud showing intermediate results of the scene analysis that ARKit uses to track device position.
- [static let showWorldOrigin: SCNDebugOptions](scndebugoptions/showworldorigin.md)
  Display a coordinate axis visualization indicating the position and orientation of the AR world coordinate system.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var pointOfView: SCNNode?](scnscenerenderer/pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var autoenablesDefaultLighting: Bool](scnscenerenderer/autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var isJitteringEnabled: Bool](scnscenerenderer/isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var showsStatistics: Bool](scnscenerenderer/showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var debugOptions: SCNDebugOptions](scnscenerenderer/debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [var renderingAPI: SCNRenderingAPI](scnscenerenderer/renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [enum SCNRenderingAPI](scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndebugoptions)*