# openGLContext

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The [`NSOpenGLContext`](../nsopenglcontext.md) object associated with the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
var openGLContext: NSOpenGLContext? { get set }
```

```objc
@property (strong, nullable) NSOpenGLContext * openGLContext;
```

#### Discussion

If the receiver has no associated context object, a new `NSOpenGLContext` object is created. The new object is initialized with the receiver’s pixel format information.

## See Also

### Related Documentation
- [var pixelFormat: NSOpenGLPixelFormat?](./pixelformat.md)
  The [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object associated with the receiver.
### Managing the NSOpenGLContext
- [func prepareOpenGL()](./prepareopengl%28%29.md)
  Used by subclasses to initialize OpenGL state.
- [func clearGLContext()](./clearglcontext%28%29.md)
  Releases the [`NSOpenGLContext`](../nsopenglcontext.md) object associated with the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/openglcontext)*