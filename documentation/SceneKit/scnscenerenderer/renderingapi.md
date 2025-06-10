# renderingAPI

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The graphics technology SceneKit uses to render the scene.

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
var renderingAPI: SCNRenderingAPI { get }
```

#### Discussion

You choose a graphics technology when initializing a scene renderer:

- When initializing a [`SCNView`](scnview.md) object, use the [`init(frame:options:)`](scnview/init(frame:options:).md) initializer and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) key. Alternatively, create a view in Interface Builder and use the Rendering API control in the inspector. During initialization, the view will attempt to use the preferred API, but will fall back to a different API if the preferred one is not supported on the current hardware.
- To create a [`SCNRenderer`](scnrenderer.md) object that renders into your own OpenGL contect, use the [`init(context:options:)`](scnrenderer/init(context:options:).md) initializer. To create a renderer for use in your own Metal workflow, use the [`init(device:options:)`](scnrenderer/init(device:options:).md) initializer.
- The rendering technology used by a [`SCNLayer`](scnlayer.md) object is determined by Core Animation.

After initializing a renderer, this property reflects the rendering technology in use.

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
- [struct SCNDebugOptions](scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.
- [enum SCNRenderingAPI](scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/renderingapi)*