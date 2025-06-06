# Color Modes

**Framework**: AGL

Specify formats and color channel layout information for the color  buffer.

## Topics

### Constants
- [var AGL_RGB8_BIT: Int32](agl_rgb8_bit.md)
  Specifies a format that has 8 bits per pixel with an RGB channel layout:  RGB=7:0, inverse color map.
- [var AGL_RGB8_A8_BIT: Int32](agl_rgb8_a8_bit.md)
  Specifies an 8-8 ARGB bits per pixel format and the channels located in the following bits: A=7:0, RGB=7:0, inverse color map.
- [var AGL_BGR233_BIT: Int32](agl_bgr233_bit.md)
  Specifies a format that has 8 bits per pixel with an RGB channel layout, and the channels located in the following bits:  B=7:6, G=5:3, R=2:0
- [var AGL_BGR233_A8_BIT: Int32](agl_bgr233_a8_bit.md)
  Specifies an 8-8 ARGB bits per pixel format and the channels located in the following bits: A=7:0, B=7:6, G=5:3, R=2:0
- [var AGL_RGB332_BIT: Int32](agl_rgb332_bit.md)
  Specifies a format that has 8 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=7:5, G=4:2, B=1:0
- [var AGL_RGB332_A8_BIT: Int32](agl_rgb332_a8_bit.md)
  Specifies an 8-8 ARGB bits per pixel format and the channels located in the following bits: A=7:0, R=7:5, G=4:2, B=1:0
- [var AGL_RGB444_BIT: Int32](agl_rgb444_bit.md)
  Specifies a format that has 16 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=11:8, G=7:4, B=3:0
- [var AGL_ARGB4444_BIT: Int32](agl_argb4444_bit.md)
  Specifies a format that has 16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=15:12, R=11:8, G=7:4, B=3:0
- [var AGL_RGB444_A8_BIT: Int32](agl_rgb444_a8_bit.md)
  Specifies a format that has 8-16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=11:8, G=7:4, B=3:0
- [var AGL_RGB555_BIT: Int32](agl_rgb555_bit.md)
  Specifies a format that has 16 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=14:10, G=9:5, B=4:0. The top bit is not used.
- [var AGL_ARGB1555_BIT: Int32](agl_argb1555_bit.md)
  Specifies a format that has 16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=15, R=14:10, G=9:5, B=4:0
- [var AGL_RGB555_A8_BIT: Int32](agl_rgb555_a8_bit.md)
  Specifies a format that has 8-16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=14:10, G=9:5, B=4:0
- [var AGL_RGB565_BIT: Int32](agl_rgb565_bit.md)
  Specifies a format that has 16 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=15:11, G=10:5, B=4:0
- [var AGL_RGB565_A8_BIT: Int32](agl_rgb565_a8_bit.md)
  Specifies a format that has 8-16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=15:11, G=10:5, B=4:0
- [var AGL_RGB888_BIT: Int32](agl_rgb888_bit.md)
  Specifies a format that has 32 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=23:16, G=15:8, B=7:0; R, G, and B take 1 byte each.
- [var AGL_ARGB8888_BIT: Int32](agl_argb8888_bit.md)
  Specifies a format that has 32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=31:24, R=23:16, G=15:8, B=7:0
- [var AGL_RGB888_A8_BIT: Int32](agl_rgb888_a8_bit.md)
  Specifies a format that has 8-32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=23:16, G=15:8, B=7:0
- [var AGL_RGB101010_BIT: Int32](agl_rgb101010_bit.md)
  Specifies a format that has 32 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=29:20, G=19:10, B=9:0
- [var AGL_ARGB2101010_BIT: Int32](agl_argb2101010_bit.md)
  Specifies a format that has 32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=31:30 R=29:20, G=19:10, B=9:0
- [var AGL_RGB101010_A8_BIT: Int32](agl_rgb101010_a8_bit.md)
  Specifies a format that has 8-32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0 R=29:20, G=19:10, B=9:0
- [var AGL_RGB121212_BIT: Int32](agl_rgb121212_bit.md)
  Specifies a format that has 48 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=35:24, G=23:12, B=11:0
- [var AGL_ARGB12121212_BIT: Int32](agl_argb12121212_bit.md)
  Specifies a format that has 48 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=47:36, R=35:24, G=23:12, B=11:0
