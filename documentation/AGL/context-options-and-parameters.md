# Context Options and Parameters

**Framework**: AGL

Define options and parameters that apply to a specific rendering context.

## Topics

### Constants
- [var AGL_SWAP_RECT: Int32](agl_swap_rect.md)
- [var AGL_BUFFER_RECT: Int32](agl_buffer_rect.md)
- [var AGL_SWAP_LIMIT: Int32](agl_swap_limit.md)
  Enable or disable the swap asynchronous limit.
- [var AGL_COLORMAP_TRACKING: Int32](agl_colormap_tracking.md)
  Enable or disable color map tracking.
- [var AGL_COLORMAP_ENTRY: Int32](agl_colormap_entry.md)
  The associated value is a color map entry specifies as {`index, r, g, b}`.
- [var AGL_RASTERIZATION: Int32](agl_rasterization.md)
  Enable or disable all rasterization of 2D and 3D primitives. You can use this option to debug and characterize the performance of an OpenGL driver without actually rendering.
- [var AGL_SWAP_INTERVAL: Int32](agl_swap_interval.md)
  The associated parameter contains one value: the current swap interval setting. A value of `0`   specifies not to synchronize to the vertical retrace. All other values indicate to synchronize to the vertical retrace.
- [var AGL_STATE_VALIDATION: Int32](agl_state_validation.md)
- [var AGL_BUFFER_NAME: Int32](agl_buffer_name.md)
  The associated value is a buffer name. You can use this option to allow multiple OpenGL contexts to share a buffer.
- [var AGL_ORDER_CONTEXT_TO_FRONT: Int32](agl_order_context_to_front.md)
  Specifies to order the current rendering context in front of all the other contexts.
- [var AGL_CONTEXT_SURFACE_ID: Int32](agl_context_surface_id.md)
  The associated value is the ID of the drawable surface for the rendering context. You can’t set this value because the system sets it. However, you can retrieve the value using the function [`aglGetInteger`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15035)).
- [var AGL_CONTEXT_DISPLAY_ID: Int32](agl_context_display_id.md)
- [var AGL_SURFACE_ORDER: Int32](agl_surface_order.md)
  The associated value is the position of the OpenGL surface relative to the window. A value of `1` means that the position is above the window; a value of `–1` specifies a position that is below the window.
- [var AGL_SURFACE_OPACITY: Int32](agl_surface_opacity.md)
  The associated value specifies the opacity of the OpenGL surface. A value of `1` means the surface is opaque (the default); `0` means completely transparent.
- [var AGL_CLIP_REGION: Int32](agl_clip_region.md)
  Enables or sets the drawable clipping region. The associated value is a `rgnHandle` data type that defines the clipping region.
- [var AGL_FS_CAPTURE_SINGLE: Int32](agl_fs_capture_single.md)
  Enables the capture of a single display for full-screen rendering. This option is disabled by default.
- [var AGL_SURFACE_BACKING_SIZE: Int32](agl_surface_backing_size.md)
  The associated value specifies the width and height of surface backing size.
- [var AGL_ENABLE_SURFACE_BACKING_SIZE: Int32](agl_enable_surface_backing_size.md)
  Enable or disable the surface backing-size override.
- [var AGL_SURFACE_VOLATILE: Int32](agl_surface_volatile.md)
  Flags the surface as a candidate for deletion.
- [var AGL_SWAP_RECT: Int32](agl_swap_rect.md)
- [var AGL_BUFFER_RECT: Int32](agl_buffer_rect.md)
- [var AGL_SWAP_LIMIT: Int32](agl_swap_limit.md)
  Enable or disable the swap asynchronous limit.
- [var AGL_COLORMAP_TRACKING: Int32](agl_colormap_tracking.md)
  Enable or disable color map tracking.
- [var AGL_COLORMAP_ENTRY: Int32](agl_colormap_entry.md)
  The associated value is a color map entry specifies as {`index, r, g, b}`.
- [var AGL_RASTERIZATION: Int32](agl_rasterization.md)
  Enable or disable all rasterization of 2D and 3D primitives. You can use this option to debug and characterize the performance of an OpenGL driver without actually rendering.
- [var AGL_SWAP_INTERVAL: Int32](agl_swap_interval.md)
  The associated parameter contains one value: the current swap interval setting. A value of `0`   specifies not to synchronize to the vertical retrace. All other values indicate to synchronize to the vertical retrace.
- [var AGL_STATE_VALIDATION: Int32](agl_state_validation.md)
- [var AGL_BUFFER_NAME: Int32](agl_buffer_name.md)
  The associated value is a buffer name. You can use this option to allow multiple OpenGL contexts to share a buffer.
- [var AGL_ORDER_CONTEXT_TO_FRONT: Int32](agl_order_context_to_front.md)
  Specifies to order the current rendering context in front of all the other contexts.
- [var AGL_CONTEXT_SURFACE_ID: Int32](agl_context_surface_id.md)
  The associated value is the ID of the drawable surface for the rendering context. You can’t set this value because the system sets it. However, you can retrieve the value using the function [`aglGetInteger`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15035)).
- [var AGL_CONTEXT_DISPLAY_ID: Int32](agl_context_display_id.md)
- [var AGL_SURFACE_ORDER: Int32](agl_surface_order.md)
  The associated value is the position of the OpenGL surface relative to the window. A value of `1` means that the position is above the window; a value of `–1` specifies a position that is below the window.
- [var AGL_SURFACE_OPACITY: Int32](agl_surface_opacity.md)
  The associated value specifies the opacity of the OpenGL surface. A value of `1` means the surface is opaque (the default); `0` means completely transparent.
- [var AGL_CLIP_REGION: Int32](agl_clip_region.md)
  Enables or sets the drawable clipping region. The associated value is a `rgnHandle` data type that defines the clipping region.
- [var AGL_FS_CAPTURE_SINGLE: Int32](agl_fs_capture_single.md)
  Enables the capture of a single display for full-screen rendering. This option is disabled by default.
- [var AGL_SURFACE_BACKING_SIZE: Int32](agl_surface_backing_size.md)
  The associated value specifies the width and height of surface backing size.
- [var AGL_ENABLE_SURFACE_BACKING_SIZE: Int32](agl_enable_surface_backing_size.md)
  Enable or disable the surface backing-size override.
- [var AGL_SURFACE_VOLATILE: Int32](agl_surface_volatile.md)
  Flags the surface as a candidate for deletion.

## See Also

- [Bit Depths](bit-depths.md)
  Define resolutions for the depth and stencil buffers.
- [Buffer and Renderer Attributes](buffer-and-renderer-attributes.md)
  Specify attributes used to create a pixel format object.
- [Buffer Mode Flags](buffer-mode-flags.md)
  Define constants used to set buffer modes.
- [Color Modes](color-modes.md)
  Specify formats and color channel layout information for the color  buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/agl/context-options-and-parameters)*