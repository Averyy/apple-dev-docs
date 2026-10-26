# NSOpenGLPFAWindow

**Framework**: AppKit  
**Kind**: case  
**Role**: Enumeration Case

A Boolean attribute. If present, this attribute indicates that only renderers that are capable of rendering to a window are considered. This attribute is implied if neither `NSOpenGLPFAFullScreen` nor `NSOpenGLPFAOffScreen` is specified.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

## Declaration

```c
NSOpenGLPFAWindow
```

## See Also

### Constants
- [var NSOpenGLPFAAccelerated: Int](./nsopenglpfaaccelerated.md)
  A Boolean attribute. If present, this attribute indicates that only hardware-accelerated renderers are considered. If not present, accelerated renderers are still preferred.
- [var NSOpenGLPFAAcceleratedCompute: Int](./nsopenglpfaacceleratedcompute.md)
  If present, this attribute indicates that only renderers that can execute OpenCL programs should be used.
- [var NSOpenGLPFAAccumSize: Int](./nsopenglpfaaccumsize.md)
  Value is a nonnegative buffer size specification. An accumulation buffer that most closely matches the specified size is preferred.
- [var NSOpenGLPFAAllRenderers: Int](./nsopenglpfaallrenderers.md)
  A Boolean attribute. If present, this attribute indicates that the pixel format selection is open to all available renderers, including debug and special-purpose renderers that are not OpenGL compliant.
- [var NSOpenGLPFAAllowOfflineRenderers: Int](./nsopenglpfaallowofflinerenderers.md)
  A Boolean attribute. If present, this attribute indicates that offline renderers may be used.
- [var NSOpenGLPFAAlphaSize: Int](./nsopenglpfaalphasize.md)
  Value is a nonnegative buffer size specification. An alpha buffer that most closely matches the specified size is preferred.
- [var NSOpenGLPFAAuxBuffers: Int](./nsopenglpfaauxbuffers.md)
  Value is a nonnegative integer that indicates the desired number of auxiliary buffers. Pixel formats with the smallest number of auxiliary buffers that meets or exceeds the specified number are preferred.
- [var NSOpenGLPFAAuxDepthStencil: Int](./nsopenglpfaauxdepthstencil.md)
  Each auxiliary buffer has its own depth stencil.
- [var NSOpenGLPFABackingStore: Int](./nsopenglpfabackingstore.md)
  A Boolean attribute. If present, this attribute indicates that OpenGL only considers renderers that have a back color buffer the full size of the drawable (regardless of window visibility) and that guarantee the back buffer contents to be valid after a call to `NSOpenGLContext` object’s [`flushBuffer()`](./nsopenglcontext/flushbuffer%28%29.md).
- [var NSOpenGLPFAClosestPolicy: Int](./nsopenglpfaclosestpolicy.md)
  A Boolean attribute. If present, this attribute indicates that the pixel format choosing policy is altered for the color buffer such that the buffer closest to the requested size is preferred, regardless of the actual color buffer depth of the supported graphics device.
- [var NSOpenGLPFAColorFloat: Int](./nsopenglpfacolorfloat.md)
- [var NSOpenGLPFAColorSize: Int](./nsopenglpfacolorsize.md)
  Value is a nonnegative buffer size specification. A color buffer that most closely matches the specified size is preferred. If unspecified, OpenGL chooses a color size that matches the screen.
- [NSOpenGLPFACompliant](./nsopenglpfacompliant.md)
  A Boolean attribute. If present, this attribute indicates that pixel format selection is only open to OpenGL-compliant renderers. This attribute is implied unless `NSOpenGLPFAAllRenderers` is specified. This attribute is not useful in the attribute array.
- [var NSOpenGLPFADepthSize: Int](./nsopenglpfadepthsize.md)
  Value is a nonnegative depth buffer size specification. A depth buffer that most closely matches the specified size is preferred.
- [var NSOpenGLPFADoubleBuffer: Int](./nsopenglpfadoublebuffer.md)
  A Boolean attribute. If present, this attribute indicates that only double-buffered pixel formats are considered. Otherwise, only single-buffered pixel formats are considered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpfawindow)*