# AGL_GREEN_SIZE

**Framework**: AGL  
**Kind**: var

The associated value is a nonnegative integer that specifies the number of green component bits. The value is `0` if the `AGL_RGBA` attribute is `GL_FALSE`. A green buffer that most closely matches the specified size is preferred.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var AGL_GREEN_SIZE: Int32 { get }
```

## See Also

- [var AGL_NONE: Int32](agl_none.md)
  Used to terminate a pixel format attribute list.
- [var AGL_ALL_RENDERERS: Int32](agl_all_renderers.md)
  This constant is a Boolean attribute. If it is present in the attributes array, pixel format selection is open to all available renderers, including debug and special-purpose renderers that are not OpenGL compliant. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_BUFFER_SIZE: Int32](agl_buffer_size.md)
- [var AGL_LEVEL: Int32](agl_level.md)
- [var AGL_RGBA: Int32](agl_rgba.md)
- [var AGL_DOUBLEBUFFER: Int32](agl_doublebuffer.md)
  This constant is a Boolean attribute. If it is present in the attributes array, only double-buffered pixel formats are considered. Otherwise, only single-buffered pixel formats are considered. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_STEREO: Int32](agl_stereo.md)
  This constant is a Boolean attribute. If it is present in the attributes array, only stereo pixel formats are considered. Otherwise, only monoscopic pixel formats are considered. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_AUX_BUFFERS: Int32](agl_aux_buffers.md)
- [var AGL_RED_SIZE: Int32](agl_red_size.md)
  The associated value is a nonnegative integer that specifies the number of red component bits. The value is `0` if the `AGL_RGBA` attribute is `GL_FALSE`. A red buffer that most closely matches the specified size is preferred.
- [var AGL_BLUE_SIZE: Int32](agl_blue_size.md)
  The associated value is a nonnegative integer that specifies the number of blue component bits. The value is `0` if the `AGL_RGBA` attribute is `GL_FALSE`. A blue buffer that most closely matches the specified size is preferred.
- [var AGL_ALPHA_SIZE: Int32](agl_alpha_size.md)
  The associated value is a nonnegative integer that specifies the number of alpha component bits. The value is `0` if the `AGL_RGBA` attribute is `GL_FALSE`. An alpha buffer that most closely matches the specified size is preferred.
- [var AGL_DEPTH_SIZE: Int32](agl_depth_size.md)
  The associated value is a nonnegative integer that specifies the number of bits in the depth buffer. A depth buffer that most closely matches the specified size is preferred.
- [var AGL_STENCIL_SIZE: Int32](agl_stencil_size.md)
  The associated value is a nonnegative integer that specifies the number of bits in the stencil buffer. The smallest stencil buffer of at least the specified size is preferred.
- [var AGL_ACCUM_RED_SIZE: Int32](agl_accum_red_size.md)
  The associated value is a nonnegative integer that specifies the number of bits of red stored in the accumulation buffer. A red accumulation buffer that most closely matches the specified size is preferred.
- [var AGL_ACCUM_GREEN_SIZE: Int32](agl_accum_green_size.md)
  The associated value is a nonnegative integer that specifies the number of bits of green stored in the accumulation buffer. A green accumulation buffer that most closely matches the specified size is preferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/agl_green_size)*