# openGLContext

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layer’s OpenGL context.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

> **Deprecated**: Please use CAMetalLayer instead.

## Declaration

```swift
var openGLContext: NSOpenGLContext? { get set }
```

```objc
@property (strong, nullable) NSOpenGLContext * openGLContext;
```

## Discussion

Provides access to the layer’s associated [`NSOpenGLContext`](../nsopenglcontext.md).  Subclasses shouldn’t invoke `setOpenGLContext:`, but can override it if desired to intercept assignment of the layer’s context.

## See Also

### Managing the Rendering Context
- [func openGLContext(for: NSOpenGLPixelFormat) -> NSOpenGLContext](./openglcontext%28for%29.md)
  Returns the OpenGL context to use for the requested pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/openglcontext)*