# SCNRenderingAPI.openGLLegacy

**Framework**: SceneKit  
**Kind**: case

Use the Legacy OpenGL API for SceneKit rendering in macOS.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case openGLLegacy
```

#### Discussion

This option is available on all macOS systems supporting SceneKit. If you request the Metal rendering API for an [`SCNView`](scnview.md) object on a system that does not support Metal, SceneKit falls back to the Legacy OpenGL API.

## See Also

- [SCNRenderingAPI.metal](scnrenderingapi/metal.md)
  Use the Metal framework for SceneKit rendering.
- [SCNRenderingAPI.openGLES2](scnrenderingapi/opengles2.md)
  Use the OpenGL ES 2.0 API for SceneKit rendering in iOS.
- [SCNRenderingAPI.openGLCore32](scnrenderingapi/openglcore32.md)
  Use the OpenGL 3.2 Core Profile API for SceneKit rendering in macOS.
- [SCNRenderingAPI.openGLCore41](scnrenderingapi/openglcore41.md)
  Use the OpenGL 4.1 Core Profile API for SceneKit rendering in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderingapi/opengllegacy)*