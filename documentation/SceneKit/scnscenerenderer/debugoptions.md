# debugOptions

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

Options for drawing overlay content in a scene that can aid debugging.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var debugOptions: SCNDebugOptions { get set }
```

#### Discussion

Use these options to display overlays that show otherwise-invisible scene content—such as node bounding boxes and the extents of physics fields—for use in debugging and profiling your app. For example:

- To visualize how well each object’s physics representation corresponds to its visible geometry,  show the shape of each [`SCNPhysicsBody`](scnphysicsbody.md) object in the scene with the [`showPhysicsShapes`](scndebugoptions/showphysicsshapes.md) option.
- To improve rendering performance in a scene with multiple [`SCNLight`](scnlight.md) objects, show each light’s area of effect with the [`showLightExtents`](scndebugoptions/showlightextents.md) option and ensure that each object in the scene is affected by no more than three lights.

## See Also

- [var pointOfView: SCNNode?](scnscenerenderer/pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var autoenablesDefaultLighting: Bool](scnscenerenderer/autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var isJitteringEnabled: Bool](scnscenerenderer/isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var showsStatistics: Bool](scnscenerenderer/showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var renderingAPI: SCNRenderingAPI](scnscenerenderer/renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [struct SCNDebugOptions](scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.
- [enum SCNRenderingAPI](scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/debugoptions)*