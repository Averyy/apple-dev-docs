# colorPixelFormat

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The color pixel format for the current drawable’s texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var colorPixelFormat: MTLPixelFormat { get set }
```

```objc
@property (nonatomic) MTLPixelFormat colorPixelFormat;
```

#### Discussion

The pixel format must be one that the underlying [`CAMetalLayer`](../../QuartzCore/cametallayer.md) can use. See [`pixelFormat`](../../QuartzCore/cametallayer/pixelformat.md).

The default value is [`MTLPixelFormat.bgra8Unorm`](../../Metal/mtlpixelformat/bgra8unorm.md).

## See Also

### Configuring the Color Render Target
- [var colorspace: CGColorSpace?](./colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](./framebufferonly.md)
  A Boolean value that determines whether the drawable’s textures are used only for rendering.
- [var drawableSize: CGSize](./drawablesize.md)
  The current size of drawable textures.
- [var preferredDrawableSize: CGSize](./preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var autoResizeDrawable: Bool](./autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](./clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/colorpixelformat)*