- [var AGL_RGB161616_BIT: Int32](agl_rgb161616_bit.md)
  Specifies a format that has 64 bits per pixel with an RGB channel layout, and the channels located in the following bits:  R=47:32, G=31:16, B=15:0
- [var AGL_ARGB16161616_BIT: Int32](agl_argb16161616_bit.md)
  Specifies a format that has 64 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=63:48, R=47:32, G=31:16, B=15:0
- [var AGL_INDEX8_BIT: Int32](agl_index8_bit.md)
  Specifies an 8-bit color look up table. (Deprecated)
- [var AGL_INDEX16_BIT: Int32](agl_index16_bit.md)
  Specifies an 16-bit color look up table. (Deprecated)
- [var AGL_RGBFLOAT64_BIT: Int32](agl_rgbfloat64_bit.md)
  Specifies a format that has 64 bits per pixel with an RGB channel layout, half-floating point values. (A half-float is a 16-bit floating-point value.)
- [var AGL_RGBAFLOAT64_BIT: Int32](agl_rgbafloat64_bit.md)
  Specifies a format that has 64 bits per pixel with an ARGB channel layout, half-floating point values. (A half-float is a 16-bit floating-point value.)
- [var AGL_RGBFLOAT128_BIT: Int32](agl_rgbfloat128_bit.md)
  Specifies a format that has 128 bits per pixel with an RGB channel layout, IEEE floating point values.
- [var AGL_RGBAFLOAT128_BIT: Int32](agl_rgbafloat128_bit.md)
  Specifies a format that has 128 bits per pixel with an ARGB channel layout, IEEE floating point values.
- [var AGL_RGBFLOAT256_BIT: Int32](agl_rgbfloat256_bit.md)
  Specifies a format that has 256 bits per pixel with an RGB channel layout, IEEE double values.
- [var AGL_RGBAFLOAT256_BIT: Int32](agl_rgbafloat256_bit.md)
  Specifies a format that has 256 bits per pixel with an ARGB channel layout, IEEE double values.
- [var AGL_RGB8_BIT: Int32](agl_rgb8_bit.md)
  Specifies a format that has 8 bits per pixel with an RGB channel layout:  RGB=7:0, inverse color map.
- [var AGL_RGB8_A8_BIT: Int32](agl_rgb8_a8_bit.md)
  Specifies an 8-8 ARGB bits per pixel format and the channels located in the following bits: A=7:0, RGB=7:0, inverse color map.
- [var AGL_BGR233_BIT: Int32](agl_bgr233_bit.md)
  Specifies a format that has 8 bits per pixel with an RGB channel layout, and the channels located in the following bits:  B=7:6, G=5:3, R=2:0
- [var AGL_BGR233_A8_BIT: Int32](agl_bgr233_a8_bit.md)
  Specifies an 8-8 ARGB bits per pixel format and the channels located in the following bits: A=7:0, B=7:6, G=5:3, R=2:0
- [var AGL_RGB332_BIT: Int32](agl_rgb332_bit.md)
  Specifies a format that has 8 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=7:5, G=4:2, B=1:0
- [var AGL_RGB332_A8_BIT: Int32](agl_rgb332_a8_bit.md)
  Specifies an 8-8 ARGB bits per pixel format and the channels located in the following bits: A=7:0, R=7:5, G=4:2, B=1:0
- [var AGL_RGB444_BIT: Int32](agl_rgb444_bit.md)
  Specifies a format that has 16 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=11:8, G=7:4, B=3:0
- [var AGL_ARGB4444_BIT: Int32](agl_argb4444_bit.md)
  Specifies a format that has 16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=15:12, R=11:8, G=7:4, B=3:0
- [var AGL_RGB444_A8_BIT: Int32](agl_rgb444_a8_bit.md)
  Specifies a format that has 8-16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=11:8, G=7:4, B=3:0
- [var AGL_RGB555_BIT: Int32](agl_rgb555_bit.md)
  Specifies a format that has 16 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=14:10, G=9:5, B=4:0. The top bit is not used.
- [var AGL_ARGB1555_BIT: Int32](agl_argb1555_bit.md)
  Specifies a format that has 16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=15, R=14:10, G=9:5, B=4:0
- [var AGL_RGB555_A8_BIT: Int32](agl_rgb555_a8_bit.md)
  Specifies a format that has 8-16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=14:10, G=9:5, B=4:0
