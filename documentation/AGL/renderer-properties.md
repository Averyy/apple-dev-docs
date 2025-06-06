# Renderer Properties

**Framework**: AGL

Specify constants that you can use to query renderer properties.

#### Overview

You can pass these constants to the function [`AGL`](agl-collection.md) to find out the property value for a specific renderer.

## Topics

### Constants
- [var AGL_BUFFER_MODES: Int32](agl_buffer_modes.md)
  The associated value can be a bitwise `OR` of the any of the constants specified in [`Buffer Mode Flags`](buffer-mode-flags.md).
- [var AGL_MIN_LEVEL: Int32](agl_min_level.md)
  The associated value specifies the minimum overlay buffer level. Negative values indicate an underlay buffer.
- [var AGL_MAX_LEVEL: Int32](agl_max_level.md)
  The associated value specifies the maximum overlay buffer level.
- [var AGL_COLOR_MODES: Int32](agl_color_modes.md)
  The associated value can be a bitwise `OR` of any of the constants specified in [`Color Modes`](color-modes.md).
- [var AGL_ACCUM_MODES: Int32](agl_accum_modes.md)
  The associated value can be a bitwise `OR` of any of the constants specified in [`Color Modes`](color-modes.md).
- [var AGL_DEPTH_MODES: Int32](agl_depth_modes.md)
  The associated value can be the bitwise `OR` of any of the constants specified in [`Bit Depths`](bit-depths.md).
- [var AGL_STENCIL_MODES: Int32](agl_stencil_modes.md)
  The associated value can be the bitwise `OR` of any of the constants specified in [`Bit Depths`](bit-depths.md).
- [var AGL_MAX_AUX_BUFFERS: Int32](agl_max_aux_buffers.md)
  The associated value is the maximum number of auxiliary buffers that can be supported by the renderer.
- [var AGL_VIDEO_MEMORY: Int32](agl_video_memory.md)
  The associated value is the amount of video memory.
- [var AGL_TEXTURE_MEMORY: Int32](agl_texture_memory.md)
  The associated value is the amount of texture memory.
- [var AGL_RENDERER_COUNT: Int32](agl_renderer_count.md)
  The associated value is the number of renderers.
- [var AGL_BUFFER_MODES: Int32](agl_buffer_modes.md)
  The associated value can be a bitwise `OR` of the any of the constants specified in [`Buffer Mode Flags`](buffer-mode-flags.md).
- [var AGL_MIN_LEVEL: Int32](agl_min_level.md)
  The associated value specifies the minimum overlay buffer level. Negative values indicate an underlay buffer.
- [var AGL_MAX_LEVEL: Int32](agl_max_level.md)
  The associated value specifies the maximum overlay buffer level.
- [var AGL_COLOR_MODES: Int32](agl_color_modes.md)
  The associated value can be a bitwise `OR` of any of the constants specified in [`Color Modes`](color-modes.md).
- [var AGL_ACCUM_MODES: Int32](agl_accum_modes.md)
  The associated value can be a bitwise `OR` of any of the constants specified in [`Color Modes`](color-modes.md).
- [var AGL_DEPTH_MODES: Int32](agl_depth_modes.md)
  The associated value can be the bitwise `OR` of any of the constants specified in [`Bit Depths`](bit-depths.md).
- [var AGL_STENCIL_MODES: Int32](agl_stencil_modes.md)
  The associated value can be the bitwise `OR` of any of the constants specified in [`Bit Depths`](bit-depths.md).
- [var AGL_MAX_AUX_BUFFERS: Int32](agl_max_aux_buffers.md)
  The associated value is the maximum number of auxiliary buffers that can be supported by the renderer.
- [var AGL_VIDEO_MEMORY: Int32](agl_video_memory.md)
  The associated value is the amount of video memory.
- [var AGL_TEXTURE_MEMORY: Int32](agl_texture_memory.md)
  The associated value is the amount of texture memory.
- [var AGL_RENDERER_COUNT: Int32](agl_renderer_count.md)
  The associated value is the number of renderers.

## See Also

- [Bit Depths](bit-depths.md)
  Define resolutions for the depth and stencil buffers.
- [Buffer and Renderer Attributes](buffer-and-renderer-attributes.md)
  Specify attributes used to create a pixel format object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/renderer-properties)*