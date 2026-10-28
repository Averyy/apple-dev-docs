# flushBuffer()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Copies the back buffer to the front buffer of the OpenGL context.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
func flushBuffer()
```

```objc
- (void) flushBuffer;
```

## Discussion

If the receiver is not a double-buffered context, this call does nothing.

If the [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object used to create the context had a [`false`](../../Swift/false.md) backing store attribute (`NSOpenGLPFABackingStore`), the buffers may be exchanged rather than copied. This is often the case in full-screen mode.

According to the swap interval context attribute (see [`NSOpenGLCPSwapInterval`](../nsopenglcpswapinterval.md)), the copy may take place during the vertical retrace of the monitor, rather than immediately after [`flushBuffer()`](./flushbuffer%28%29.md) is called. An implicit `glFlush` is done by [`flushBuffer()`](./flushbuffer%28%29.md) before it returns. For optimal performance, an application should not call `glFlush` immediately before calling [`flushBuffer()`](./flushbuffer%28%29.md). Subsequent OpenGL commands can be issued immediately after calling [`flushBuffer()`](./flushbuffer%28%29.md), but are not executed until the buffer copy is completed.

## See Also

### Related Documentation
- [func getValues(UnsafeMutablePointer<GLint>, for: NSOpenGLContext.Parameter)](./getvalues%28_,for%29.md)
  Returns the value of the requested parameter.
- [init?(format: NSOpenGLPixelFormat, share: NSOpenGLContext?)](./init%28format,share%29.md)
  Returns an OpenGL context object initialized with the specified pixel format information.
- [func setValues(UnsafePointer<GLint>, for: NSOpenGLContext.Parameter)](./setvalues%28_,for%29.md)
  Sets the value of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/flushbuffer())*