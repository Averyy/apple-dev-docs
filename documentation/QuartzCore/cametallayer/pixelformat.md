# pixelFormat

**Framework**: Core Animation  
**Kind**: property

The pixel format of the layer’s textures.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var pixelFormat: MTLPixelFormat { get set }
```

#### Discussion

The default value is [`MTLPixelFormat.bgra8Unorm`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra8unorm).

You must use one of the following formats:

- [`MTLPixelFormat.bgra8Unorm`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra8unorm)
- [`MTLPixelFormat.bgra8Unorm_srgb`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra8unorm_srgb)
- [`MTLPixelFormat.rgba16Float`](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba16float)
- [`MTLPixelFormat.rgb10a2Unorm`](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb10a2unorm)
- [`MTLPixelFormat.bgr10a2Unorm`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10a2unorm)
- [`MTLPixelFormat.bgra10_xr`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr)
- [`MTLPixelFormat.bgra10_xr_srgb`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr_srgb)
- [`MTLPixelFormat.bgr10_xr`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr)
- [`MTLPixelFormat.bgr10_xr_srgb`](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr_srgb)

## See Also

- [var colorspace: CGColorSpace?](cametallayer/colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](cametallayer/framebufferonly.md)
  A Boolean value that determines whether the layer’s textures are used only for rendering.
- [var drawableSize: CGSize](cametallayer/drawablesize.md)
  The size, in pixels, of textures for rendering layer content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/pixelformat)*