# Buffer and Renderer Attributes

**Framework**: AGL

Specify attributes used to create a pixel format object.

#### Overview

Each of these constants can be assigned to the the attribute array passed to the function [`AGL`](agl-collection.md). They can also be passed to the function [`AGL`](agl-collection.md).

## Topics

### Constants
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
- [var AGL_GREEN_SIZE: Int32](agl_green_size.md)
  The associated value is a nonnegative integer that specifies the number of green component bits. The value is `0` if the `AGL_RGBA` attribute is `GL_FALSE`. A green buffer that most closely matches the specified size is preferred.
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
- [var AGL_ACCUM_BLUE_SIZE: Int32](agl_accum_blue_size.md)
  The associated value is a nonnegative integer that specifies the number of bits of blue stored in the accumulation buffer. A blue accumulation buffer that most closely matches the specified size is preferred.
- [var AGL_ACCUM_ALPHA_SIZE: Int32](agl_accum_alpha_size.md)
  The associated value is a nonnegative integer that specifies the number of bits of alpha stored in the accumulation buffer. An alpha accumulation buffer that most closely matches the specified size is preferred.
- [var AGL_PIXEL_SIZE: Int32](agl_pixel_size.md)
- [var AGL_MINIMUM_POLICY: Int32](agl_minimum_policy.md)
  This constant is a Boolean attribute. If it is present in the attributes array, the pixel format choosing policy is altered for the color, depth, and accumulation buffers such that only buffers of size greater than or equal to the desired size are considered. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_MAXIMUM_POLICY: Int32](agl_maximum_policy.md)
- [var AGL_OFFSCREEN: Int32](agl_offscreen.md)
- [var AGL_FULLSCREEN: Int32](agl_fullscreen.md)
- [var AGL_SAMPLE_BUFFERS_ARB: Int32](agl_sample_buffers_arb.md)
  The associated value is the number of multisample buffers.
- [var AGL_SAMPLES_ARB: Int32](agl_samples_arb.md)
  The associated value is the number of samples per multisample buffer.
- [var AGL_AUX_DEPTH_STENCIL: Int32](agl_aux_depth_stencil.md)
  The associated value is the independent depth and/or the stencil buffers for the auxiliary buffer.
- [var AGL_COLOR_FLOAT: Int32](agl_color_float.md)
  This constant is a Boolean attribute. If it is present in the attributes array, color buffers store floating-point pixels. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_MULTISAMPLE: Int32](agl_multisample.md)
  This constant is a Boolean attribute. If it is present in the attributes array,  specifies a hint to the driver to prefer multisampling. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_SUPERSAMPLE: Int32](agl_supersample.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies a hint to the driver to prefer supersampling. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_SAMPLE_ALPHA: Int32](agl_sample_alpha.md)
  This constant is a Boolean attribute. If it is present in the attributes array, request alpha filtering when multisampling. Do not supply a value with this constant because its presence in the array implies `true`.
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
- [var AGL_GREEN_SIZE: Int32](agl_green_size.md)
  The associated value is a nonnegative integer that specifies the number of green component bits. The value is `0` if the `AGL_RGBA` attribute is `GL_FALSE`. A green buffer that most closely matches the specified size is preferred.
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
- [var AGL_ACCUM_BLUE_SIZE: Int32](agl_accum_blue_size.md)
  The associated value is a nonnegative integer that specifies the number of bits of blue stored in the accumulation buffer. A blue accumulation buffer that most closely matches the specified size is preferred.
- [var AGL_ACCUM_ALPHA_SIZE: Int32](agl_accum_alpha_size.md)
  The associated value is a nonnegative integer that specifies the number of bits of alpha stored in the accumulation buffer. An alpha accumulation buffer that most closely matches the specified size is preferred.
- [var AGL_PIXEL_SIZE: Int32](agl_pixel_size.md)
- [var AGL_MINIMUM_POLICY: Int32](agl_minimum_policy.md)
  This constant is a Boolean attribute. If it is present in the attributes array, the pixel format choosing policy is altered for the color, depth, and accumulation buffers such that only buffers of size greater than or equal to the desired size are considered. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_MAXIMUM_POLICY: Int32](agl_maximum_policy.md)
- [var AGL_OFFSCREEN: Int32](agl_offscreen.md)
- [var AGL_FULLSCREEN: Int32](agl_fullscreen.md)
- [var AGL_SAMPLE_BUFFERS_ARB: Int32](agl_sample_buffers_arb.md)
  The associated value is the number of multisample buffers.
- [var AGL_SAMPLES_ARB: Int32](agl_samples_arb.md)
  The associated value is the number of samples per multisample buffer.
- [var AGL_AUX_DEPTH_STENCIL: Int32](agl_aux_depth_stencil.md)
  The associated value is the independent depth and/or the stencil buffers for the auxiliary buffer.
- [var AGL_COLOR_FLOAT: Int32](agl_color_float.md)
  This constant is a Boolean attribute. If it is present in the attributes array, color buffers store floating-point pixels. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_MULTISAMPLE: Int32](agl_multisample.md)
  This constant is a Boolean attribute. If it is present in the attributes array,  specifies a hint to the driver to prefer multisampling. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_SUPERSAMPLE: Int32](agl_supersample.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies a hint to the driver to prefer supersampling. Do not supply a value with this constant because its presence in the array implies `true`.
- [var AGL_SAMPLE_ALPHA: Int32](agl_sample_alpha.md)
  This constant is a Boolean attribute. If it is present in the attributes array, request alpha filtering when multisampling. Do not supply a value with this constant because its presence in the array implies `true`.

## See Also

- [Bit Depths](bit-depths.md)
  Define resolutions for the depth and stencil buffers.
- [Buffer Mode Flags](buffer-mode-flags.md)
  Define constants used to set buffer modes.
- [Color Modes](color-modes.md)
  Specify formats and color channel layout information for the color  buffer.
- [Context Options and Parameters](context-options-and-parameters.md)
  Define options and parameters that apply to a specific rendering context.
- [Error Codes](error-codes.md)
  Defines the error codes that can be returned by the [`aglGetError`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15037)) function.
- [Globally Configured Options](globally-configured-options.md)
  Specify options that apply globally.
- [Renderer Attributes](renderer-attributes.md)
  Define options for managing renderers.
- [Renderer IDs](renderer-ids.md)
  Define constants that specify hardware and software renderers.
- [Renderer Properties](renderer-properties.md)
  Specify constants that you can use to query renderer properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/buffer-and-renderer-attributes)*