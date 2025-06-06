# SCNRenderingAPI

**Framework**: SceneKit  
**Kind**: enum

Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.

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
enum SCNRenderingAPI
```

## Topics

### Constants
- [SCNRenderingAPI.metal](scnrenderingapi/metal.md)
  Use the Metal framework for SceneKit rendering.
- [SCNRenderingAPI.openGLES2](scnrenderingapi/opengles2.md)
  Use the OpenGL ES 2.0 API for SceneKit rendering in iOS.
- [SCNRenderingAPI.openGLLegacy](scnrenderingapi/opengllegacy.md)
  Use the Legacy OpenGL API for SceneKit rendering in macOS.
- [SCNRenderingAPI.openGLCore32](scnrenderingapi/openglcore32.md)
  Use the OpenGL 3.2 Core Profile API for SceneKit rendering in macOS.
- [SCNRenderingAPI.openGLCore41](scnrenderingapi/openglcore41.md)
  Use the OpenGL 4.1 Core Profile API for SceneKit rendering in macOS.
### Initializers
- [init?(rawValue: UInt)](scnrenderingapi/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct SCNDebugOptions](scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderingapi)*