- [var AGL_RGB565_BIT: Int32](agl_rgb565_bit.md)
  Specifies a format that has 16 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=15:11, G=10:5, B=4:0
- [var AGL_RGB565_A8_BIT: Int32](agl_rgb565_a8_bit.md)
  Specifies a format that has 8-16 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=15:11, G=10:5, B=4:0
- [var AGL_RGB888_BIT: Int32](agl_rgb888_bit.md)
  Specifies a format that has 32 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=23:16, G=15:8, B=7:0; R, G, and B take 1 byte each.
- [var AGL_ARGB8888_BIT: Int32](agl_argb8888_bit.md)
  Specifies a format that has 32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=31:24, R=23:16, G=15:8, B=7:0
- [var AGL_RGB888_A8_BIT: Int32](agl_rgb888_a8_bit.md)
  Specifies a format that has 8-32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0, R=23:16, G=15:8, B=7:0
- [var AGL_RGB101010_BIT: Int32](agl_rgb101010_bit.md)
  Specifies a format that has 32 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=29:20, G=19:10, B=9:0
- [var AGL_ARGB2101010_BIT: Int32](agl_argb2101010_bit.md)
  Specifies a format that has 32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=31:30 R=29:20, G=19:10, B=9:0
- [var AGL_RGB101010_A8_BIT: Int32](agl_rgb101010_a8_bit.md)
  Specifies a format that has 8-32 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=7:0 R=29:20, G=19:10, B=9:0
- [var AGL_RGB121212_BIT: Int32](agl_rgb121212_bit.md)
  Specifies a format that has 48 bits per pixel with an RGB channel layout, and the channels located in the following bits: R=35:24, G=23:12, B=11:0
- [var AGL_ARGB12121212_BIT: Int32](agl_argb12121212_bit.md)
  Specifies a format that has 48 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=47:36, R=35:24, G=23:12, B=11:0
- [var AGL_RGB161616_BIT: Int32](agl_rgb161616_bit.md)
  Specifies a format that has 64 bits per pixel with an RGB channel layout, and the channels located in the following bits:  R=47:32, G=31:16, B=15:0
- [var AGL_ARGB16161616_BIT: Int32](agl_argb16161616_bit.md)
  Specifies a format that has 64 bits per pixel with an ARGB channel layout, and the channels located in the following bits: A=63:48, R=47:32, G=31:16, B=15:0
- [var AGL_INDEX8_BIT: Int32](agl_index8_bit.md)
  Specifies an 8-bit color look up table. (Deprecated)
- [var AGL_INDEX16_BIT: Int32](agl_index16_bit.md)
  Specifies an 16-bit color look up table. (Deprecated)
- [var AGL_RGBFLOAT64_BIT: Int32](agl_rgbfloat64_bit.md)
  Specifies a format that has 64 bits per pixel with an RGB channel layout, half-floating point values. (A half-float is a 16-bit floating-point value.)
- [var AGL_RGBAFLOAT64_BIT: Int32](agl_rgbafloat64_bit.md)
  Specifies a format that has 64 bits per pixel with an ARGB channel layout, half-floating point values. (A half-float is a 16-bit floating-point value.)
- [var AGL_RGBFLOAT128_BIT: Int32](agl_rgbfloat128_bit.md)
  Specifies a format that has 128 bits per pixel with an RGB channel layout, IEEE floating point values.
- [var AGL_RGBAFLOAT128_BIT: Int32](agl_rgbafloat128_bit.md)
  Specifies a format that has 128 bits per pixel with an ARGB channel layout, IEEE floating point values.
- [var AGL_RGBFLOAT256_BIT: Int32](agl_rgbfloat256_bit.md)
  Specifies a format that has 256 bits per pixel with an RGB channel layout, IEEE double values.
- [var AGL_RGBAFLOAT256_BIT: Int32](agl_rgbafloat256_bit.md)
  Specifies a format that has 256 bits per pixel with an ARGB channel layout, IEEE double values.

## See Also

- [Bit Depths](bit-depths.md)
  Define resolutions for the depth and stencil buffers.
- [Buffer and Renderer Attributes](buffer-and-renderer-attributes.md)
  Specify attributes used to create a pixel format object.
- [Buffer Mode Flags](buffer-mode-flags.md)
  Define constants used to set buffer modes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/agl/color-modes)*