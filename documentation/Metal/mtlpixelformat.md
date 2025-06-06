# MTLPixelFormat

**Framework**: Metal  
**Kind**: enum

The data formats that describe the organization and characteristics of individual pixels in a texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLPixelFormat
```

#### Overview

There are three varieties of pixel formats: ordinary, packed, and compressed. For ordinary and packed formats, the name of the pixel format specifies the order of components (such as `R`, `RG`, `RGB`, `RGBA`, `BGRA`), bits per component (such as `8`, `16`, `32`), and data type for the component (such as `Float`, `Sint`, `Snorm`, `Uint`, `Unorm`). If the pixel format name has the `_sRGB` suffix, then reading and writing pixel data applies sRGB gamma compression and decompression. The alpha component of sRGB pixel formats is always treated as a linear value. For compressed formats, the name of the pixel format specifies a compression family (such as `ASTC`, `BC`, `EAC`, `ETC2`, `PVRTC`).

> **Note**:  Pixel format availability and capabilities vary by feature set. See [`Pixel Format Capabilities`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for more information.

##### Storage Characteristics

The number and size of each pixel component determines the storage size of each pixel format. For example, the storage size of [`MTLPixelFormat.bgra8Unorm`](mtlpixelformat/bgra8unorm.md) is 32 bits (four 8-bit components) and the storage size of [`MTLPixelFormat.bgr5A1Unorm`](mtlpixelformat/bgr5a1unorm.md) is 16 bits (three 5-bit components and one 1-bit component).

For normalized signed integer formats (`Snorm`), values in the range `[-1.0, 1.0]` map to `[MIN_INT, MAX_INT]`, where `MIN_INT` is the greatest negative integer and `MAX_INT` is the greatest positive integer for the number of bits in the storage size. Positive values and zero distribute uniformly in the range `[0.0, 1.0]`, and negative integer values greater than `(MIN_INT + 1)` distribute uniformly in the range `(-1.0, 0.0)`.

> ❗ **Important**:  For `Snorm` formats, the values `MIN_INT` and `(MIN_INT + 1)` both map to `-1.0`.

For normalized unsigned integer formats (`Unorm`), values in the range `[0.0, 1.0]` are uniformly mapped to `[0, MAX_UINT]`, where `MAX_UINT` is the greatest unsigned integer for the number of bits in the storage size.

Format data is little-endian (the least-significant byte in the least-significant address). For formats with components that are themselves byte-aligned and more than one byte, the components are also little-endian.

See Table 7.7 in the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) (PDF) for details on pixel format normalization.

## Topics

### Ordinary 8-Bit Pixel Formats
- [MTLPixelFormat.a8Unorm](mtlpixelformat/a8unorm.md)
  Ordinary format with one 8-bit normalized unsigned integer component.
- [MTLPixelFormat.r8Unorm](mtlpixelformat/r8unorm.md)
  Ordinary format with one 8-bit normalized unsigned integer component.
- [MTLPixelFormat.r8Unorm_srgb](mtlpixelformat/r8unorm_srgb.md)
  Ordinary format with one 8-bit normalized unsigned integer component with conversion between sRGB and linear space.
- [MTLPixelFormat.r8Snorm](mtlpixelformat/r8snorm.md)
  Ordinary format with one 8-bit normalized signed integer component.
- [MTLPixelFormat.r8Uint](mtlpixelformat/r8uint.md)
  Ordinary format with one 8-bit unsigned integer component.
- [MTLPixelFormat.r8Sint](mtlpixelformat/r8sint.md)
  Ordinary format with one 8-bit signed integer component.
### Ordinary 16-Bit Pixel Formats
- [MTLPixelFormat.r16Unorm](mtlpixelformat/r16unorm.md)
  Ordinary format with one 16-bit normalized unsigned integer component.
- [MTLPixelFormat.r16Snorm](mtlpixelformat/r16snorm.md)
  Ordinary format with one 16-bit normalized signed integer component.
- [MTLPixelFormat.r16Uint](mtlpixelformat/r16uint.md)
  Ordinary format with one 16-bit unsigned integer component.
- [MTLPixelFormat.r16Sint](mtlpixelformat/r16sint.md)
  Ordinary format with one 16-bit signed integer component.
- [MTLPixelFormat.r16Float](mtlpixelformat/r16float.md)
  Ordinary format with one 16-bit floating-point component.
- [MTLPixelFormat.rg8Unorm](mtlpixelformat/rg8unorm.md)
  Ordinary format with two 8-bit normalized unsigned integer components.
- [MTLPixelFormat.rg8Unorm_srgb](mtlpixelformat/rg8unorm_srgb.md)
  Ordinary format with two 8-bit normalized unsigned integer components with conversion between sRGB and linear space.
- [MTLPixelFormat.rg8Snorm](mtlpixelformat/rg8snorm.md)
  Ordinary format with two 8-bit normalized signed integer components.
- [MTLPixelFormat.rg8Uint](mtlpixelformat/rg8uint.md)
  Ordinary format with two 8-bit unsigned integer components.
- [MTLPixelFormat.rg8Sint](mtlpixelformat/rg8sint.md)
  Ordinary format with two 8-bit signed integer components.
### Packed 16-Bit Pixel Formats
- [MTLPixelFormat.b5g6r5Unorm](mtlpixelformat/b5g6r5unorm.md)
  Packed 16-bit format with normalized unsigned integer color components: 5 bits for blue, 6 bits for green, 5 bits for red, packed into 16 bits.
- [MTLPixelFormat.a1bgr5Unorm](mtlpixelformat/a1bgr5unorm.md)
  Packed 16-bit format with normalized unsigned integer color components: 5 bits each for BGR and 1 for alpha, packed into 16 bits.
- [MTLPixelFormat.abgr4Unorm](mtlpixelformat/abgr4unorm.md)
  Packed 16-bit format with normalized unsigned integer color components: 4 bits each for ABGR, packed into 16 bits.
- [MTLPixelFormat.bgr5A1Unorm](mtlpixelformat/bgr5a1unorm.md)
  Packed 16-bit format with normalized unsigned integer color components: 5 bits each for BGR and 1 for alpha, packed into 16 bits.
### Ordinary 32-Bit Pixel Formats
- [MTLPixelFormat.r32Uint](mtlpixelformat/r32uint.md)
  Ordinary format with one 32-bit unsigned integer component.
- [MTLPixelFormat.r32Sint](mtlpixelformat/r32sint.md)
  Ordinary format with one 32-bit signed integer component.
- [MTLPixelFormat.r32Float](mtlpixelformat/r32float.md)
  Ordinary format with one 32-bit floating-point component.
- [MTLPixelFormat.rg16Unorm](mtlpixelformat/rg16unorm.md)
  Ordinary format with two 16-bit normalized unsigned integer components.
- [MTLPixelFormat.rg16Snorm](mtlpixelformat/rg16snorm.md)
  Ordinary format with two 16-bit normalized signed integer components.
- [MTLPixelFormat.rg16Uint](mtlpixelformat/rg16uint.md)
  Ordinary format with two 16-bit unsigned integer components.
- [MTLPixelFormat.rg16Sint](mtlpixelformat/rg16sint.md)
  Ordinary format with two 16-bit signed integer components.
- [MTLPixelFormat.rg16Float](mtlpixelformat/rg16float.md)
  Ordinary format with two 16-bit floating-point components.
- [MTLPixelFormat.rgba8Unorm](mtlpixelformat/rgba8unorm.md)
  Ordinary format with four 8-bit normalized unsigned integer components in RGBA order.
- [MTLPixelFormat.rgba8Unorm_srgb](mtlpixelformat/rgba8unorm_srgb.md)
  Ordinary format with four 8-bit normalized unsigned integer components in RGBA order with conversion between sRGB and linear space.
- [MTLPixelFormat.rgba8Snorm](mtlpixelformat/rgba8snorm.md)
  Ordinary format with four 8-bit normalized signed integer components in RGBA order.
- [MTLPixelFormat.rgba8Uint](mtlpixelformat/rgba8uint.md)
  Ordinary format with four 8-bit unsigned integer components in RGBA order.
- [MTLPixelFormat.rgba8Sint](mtlpixelformat/rgba8sint.md)
  Ordinary format with four 8-bit signed integer components in RGBA order.
- [MTLPixelFormat.bgra8Unorm](mtlpixelformat/bgra8unorm.md)
  Ordinary format with four 8-bit normalized unsigned integer components in BGRA order.
- [MTLPixelFormat.bgra8Unorm_srgb](mtlpixelformat/bgra8unorm_srgb.md)
  Ordinary format with four 8-bit normalized unsigned integer components in BGRA order with conversion between sRGB and linear space.
### Packed 32-Bit Pixel Formats
- [MTLPixelFormat.bgr10a2Unorm](mtlpixelformat/bgr10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.
- [MTLPixelFormat.rgb10a2Unorm](mtlpixelformat/rgb10a2unorm.md)
  A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rgb10a2Uint](mtlpixelformat/rgb10a2uint.md)
  A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormat.rg11b10Float](mtlpixelformat/rg11b10float.md)
  32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.
- [MTLPixelFormat.rgb9e5Float](mtlpixelformat/rgb9e5float.md)
  Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.
### Ordinary 64-Bit Pixel Formats
- [MTLPixelFormat.rg32Uint](mtlpixelformat/rg32uint.md)
  Ordinary format with two 32-bit unsigned integer components.
- [MTLPixelFormat.rg32Sint](mtlpixelformat/rg32sint.md)
  Ordinary format with two 32-bit signed integer components.
- [MTLPixelFormat.rg32Float](mtlpixelformat/rg32float.md)
  Ordinary format with two 32-bit floating-point components.
- [MTLPixelFormat.rgba16Unorm](mtlpixelformat/rgba16unorm.md)
  Ordinary format with four 16-bit normalized unsigned integer components in RGBA order.
- [MTLPixelFormat.rgba16Snorm](mtlpixelformat/rgba16snorm.md)
  Ordinary format with four 16-bit normalized signed integer components in RGBA order.
- [MTLPixelFormat.rgba16Uint](mtlpixelformat/rgba16uint.md)
  Ordinary format with four 16-bit unsigned integer components in RGBA order.
- [MTLPixelFormat.rgba16Sint](mtlpixelformat/rgba16sint.md)
  Ordinary format with four 16-bit signed integer components in RGBA order.
- [MTLPixelFormat.rgba16Float](mtlpixelformat/rgba16float.md)
  Ordinary format with four 16-bit floating-point components in RGBA order.
### Ordinary 128-Bit Pixel Formats
- [MTLPixelFormat.rgba32Uint](mtlpixelformat/rgba32uint.md)
  Ordinary format with four 32-bit unsigned integer components in RGBA order.
- [MTLPixelFormat.rgba32Sint](mtlpixelformat/rgba32sint.md)
  Ordinary format with four 32-bit signed integer components in RGBA order.
- [MTLPixelFormat.rgba32Float](mtlpixelformat/rgba32float.md)
  Ordinary format with four 32-bit floating-point components in RGBA order.
### Compressed PVRTC Pixel Formats
- [MTLPixelFormat.pvrtc_rgb_2bpp](mtlpixelformat/pvrtc_rgb_2bpp.md)
  Compressed format using PVRTC compression and 2bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_2bpp_srgb](mtlpixelformat/pvrtc_rgb_2bpp_srgb.md)
  Compressed format using PVRTC compression and 2bpp for RGB components with conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgb_4bpp](mtlpixelformat/pvrtc_rgb_4bpp.md)
  Compressed format using PVRTC compression and 4bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_4bpp_srgb](mtlpixelformat/pvrtc_rgb_4bpp_srgb.md)
  Compressed format using PVRTC compression and 4bpp for RGB components with conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_2bpp](mtlpixelformat/pvrtc_rgba_2bpp.md)
  Compressed format using PVRTC compression and 2bpp for RGBA components.
- [MTLPixelFormat.pvrtc_rgba_2bpp_srgb](mtlpixelformat/pvrtc_rgba_2bpp_srgb.md)
  Compressed format using PVRTC compression and 2bpp for RGBA components with conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_4bpp](mtlpixelformat/pvrtc_rgba_4bpp.md)
  Compressed format using PVRTC compression and 4bpp for RGBA components.
- [MTLPixelFormat.pvrtc_rgba_4bpp_srgb](mtlpixelformat/pvrtc_rgba_4bpp_srgb.md)
  Compressed format using PVRTC compression and 4bpp for RGBA components with conversion between sRGB and linear space.
### Compressed EAC/ETC Pixel Formats
- [MTLPixelFormat.eac_r11Unorm](mtlpixelformat/eac_r11unorm.md)
  Compressed format using EAC compression with one normalized unsigned integer component.
- [MTLPixelFormat.eac_r11Snorm](mtlpixelformat/eac_r11snorm.md)
  Compressed format using EAC compression with one normalized signed integer component.
- [MTLPixelFormat.eac_rg11Unorm](mtlpixelformat/eac_rg11unorm.md)
  Compressed format using EAC compression with two normalized unsigned integer components.
- [MTLPixelFormat.eac_rg11Snorm](mtlpixelformat/eac_rg11snorm.md)
  Compressed format using EAC compression with two normalized signed integer components.
- [MTLPixelFormat.eac_rgba8](mtlpixelformat/eac_rgba8.md)
  Compressed format using EAC compression with four 8-bit components.
- [MTLPixelFormat.eac_rgba8_srgb](mtlpixelformat/eac_rgba8_srgb.md)
  Compressed format using EAC compression with four 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormat.etc2_rgb8](mtlpixelformat/etc2_rgb8.md)
  Compressed format using ETC2 compression with three 8-bit components.
- [MTLPixelFormat.etc2_rgb8_srgb](mtlpixelformat/etc2_rgb8_srgb.md)
  Compressed format using ETC2 compression with three 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormat.etc2_rgb8a1](mtlpixelformat/etc2_rgb8a1.md)
  Compressed format using ETC2 compression with four 8-bit components.
- [MTLPixelFormat.etc2_rgb8a1_srgb](mtlpixelformat/etc2_rgb8a1_srgb.md)
  Compressed format using ETC2 compression with four 8-bit components with conversion between sRGB and linear space.
### Compressed ASTC Pixel Formats
- [MTLPixelFormat.astc_4x4_srgb](mtlpixelformat/astc_4x4_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 4, and a block height of 4.
- [MTLPixelFormat.astc_5x4_srgb](mtlpixelformat/astc_5x4_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 5, and a block height of 4.
- [MTLPixelFormat.astc_5x5_srgb](mtlpixelformat/astc_5x5_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 5, and a block height of 5.
- [MTLPixelFormat.astc_6x5_srgb](mtlpixelformat/astc_6x5_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 6, and a block height of 5.
- [MTLPixelFormat.astc_6x6_srgb](mtlpixelformat/astc_6x6_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 6, and a block height of 6.
- [MTLPixelFormat.astc_8x5_srgb](mtlpixelformat/astc_8x5_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 8, and a block height of 5.
- [MTLPixelFormat.astc_8x6_srgb](mtlpixelformat/astc_8x6_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 8, and a block height of 6.
- [MTLPixelFormat.astc_8x8_srgb](mtlpixelformat/astc_8x8_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 8, and a block height of 8.
- [MTLPixelFormat.astc_10x5_srgb](mtlpixelformat/astc_10x5_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 5.
- [MTLPixelFormat.astc_10x6_srgb](mtlpixelformat/astc_10x6_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 6.
- [MTLPixelFormat.astc_10x8_srgb](mtlpixelformat/astc_10x8_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 8.
- [MTLPixelFormat.astc_10x10_srgb](mtlpixelformat/astc_10x10_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 10.
- [MTLPixelFormat.astc_12x10_srgb](mtlpixelformat/astc_12x10_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 12, and a block height of 10.
- [MTLPixelFormat.astc_12x12_srgb](mtlpixelformat/astc_12x12_srgb.md)
  ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 12, and a block height of 12.
- [MTLPixelFormat.astc_4x4_ldr](mtlpixelformat/astc_4x4_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 4, and a block height of 4.
- [MTLPixelFormat.astc_5x4_ldr](mtlpixelformat/astc_5x4_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 5, and a block height of 4.
- [MTLPixelFormat.astc_5x5_ldr](mtlpixelformat/astc_5x5_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 5, and a block height of 5.
- [MTLPixelFormat.astc_6x5_ldr](mtlpixelformat/astc_6x5_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 6, and a block height of 5.
- [MTLPixelFormat.astc_6x6_ldr](mtlpixelformat/astc_6x6_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 6, and a block height of 6.
- [MTLPixelFormat.astc_8x5_ldr](mtlpixelformat/astc_8x5_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 8, and a block height of 5.
- [MTLPixelFormat.astc_8x6_ldr](mtlpixelformat/astc_8x6_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 8, and a block height of 6.
- [MTLPixelFormat.astc_8x8_ldr](mtlpixelformat/astc_8x8_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 8, and a block height of 8.
- [MTLPixelFormat.astc_10x5_ldr](mtlpixelformat/astc_10x5_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 5.
- [MTLPixelFormat.astc_10x6_ldr](mtlpixelformat/astc_10x6_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 6.
- [MTLPixelFormat.astc_10x8_ldr](mtlpixelformat/astc_10x8_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 8.
- [MTLPixelFormat.astc_10x10_ldr](mtlpixelformat/astc_10x10_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 10.
- [MTLPixelFormat.astc_12x10_ldr](mtlpixelformat/astc_12x10_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 12, and a block height of 10.
- [MTLPixelFormat.astc_12x12_ldr](mtlpixelformat/astc_12x12_ldr.md)
  ASTC-compressed format with low-dynamic-range content, a block width of 12, and a block height of 12.
- [MTLPixelFormat.astc_4x4_hdr](mtlpixelformat/astc_4x4_hdr.md)
  ASTC-compressed format with high-dynamic-range content, a block width of 4, and a block height of 4.
- [MTLPixelFormat.astc_5x4_hdr](mtlpixelformat/astc_5x4_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 5, and a block height of 4.
- [MTLPixelFormat.astc_5x5_hdr](mtlpixelformat/astc_5x5_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 5, and a block height of 6.
- [MTLPixelFormat.astc_6x5_hdr](mtlpixelformat/astc_6x5_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 6, and a block height of 5.
- [MTLPixelFormat.astc_6x6_hdr](mtlpixelformat/astc_6x6_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 6, and a block height of 6.
- [MTLPixelFormat.astc_8x5_hdr](mtlpixelformat/astc_8x5_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 8, and a block height of 5.
- [MTLPixelFormat.astc_8x6_hdr](mtlpixelformat/astc_8x6_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 8, and a block height of 6.
- [MTLPixelFormat.astc_8x8_hdr](mtlpixelformat/astc_8x8_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 8, and a block height of 8.
- [MTLPixelFormat.astc_10x5_hdr](mtlpixelformat/astc_10x5_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 5.
- [MTLPixelFormat.astc_10x6_hdr](mtlpixelformat/astc_10x6_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 6.
- [MTLPixelFormat.astc_10x8_hdr](mtlpixelformat/astc_10x8_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 8.
- [MTLPixelFormat.astc_10x10_hdr](mtlpixelformat/astc_10x10_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 10.
- [MTLPixelFormat.astc_12x10_hdr](mtlpixelformat/astc_12x10_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 12, and a block height of 10.
- [MTLPixelFormat.astc_12x12_hdr](mtlpixelformat/astc_12x12_hdr.md)
  ASTC-compressed format with high-dynamic range content, a block width of 12, and a block height of 12.
### Compressed BC Pixel Formats
- [MTLPixelFormat.bc1_rgba](mtlpixelformat/bc1_rgba.md)
  Compressed format with two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc1_rgba_srgb](mtlpixelformat/bc1_rgba_srgb.md)
  Compressed format with two 16-bit color components and one 32-bit descriptor component, with conversion between sRGB and linear space.
- [MTLPixelFormat.bc2_rgba](mtlpixelformat/bc2_rgba.md)
  Compressed format with two 64-bit chunks. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc2_rgba_srgb](mtlpixelformat/bc2_rgba_srgb.md)
  Compressed format with two 64-bit chunks, with conversion between sRGB and linear space. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc3_rgba](mtlpixelformat/bc3_rgba.md)
  Compressed format with two 64-bit chunks. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc3_rgba_srgb](mtlpixelformat/bc3_rgba_srgb.md)
  Compressed format with two 64-bit chunks, with conversion between sRGB and linear space. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormat.bc4_rUnorm](mtlpixelformat/bc4_runorm.md)
  Compressed format with one normalized unsigned integer component.
- [MTLPixelFormat.bc4_rSnorm](mtlpixelformat/bc4_rsnorm.md)
  Compressed format with one normalized signed integer component.
- [MTLPixelFormat.bc5_rgUnorm](mtlpixelformat/bc5_rgunorm.md)
  Compressed format with two normalized unsigned integer components.
- [MTLPixelFormat.bc5_rgSnorm](mtlpixelformat/bc5_rgsnorm.md)
  Compressed format with two normalized signed integer components.
- [MTLPixelFormat.bc6H_rgbFloat](mtlpixelformat/bc6h_rgbfloat.md)
  Compressed format with four floating-point components.
- [MTLPixelFormat.bc6H_rgbuFloat](mtlpixelformat/bc6h_rgbufloat.md)
  Compressed format with four unsigned floating-point components.
- [MTLPixelFormat.bc7_rgbaUnorm](mtlpixelformat/bc7_rgbaunorm.md)
  Compressed format with four normalized unsigned integer components.
- [MTLPixelFormat.bc7_rgbaUnorm_srgb](mtlpixelformat/bc7_rgbaunorm_srgb.md)
  Compressed format with four normalized unsigned integer components, with conversion between sRGB and linear space.
### YUV Pixel Formats
- [MTLPixelFormat.gbgr422](mtlpixelformat/gbgr422.md)
  A pixel format where the red and green components are subsampled horizontally.
- [MTLPixelFormat.bgrg422](mtlpixelformat/bgrg422.md)
  A pixel format where the red and green components are subsampled horizontally.
### Depth and Stencil Pixel Formats
- [MTLPixelFormat.depth16Unorm](mtlpixelformat/depth16unorm.md)
  A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormat.depth32Float](mtlpixelformat/depth32float.md)
  A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormat.stencil8](mtlpixelformat/stencil8.md)
  A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormat.depth24Unorm_stencil8](mtlpixelformat/depth24unorm_stencil8.md)
  A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormat.depth32Float_stencil8](mtlpixelformat/depth32float_stencil8.md)
  A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormat.x32_stencil8](mtlpixelformat/x32_stencil8.md)
  A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.
- [MTLPixelFormat.x24_stencil8](mtlpixelformat/x24_stencil8.md)
  A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value.
### Extended Range and Wide Color Pixel Formats
- [MTLPixelFormat.bgra10_xr](mtlpixelformat/bgra10_xr.md)
  A 64-bit extended-range pixel format with four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgra10_xr_srgb](mtlpixelformat/bgra10_xr_srgb.md)
  A 64-bit extended-range pixel format with sRGB conversion and four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormat.bgr10_xr](mtlpixelformat/bgr10_xr.md)
  A 32-bit extended-range pixel format with three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.
- [MTLPixelFormat.bgr10_xr_srgb](mtlpixelformat/bgr10_xr_srgb.md)
  A 32-bit extended-range pixel format with sRGB conversion and three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.
### Invalid Pixel Format
- [MTLPixelFormat.invalid](mtlpixelformat/invalid.md)
  The default value of the pixel format for the `MTLRenderPipelineState`. You cannot create a texture with this value.
### Initializers
- [init?(rawValue: UInt)](mtlpixelformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing Texture Data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [enum MTLTextureCompressionType](mtltexturecompressiontype.md)
- [class MTLTextureDescriptor](mtltexturedescriptor.md)
  An object that you use to configure new Metal texture objects.
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [class MTLSharedTextureHandle](mtlsharedtexturehandle.md)
  A texture handle that can be shared across process address space boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Metal/mtlpixelformat)*