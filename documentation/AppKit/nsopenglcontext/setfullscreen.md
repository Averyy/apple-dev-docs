# setFullScreen

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the OpenGL context to full-screen mode.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Full-screen mode contexts are deprecated. See [Drawing to the Full Screen](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_fullscreen/opengl_cgl.html#//apple_ref/doc/uid/TP40001987-CH210).

## Declaration

```objc
- (void) setFullScreen;
```

## Discussion

In full-screen mode, the receiver renders onto the entire screen. The receiver’s viewport is set to the full size of the screen. Call the [`clearDrawable()`](./cleardrawable%28%29.md) method to exit full-screen mode.

The `NSOpenGLPFAFullScreen` attribute must have been specified in the receiver’s [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md). Some OpenGL renderers, like the software renderer, do not support full-screen mode. The following code determines if a full-screen pixel format is possible on a given system:

```objc
NSOpenGLPixelFormatAttribute attrs[] =
{
    NSOpenGLPFAFullScreen,
    nil
};
 
NSOpenGLPixelFormat* pixFmt = [[NSOpenGLPixelFormat alloc] initWithAttributes:attrs];
 
/* Check if initWithAttributes succeeded. */
if(pixFmt == nil) {
    /* initWithAttributes failed. There is no full-screen renderer.  */
}
```

> **Note**:  Use Core Graphics’s **Direct Display** API to capture the display before entering full-screen mode and release it after exiting. A captured display prevents contention from other applications and system services. In addition, applications are not notified of display changes, preventing them from repositioning their windows and the Finder from repositioning desktop icons.

## See Also

### Managing the Drawable Object
- [var view: NSView?](./view.md)
  Returns the OpenGL context’s view.
- [- setOffScreen:width:height:rowbytes:](./setoffscreen_width_height_rowbytes_.md)
  Instructs the OpenGL context to render into an offscreen buffer with the specified attributes.
- [func clearDrawable()](./cleardrawable%28%29.md)
  Disassociates the OpenGL context from its viewport.
- [func update()](./update%28%29.md)
  Updates the OpenGL context’s drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/setfullscreen)*