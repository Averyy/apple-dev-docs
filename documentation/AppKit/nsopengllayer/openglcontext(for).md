# openGLContext(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the OpenGL context to use for the requested pixel format.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

> **Deprecated**: Please use CAMetalLayer instead.

## Declaration

```swift
func openGLContext(for pixelFormat: NSOpenGLPixelFormat) -> NSOpenGLContext
```

```objc
- (NSOpenGLContext *) openGLContextForPixelFormat:(NSOpenGLPixelFormat *) pixelFormat;
```

#### Return Value

An autoreleased [`NSOpenGLContext`](../nsopenglcontext.md).

## Parameters

- `pixelFormat`: The pixel format.

## See Also

### Managing the Rendering Context
- [var openGLContext: NSOpenGLContext?](./openglcontext.md)
  The layer’s OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/openglcontext(for:))*