# showsStatistics

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.

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
var showsStatistics: Bool { get set }
```

#### Discussion

The SceneKit statistics view displays various information about scene rendering performance and GPU resource usage, including a frames-per-second (fps) counter. In macOS, click the gear button in the statistics view to show a panel with additional controls for adjusting SceneKit’s rendering of the scene.

## See Also

- [var pointOfView: SCNNode?](scnscenerenderer/pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var autoenablesDefaultLighting: Bool](scnscenerenderer/autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var isJitteringEnabled: Bool](scnscenerenderer/isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var debugOptions: SCNDebugOptions](scnscenerenderer/debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [var renderingAPI: SCNRenderingAPI](scnscenerenderer/renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [struct SCNDebugOptions](scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.
- [enum SCNRenderingAPI](scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/showsstatistics)*