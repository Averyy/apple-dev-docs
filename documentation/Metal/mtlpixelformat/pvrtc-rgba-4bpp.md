# MTLPixelFormat.pvrtc_rgba_4bpp

**Framework**: Metal  
**Kind**: case

A compressed format that uses PVRTC compression and 4bpp for RGBA components.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case pvrtc_rgba_4bpp
```

#### Discussion

The only texture types that support this format include:

- [`MTLTextureType.type2D`](mtltexturetype/type2d.md)
- [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md)
- [`MTLTextureType.typeCube`](mtltexturetype/typecube.md)

> **Note**: The format doesn’t support subimages.

## See Also

- [MTLPixelFormat.pvrtc_rgb_2bpp](mtlpixelformat/pvrtc_rgb_2bpp.md)
  A compressed format that uses PVRTC compression and 2bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_2bpp_srgb](mtlpixelformat/pvrtc_rgb_2bpp_srgb.md)
  A compressed format that uses PVRTC compression and 2bpp for RGB components with a conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgb_4bpp](mtlpixelformat/pvrtc_rgb_4bpp.md)
  A compressed format that uses PVRTC compression and 4bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_4bpp_srgb](mtlpixelformat/pvrtc_rgb_4bpp_srgb.md)
  A compressed format that uses PVRTC compression and 4bpp for RGB components with a conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_2bpp](mtlpixelformat/pvrtc_rgba_2bpp.md)
  A compressed format that uses PVRTC compression and 2bpp for RGBA components.
- [MTLPixelFormat.pvrtc_rgba_2bpp_srgb](mtlpixelformat/pvrtc_rgba_2bpp_srgb.md)
  A compressed format that uses PVRTC compression and 2bpp for RGBA components with a conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_4bpp_srgb](mtlpixelformat/pvrtc_rgba_4bpp_srgb.md)
  A compressed format that uses PVRTC compression and 4bpp for RGBA components with a conversion between sRGB and linear space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgba_4bpp)*