# setOffScreen:width:height:rowbytes:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Instructs the OpenGL context to render into an offscreen buffer with the specified attributes.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use a OpenGL framebuffer object instead.

## Declaration

```objc
- (void) setOffScreen:(void *) baseaddr width:(GLsizei) width height:(GLsizei) height rowbytes:(GLint) rowbytes;
```

## Discussion

The receiver’s viewport is set to the full size of the offscreen area. Call the [`clearDrawable()`](./cleardrawable%28%29.md) method to exit offscreen mode.

The `NSOpenGLPFAOffScreen` attribute must have been specified in the receiver’s pixel format object.

> **Note**:  To obtain behavior similar to offscreen mode on renderers that do not support accelerated offscreen contexts, attach the context to a hidden window and use `glReadPixels`.

## Parameters

- `baseaddr`: The base address of the buffer in memory. This buffer must contain at least `rowbytes` `*` `height` bytes.
- `width`: The width of the memory buffer, measured in pixels.
- `height`: The height of the memory buffer, measured in pixels.
- `rowbytes`: The number of bytes in a single row of the buffer. This value must be greater than or equal to the value in `width` times the number of bytes per pixel.

## See Also

### Managing the Drawable Object
- [var view: NSView?](./view.md)
  Returns the OpenGL context’s view.
- [- setFullScreen](./setfullscreen.md)
  Sets the OpenGL context to full-screen mode.
- [func clearDrawable()](./cleardrawable%28%29.md)
  Disassociates the OpenGL context from its viewport.
- [func update()](./update%28%29.md)
  Updates the OpenGL context’s drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/setoffscreen:width:height:rowbytes:)*