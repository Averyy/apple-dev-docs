# autoenablesDefaultLighting

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that determines whether SceneKit automatically adds lights to a scene.

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
var autoenablesDefaultLighting: Bool { get set }
```

```objc
@property (nonatomic) BOOL autoenablesDefaultLighting;
```

## Discussion

If this property’s value is [`false`](../../Swift/false.md) (the default), the only light sources SceneKit uses for rendering a scene are those contained in the scene graph. If you change the value to [`true`](../../Swift/true.md), SceneKit automatically adds and places an omnidirectional light source when rendering scenes that contain no lights or only contain ambient lights.

## See Also

### Managing Scene Display
- [var pointOfView: SCNNode?](./pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var isJitteringEnabled: Bool](./isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var showsStatistics: Bool](./showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var debugOptions: SCNDebugOptions](./debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [var renderingAPI: SCNRenderingAPI](./renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [struct SCNDebugOptions](../scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](./debugoptions.md) property.
- [enum SCNRenderingAPI](../scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](../scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](./renderingapi.md) property and the [`preferredRenderingAPI`](../scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](../scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/autoenablesdefaultlighting)*