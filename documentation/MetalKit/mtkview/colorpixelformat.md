# colorPixelFormat

**Framework**: MetalKit  
**Kind**: property

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
@MainActor
var colorPixelFormat: MTLPixelFormat { get set }
```

#### Discussion

The pixel format must be one that the underlying [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) can use. See [`pixelFormat`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/pixelFormat).

The default value is [`MTLPixelFormat.bgra8Unorm`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/bgra8Unorm).

## See Also

- [var colorspace: CGColorSpace?](mtkview/colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](mtkview/framebufferonly.md)
  A Boolean value that determines whether the drawable’s textures are used only for rendering.
- [var drawableSize: CGSize](mtkview/drawablesize.md)
  The current size of drawable textures.
- [var preferredDrawableSize: CGSize](mtkview/preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var autoResizeDrawable: Bool](mtkview/autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](mtkview/clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/colorpixelformat)*