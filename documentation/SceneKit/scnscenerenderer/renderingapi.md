# renderingAPI

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The graphics technology SceneKit uses to render the scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var renderingAPI: SCNRenderingAPI { get }
```

```objc
@property (nonatomic, readonly) SCNRenderingAPI renderingAPI;
```

## Discussion

You choose a graphics technology when initializing a scene renderer:

- When initializing a [`SCNView`](../scnview.md) object, use the [`init(frame:options:)`](../scnview/init%28frame,options%29.md) initializer and the [`preferredRenderingAPI`](../scnview/option/preferredrenderingapi.md) key. Alternatively, create a view in Interface Builder and use the Rendering API control in the inspector. During initialization, the view will attempt to use the preferred API, but will fall back to a different API if the preferred one is not supported on the current hardware.
- To create a [`SCNRenderer`](../scnrenderer.md) object that renders into your own OpenGL contect, use the [`init(context:options:)`](../scnrenderer/init%28context,options%29.md) initializer. To create a renderer for use in your own Metal workflow, use the [`init(device:options:)`](../scnrenderer/init%28device,options%29.md) initializer.
- The rendering technology used by a [`SCNLayer`](../scnlayer.md) object is determined by Core Animation.

After initializing a renderer, this property reflects the rendering technology in use.

## See Also

### Managing Scene Display
- [var pointOfView: SCNNode?](./pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var autoenablesDefaultLighting: Bool](./autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var isJitteringEnabled: Bool](./isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var showsStatistics: Bool](./showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var debugOptions: SCNDebugOptions](./debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [struct SCNDebugOptions](../scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](./debugoptions.md) property.
- [enum SCNRenderingAPI](../scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](../scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](./renderingapi.md) property and the [`preferredRenderingAPI`](../scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](../scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/renderingapi)*