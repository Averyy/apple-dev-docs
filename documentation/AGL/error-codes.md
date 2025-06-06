# Error Codes

**Framework**: AGL

Defines the error codes that can be returned by the [`aglGetError`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15037)) function.

#### Overview

Unlike many Carbon APIs, AGL functions don’t return result codes for specific error conditions. Instead, AGL functions that fail either return `GL_FALSE` or `NULL`. You can find out the specific nature of the error by calling the function [`aglGetError`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15037)), which returns the appropriate error code.

## Topics

### Constants
- [var AGL_NO_ERROR: Int32](agl_no_error.md)
  No error.
- [var AGL_BAD_ATTRIBUTE: Int32](agl_bad_attribute.md)
  Invalid pixel format attribute.
- [var AGL_BAD_PROPERTY: Int32](agl_bad_property.md)
  Invalid renderer property.
- [var AGL_BAD_PIXELFMT: Int32](agl_bad_pixelfmt.md)
  Invalid pixel format.
- [var AGL_BAD_RENDINFO: Int32](agl_bad_rendinfo.md)
  Invalid renderer info.
- [var AGL_BAD_CONTEXT: Int32](agl_bad_context.md)
  Invalid rendering context.
- [var AGL_BAD_DRAWABLE: Int32](agl_bad_drawable.md)
- [var AGL_BAD_GDEV: Int32](agl_bad_gdev.md)
  Invalid graphics device.
- [var AGL_BAD_STATE: Int32](agl_bad_state.md)
  Invalid rendering context state.
- [var AGL_BAD_VALUE: Int32](agl_bad_value.md)
  Invalid numerical value.
- [var AGL_BAD_MATCH: Int32](agl_bad_match.md)
  Invalid share rendering context.
- [var AGL_BAD_ENUM: Int32](agl_bad_enum.md)
  Invalid enumerant.
- [var AGL_BAD_OFFSCREEN: Int32](agl_bad_offscreen.md)
  Invalid offscreen drawable object.
- [var AGL_BAD_FULLSCREEN: Int32](agl_bad_fullscreen.md)
  Invalid full-screen drawable object.
- [var AGL_BAD_WINDOW: Int32](agl_bad_window.md)
  Invalid window.
- [var AGL_BAD_POINTER: Int32](agl_bad_pointer.md)
  Invalid pointer.
- [var AGL_BAD_MODULE: Int32](agl_bad_module.md)
  Invalid code module.
- [var AGL_BAD_ALLOC: Int32](agl_bad_alloc.md)
  Memory allocation failure.
- [var AGL_BAD_CONNECTION: Int32](agl_bad_connection.md)
  Unable to connect to the window server.
- [var AGL_NO_ERROR: Int32](agl_no_error.md)
  No error.
- [var AGL_BAD_ATTRIBUTE: Int32](agl_bad_attribute.md)
  Invalid pixel format attribute.
- [var AGL_BAD_PROPERTY: Int32](agl_bad_property.md)
  Invalid renderer property.
- [var AGL_BAD_PIXELFMT: Int32](agl_bad_pixelfmt.md)
  Invalid pixel format.
- [var AGL_BAD_RENDINFO: Int32](agl_bad_rendinfo.md)
  Invalid renderer info.
- [var AGL_BAD_CONTEXT: Int32](agl_bad_context.md)
  Invalid rendering context.
- [var AGL_BAD_DRAWABLE: Int32](agl_bad_drawable.md)
- [var AGL_BAD_GDEV: Int32](agl_bad_gdev.md)
  Invalid graphics device.
- [var AGL_BAD_STATE: Int32](agl_bad_state.md)
  Invalid rendering context state.
- [var AGL_BAD_VALUE: Int32](agl_bad_value.md)
  Invalid numerical value.
- [var AGL_BAD_MATCH: Int32](agl_bad_match.md)
  Invalid share rendering context.
- [var AGL_BAD_ENUM: Int32](agl_bad_enum.md)
  Invalid enumerant.
- [var AGL_BAD_OFFSCREEN: Int32](agl_bad_offscreen.md)
  Invalid offscreen drawable object.
- [var AGL_BAD_FULLSCREEN: Int32](agl_bad_fullscreen.md)
  Invalid full-screen drawable object.
- [var AGL_BAD_WINDOW: Int32](agl_bad_window.md)
  Invalid window.
- [var AGL_BAD_POINTER: Int32](agl_bad_pointer.md)
  Invalid pointer.
- [var AGL_BAD_MODULE: Int32](agl_bad_module.md)
  Invalid code module.
- [var AGL_BAD_ALLOC: Int32](agl_bad_alloc.md)
  Memory allocation failure.
- [var AGL_BAD_CONNECTION: Int32](agl_bad_connection.md)
  Unable to connect to the window server.

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
- [Globally Configured Options](globally-configured-options.md)
  Specify options that apply globally.
- [Renderer Attributes](renderer-attributes.md)
  Define options for managing renderers.
- [Renderer IDs](renderer-ids.md)
  Define constants that specify hardware and software renderers.
- [Renderer Properties](renderer-properties.md)
  Specify constants that you can use to query renderer properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/error-codes)*