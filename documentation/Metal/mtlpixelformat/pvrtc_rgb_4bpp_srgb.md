# MTLPixelFormat.pvrtc_rgb_4bpp_srgb

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A compressed format that uses PVRTC compression and 4bpp for RGB components with a conversion between sRGB and linear space.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use one of the other formats with `astc`/`ASTC`, `etc2`/`ETC2`, or `bc`/`BC` instead.

## Declaration

```swift
case pvrtc_rgb_4bpp_srgb
```

```c
MTLPixelFormatPVRTC_RGB_4BPP_sRGB
```

#### Discussion

The only texture types that support this format include:

- [`MTLTextureType.type2D`](../mtltexturetype/type2d.md)
- [`MTLTextureType.type2DArray`](../mtltexturetype/type2darray.md)
- [`MTLTextureType.typeCube`](../mtltexturetype/typecube.md)

> **Note**: The format doesn’t support subimages.

## See Also

### Compressed PVRTC pixel formats
- [MTLPixelFormat.pvrtc_rgb_2bpp](./pvrtc_rgb_2bpp.md)
  A compressed format that uses PVRTC compression and 2bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_2bpp_srgb](./pvrtc_rgb_2bpp_srgb.md)
  A compressed format that uses PVRTC compression and 2bpp for RGB components with a conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgb_4bpp](./pvrtc_rgb_4bpp.md)
  A compressed format that uses PVRTC compression and 4bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgba_2bpp](./pvrtc_rgba_2bpp.md)
  A compressed format that uses PVRTC compression and 2bpp for RGBA components.
- [MTLPixelFormat.pvrtc_rgba_2bpp_srgb](./pvrtc_rgba_2bpp_srgb.md)
  A compressed format that uses PVRTC compression and 2bpp for RGBA components with a conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_4bpp](./pvrtc_rgba_4bpp.md)
  A compressed format that uses PVRTC compression and 4bpp for RGBA components.
- [MTLPixelFormat.pvrtc_rgba_4bpp_srgb](./pvrtc_rgba_4bpp_srgb.md)
  A compressed format that uses PVRTC compression and 4bpp for RGBA components with a conversion between sRGB and linear space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgb_4bpp_srgb)*