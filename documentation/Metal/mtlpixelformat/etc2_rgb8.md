# MTLPixelFormat.etc2_rgb8

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Compressed format using ETC2 compression with three 8-bit components.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case etc2_rgb8
```

```c
MTLPixelFormatETC2_RGB8
```

#### Discussion

Only [`MTLTextureType.type2D`](../mtltexturetype/type2d.md), [`MTLTextureType.type2DArray`](../mtltexturetype/type2darray.md), and [`MTLTextureType.typeCube`](../mtltexturetype/typecube.md) textures are supported.

## See Also

### Compressed EAC/ETC pixel formats
- [MTLPixelFormat.eac_r11Unorm](./eac_r11unorm.md)
  Compressed format using EAC compression with one normalized unsigned integer component.
- [MTLPixelFormat.eac_r11Snorm](./eac_r11snorm.md)
  Compressed format using EAC compression with one normalized signed integer component.
- [MTLPixelFormat.eac_rg11Unorm](./eac_rg11unorm.md)
  Compressed format using EAC compression with two normalized unsigned integer components.
- [MTLPixelFormat.eac_rg11Snorm](./eac_rg11snorm.md)
  Compressed format using EAC compression with two normalized signed integer components.
- [MTLPixelFormat.eac_rgba8](./eac_rgba8.md)
  Compressed format using EAC compression with four 8-bit components.
- [MTLPixelFormat.eac_rgba8_srgb](./eac_rgba8_srgb.md)
  Compressed format using EAC compression with four 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormat.etc2_rgb8_srgb](./etc2_rgb8_srgb.md)
  Compressed format using ETC2 compression with three 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormat.etc2_rgb8a1](./etc2_rgb8a1.md)
  Compressed format using ETC2 compression with four 8-bit components.
- [MTLPixelFormat.etc2_rgb8a1_srgb](./etc2_rgb8a1_srgb.md)
  Compressed format using ETC2 compression with four 8-bit components with conversion between sRGB and linear space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/etc2_rgb8)*