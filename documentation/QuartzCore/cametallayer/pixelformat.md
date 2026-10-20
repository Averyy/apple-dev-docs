# pixelFormat

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property MTLPixelFormat pixelFormat;
```

#### Discussion

The default value is [`MTLPixelFormat.bgra8Unorm`](../../Metal/mtlpixelformat/bgra8unorm.md).

You must use one of the following formats:

- [`MTLPixelFormat.bgra8Unorm`](../../Metal/mtlpixelformat/bgra8unorm.md)
- [`MTLPixelFormat.bgra8Unorm_srgb`](../../Metal/mtlpixelformat/bgra8unorm_srgb.md)
- [`MTLPixelFormat.rgba16Float`](../../Metal/mtlpixelformat/rgba16float.md)
- [`MTLPixelFormat.rgb10a2Unorm`](../../Metal/mtlpixelformat/rgb10a2unorm.md)
- [`MTLPixelFormat.bgr10a2Unorm`](../../Metal/mtlpixelformat/bgr10a2unorm.md)
- [`MTLPixelFormat.bgra10_xr`](../../Metal/mtlpixelformat/bgra10_xr.md)
- [`MTLPixelFormat.bgra10_xr_srgb`](../../Metal/mtlpixelformat/bgra10_xr_srgb.md)
- [`MTLPixelFormat.bgr10_xr`](../../Metal/mtlpixelformat/bgr10_xr.md)
- [`MTLPixelFormat.bgr10_xr_srgb`](../../Metal/mtlpixelformat/bgr10_xr_srgb.md)

## See Also

### Configuring the Layer’s Drawable Objects
- [var colorspace: CGColorSpace?](./colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](./framebufferonly.md)
  A Boolean value that determines whether the layer’s textures are used only for rendering.
- [var drawableSize: CGSize](./drawablesize.md)
  The size, in pixels, of textures for rendering layer content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/pixelformat)*