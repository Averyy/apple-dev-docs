# openGLContext

**Framework**: SceneKit  
**Kind**: property

The OpenGL context that the view uses to render its contents.

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
@MainActor
var openGLContext: NSOpenGLContext? { get set }
```

#### Discussion

If you use OpenGL for custom rendering (see the [`SCNShadable`](scnshadable.md), [`SCNNodeRendererDelegate`](scnnoderendererdelegate.md), and [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocols), you can use this property to share OpenGL resources between the context used for rendering the scene and other OpenGL contexts your app uses. For details on sharing OpenGL resources, see [`Sharing Rendering Context Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_contexts/opengl_contexts.html#//apple_ref/doc/uid/TP40001987-CH216-SW7). (SceneKit automatically shares its own OpenGL resources between multiple [`SCNView`](scnview.md) instances in your app as needed.)

## See Also

- [var pixelFormat: NSOpenGLPixelFormat?](scnview/pixelformat.md)
  The view’s OpenGL pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/openglcontext)*