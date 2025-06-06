# openGLContext

**Framework**: AppKit  
**Kind**: property

The [`NSOpenGLContext`](nsopenglcontext.md) object associated with the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var openGLContext: NSOpenGLContext? { get set }
```

#### Discussion

If the receiver has no associated context object, a new `NSOpenGLContext` object is created. The new object is initialized with the receiver’s pixel format information.

## See Also

- [var pixelFormat: NSOpenGLPixelFormat?](nsopenglview/pixelformat.md)
  The [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object associated with the receiver.
- [func prepareOpenGL()](nsopenglview/prepareopengl.md)
  Used by subclasses to initialize OpenGL state.
- [func clearGLContext()](nsopenglview/clearglcontext.md)
  Releases the [`NSOpenGLContext`](nsopenglcontext.md) object associated with the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/openglcontext)*