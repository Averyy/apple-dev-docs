# OpenGL Pixel Format Attributes

**Framework**: AppKit

Pixel format attributes for OpenGL.

## Topics

### Constants
- [var NSOpenGLPFAAccelerated: Int](nsopenglpfaaccelerated.md)
  A Boolean attribute. If present, this attribute indicates that only hardware-accelerated renderers are considered. If not present, accelerated renderers are still preferred.
- [var NSOpenGLPFAAcceleratedCompute: Int](nsopenglpfaacceleratedcompute.md)
  If present, this attribute indicates that only renderers that can execute OpenCL programs should be used.
- [var NSOpenGLPFAAccumSize: Int](nsopenglpfaaccumsize.md)
  Value is a nonnegative buffer size specification. An accumulation buffer that most closely matches the specified size is preferred.
- [var NSOpenGLPFAAllRenderers: Int](nsopenglpfaallrenderers.md)
  A Boolean attribute. If present, this attribute indicates that the pixel format selection is open to all available renderers, including debug and special-purpose renderers that are not OpenGL compliant.
- [var NSOpenGLPFAAllowOfflineRenderers: Int](nsopenglpfaallowofflinerenderers.md)
  A Boolean attribute. If present, this attribute indicates that offline renderers may be used.
- [var NSOpenGLPFAAlphaSize: Int](nsopenglpfaalphasize.md)
  Value is a nonnegative buffer size specification. An alpha buffer that most closely matches the specified size is preferred.
- [var NSOpenGLPFAAuxBuffers: Int](nsopenglpfaauxbuffers.md)
  Value is a nonnegative integer that indicates the desired number of auxiliary buffers. Pixel formats with the smallest number of auxiliary buffers that meets or exceeds the specified number are preferred.
- [var NSOpenGLPFAAuxDepthStencil: Int](nsopenglpfaauxdepthstencil.md)
  Each auxiliary buffer has its own depth stencil.
- [var NSOpenGLPFABackingStore: Int](nsopenglpfabackingstore.md)
  A Boolean attribute. If present, this attribute indicates that OpenGL only considers renderers that have a back color buffer the full size of the drawable (regardless of window visibility) and that guarantee the back buffer contents to be valid after a call to `NSOpenGLContext` object’s [`flushBuffer()`](nsopenglcontext/flushbuffer().md).
- [var NSOpenGLPFAClosestPolicy: Int](nsopenglpfaclosestpolicy.md)
  A Boolean attribute. If present, this attribute indicates that the pixel format choosing policy is altered for the color buffer such that the buffer closest to the requested size is preferred, regardless of the actual color buffer depth of the supported graphics device.
- [var NSOpenGLPFAColorFloat: Int](nsopenglpfacolorfloat.md)
- [var NSOpenGLPFAColorSize: Int](nsopenglpfacolorsize.md)
  Value is a nonnegative buffer size specification. A color buffer that most closely matches the specified size is preferred. If unspecified, OpenGL chooses a color size that matches the screen.
- [var NSOpenGLPFADepthSize: Int](nsopenglpfadepthsize.md)
  Value is a nonnegative depth buffer size specification. A depth buffer that most closely matches the specified size is preferred.
- [var NSOpenGLPFADoubleBuffer: Int](nsopenglpfadoublebuffer.md)
  A Boolean attribute. If present, this attribute indicates that only double-buffered pixel formats are considered. Otherwise, only single-buffered pixel formats are considered.
- [var NSOpenGLPFAMaximumPolicy: Int](nsopenglpfamaximumpolicy.md)
  A Boolean attribute. If present, this attribute indicates that the pixel format choosing policy is altered for the color, depth, and accumulation buffers such that, if a nonzero buffer size is requested, the largest available buffer is preferred.
- [var NSOpenGLPFAMinimumPolicy: Int](nsopenglpfaminimumpolicy.md)
  A Boolean attribute. If present, this attribute indicates that the pixel format choosing policy is altered for the color, depth, and accumulation buffers such that only buffers of size greater than or equal to the desired size are considered.
- [var NSOpenGLPFAMultisample: Int](nsopenglpfamultisample.md)
- [var NSOpenGLPFANoRecovery: Int](nsopenglpfanorecovery.md)
- [var NSOpenGLPFAOpenGLProfile: Int](nsopenglpfaopenglprofile.md)
  A constant that represents an OpenGL profile.
- [var NSOpenGLPFARendererID: Int](nsopenglpfarendererid.md)
- [var NSOpenGLPFASampleAlpha: Int](nsopenglpfasamplealpha.md)
  A Boolean attribute. If present and used with [`NSOpenGLPFASampleBuffers`](nsopenglpfasamplebuffers.md) and [`NSOpenGLPFASampleBuffers`](nsopenglpfasamplebuffers.md), this attribute hints to OpenGL to update multi-sample alpha values to ensure the most accurate rendering. If pixel format is not requesting antialiasing then this hint does nothing.
- [var NSOpenGLPFASampleBuffers: Int](nsopenglpfasamplebuffers.md)
  Value is a nonnegative number indicating the number of multisample buffers.
- [var NSOpenGLPFASamples: Int](nsopenglpfasamples.md)
  Value is a nonnegative indicating the number of samples per multisample buffer.
- [var NSOpenGLPFAScreenMask: Int](nsopenglpfascreenmask.md)
- [var NSOpenGLPFAStencilSize: Int](nsopenglpfastencilsize.md)
  Value is a nonnegative integer that indicates the desired number of stencil bitplanes. The smallest stencil buffer of at least the specified size is preferred.
- [var NSOpenGLPFAStereo: Int](nsopenglpfastereo.md)
  A Boolean attribute. If present, this attribute indicates that only stereo pixel formats are considered. Otherwise, only monoscopic pixel formats are considered.
- [var NSOpenGLPFASupersample: Int](nsopenglpfasupersample.md)
- [var NSOpenGLPFATripleBuffer: Int](nsopenglpfatriplebuffer.md)
  A Boolean attribute. If present, this attribute indicates that only triple-buffered pixel formats are considered. Otherwise, only single-buffered pixel formats are considered.
- [var NSOpenGLPFAVirtualScreenCount: Int](nsopenglpfavirtualscreencount.md)
  The number of virtual screens in this format.

## See Also

- [typealias NSOpenGLPixelFormatAttribute](nsopenglpixelformatattribute.md)
  Pixel format attributes for OpenGL.
- [OpenGL Profiles](opengl-profiles.md)
  Constants that specify the functionality provided by the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/opengl-pixel-format-attributes)*