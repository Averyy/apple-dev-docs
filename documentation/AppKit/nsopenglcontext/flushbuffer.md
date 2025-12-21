# flushBuffer()

**Framework**: AppKit  
**Kind**: method

Copies the back buffer to the front buffer of the OpenGL context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func flushBuffer()
```

#### Discussion

If the receiver is not a double-buffered context, this call does nothing.

If the [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object used to create the context had a [`false`](https://developer.apple.com/documentation/Swift/false) backing store attribute (`NSOpenGLPFABackingStore`), the buffers may be exchanged rather than copied. This is often the case in full-screen mode.

According to the swap interval context attribute (see [`NSOpenGLCPSwapInterval`](nsopenglcpswapinterval.md)), the copy may take place during the vertical retrace of the monitor, rather than immediately after [`flushBuffer()`](nsopenglcontext/flushbuffer().md) is called. An implicit `glFlush` is done by [`flushBuffer()`](nsopenglcontext/flushbuffer().md) before it returns. For optimal performance, an application should not call `glFlush` immediately before calling [`flushBuffer()`](nsopenglcontext/flushbuffer().md). Subsequent OpenGL commands can be issued immediately after calling [`flushBuffer()`](nsopenglcontext/flushbuffer().md), but are not executed until the buffer copy is completed.

## See Also

- [func getValues(UnsafeMutablePointer<GLint>, for: NSOpenGLContext.Parameter)](nsopenglcontext/getvalues(_:for:).md)
  Returns the value of the requested parameter.
- [init?(format: NSOpenGLPixelFormat, share: NSOpenGLContext?)](nsopenglcontext/init(format:share:).md)
  Returns an OpenGL context object initialized with the specified pixel format information.
- [func setValues(UnsafePointer<GLint>, for: NSOpenGLContext.Parameter)](nsopenglcontext/setvalues(_:for:).md)
  Sets the value of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/flushbuffer())*