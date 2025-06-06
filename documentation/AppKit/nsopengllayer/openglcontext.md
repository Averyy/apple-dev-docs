# openGLContext

**Framework**: AppKit  
**Kind**: property

The layer’s OpenGL context.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var openGLContext: NSOpenGLContext? { get set }
```

#### Discussion

Provides access to the layer’s associated [`NSOpenGLContext`](nsopenglcontext.md).  Subclasses shouldn’t invoke `setOpenGLContext:`, but can override it if desired to intercept assignment of the layer’s context.

## See Also

- [func openGLContext(for: NSOpenGLPixelFormat) -> NSOpenGLContext](nsopengllayer/openglcontext(for:).md)
  Returns the OpenGL context to use for the requested pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/openglcontext)*