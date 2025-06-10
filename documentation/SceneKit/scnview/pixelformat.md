# pixelFormat

**Framework**: SceneKit  
**Kind**: property

The view’s OpenGL pixel format.

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
var pixelFormat: NSOpenGLPixelFormat? { get set }
```

#### Discussion

A pixel format object configures OpenGL attributes for rendering. For example, if you use OpenGL for custom rendering (see the [`SCNShadable`](scnshadable.md), [`SCNNodeRendererDelegate`](scnnoderendererdelegate.md), and [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocols), setting the pixel format to one that specifies the OpenGL 3.2 Core Profile allows you to use modern OpenGL APIs in your custom rendering code.

To change the pixel format, you can do either of the following:

- Set this property’s value before providing a scene for the view to render.
- In an [`SCNView`](scnview.md) subclass, override this property’s getter method to return your preferred pixel format.

## See Also

- [var openGLContext: NSOpenGLContext?](scnview/openglcontext.md)
  The OpenGL context that the view uses to render its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/pixelformat)*