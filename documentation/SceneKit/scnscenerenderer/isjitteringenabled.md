# isJitteringEnabled

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.

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
var isJitteringEnabled: Bool { get set }
```

#### Discussion

Jittering is a process that SceneKit uses to improve the visual quality of a rendered scene. While the scene’s content is still, SceneKit moves the [`pointOfView`](scnscenerenderer/pointofview.md) location very slightly (by less than a pixel in projected screen space). It then composites images rendered after several such moves to create the final rendered scene, creating an antialiasing effect that smooths the edges of rendered geometry.

By default, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), specifying that SceneKit should not perform jittering. Change the value to [`true`](https://developer.apple.com/documentation/swift/true) to enable jittering.

Because the [`SCNView`](scnview.md) and [`SCNLayer`](scnlayer.md) classes perform jittering automatically and asynchronously, enabling jittering for these classes has minimal impact on rendering performance. The [`SCNRenderer`](scnrenderer.md) class performs jittering synchronously, incurring a high performance cost. With this class, jittering is suitable for rendering single frames on demand, but not for real-time rendering.

## See Also

- [var pointOfView: SCNNode?](scnscenerenderer/pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var autoenablesDefaultLighting: Bool](scnscenerenderer/autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var showsStatistics: Bool](scnscenerenderer/showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var debugOptions: SCNDebugOptions](scnscenerenderer/debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [var renderingAPI: SCNRenderingAPI](scnscenerenderer/renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [struct SCNDebugOptions](scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.
- [enum SCNRenderingAPI](scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/isjitteringenabled)*