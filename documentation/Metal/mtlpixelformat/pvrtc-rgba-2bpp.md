# MTLPixelFormat.pvrtc_rgba_2bpp

**Framework**: Metal  
**Kind**: case

Compressed format using PVRTC compression and 2bpp for RGBA components.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case pvrtc_rgba_2bpp
```

#### Discussion

Only [`MTLTextureType.type2D`](mtltexturetype/type2d.md), [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md), and [`MTLTextureType.typeCube`](mtltexturetype/typecube.md) textures are supported. Subimages are not supported.

## See Also

- [MTLPixelFormat.pvrtc_rgb_2bpp](mtlpixelformat/pvrtc_rgb_2bpp.md)
  Compressed format using PVRTC compression and 2bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_2bpp_srgb](mtlpixelformat/pvrtc_rgb_2bpp_srgb.md)
  Compressed format using PVRTC compression and 2bpp for RGB components with conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgb_4bpp](mtlpixelformat/pvrtc_rgb_4bpp.md)
  Compressed format using PVRTC compression and 4bpp for RGB components.
- [MTLPixelFormat.pvrtc_rgb_4bpp_srgb](mtlpixelformat/pvrtc_rgb_4bpp_srgb.md)
  Compressed format using PVRTC compression and 4bpp for RGB components with conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_2bpp_srgb](mtlpixelformat/pvrtc_rgba_2bpp_srgb.md)
  Compressed format using PVRTC compression and 2bpp for RGBA components with conversion between sRGB and linear space.
- [MTLPixelFormat.pvrtc_rgba_4bpp](mtlpixelformat/pvrtc_rgba_4bpp.md)
  Compressed format using PVRTC compression and 4bpp for RGBA components.
- [MTLPixelFormat.pvrtc_rgba_4bpp_srgb](mtlpixelformat/pvrtc_rgba_4bpp_srgb.md)
  Compressed format using PVRTC compression and 4bpp for RGBA components with conversion between sRGB and linear space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgba_2bpp)*