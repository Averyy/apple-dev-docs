# framebufferOnly

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the drawable’s textures are used only for rendering.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var framebufferOnly: Bool { get set }
```

```objc
@property (nonatomic) BOOL framebufferOnly;
```

## Discussion

If the value is [`true`](../../Swift/true.md) (the default), the underlying [`CAMetalLayer`](../../QuartzCore/cametallayer.md) object allocates its textures with only the [`renderTarget`](../../Metal/mtltextureusage/rendertarget.md) usage flag. Core Animation can then optimize the textures for display purposes. However, you may not sample, read from, or write to those textures. If the value is [`false`](../../Swift/false.md), you can sample or perform read/write operations on the textures, but at a cost to performance.

## See Also

### Configuring the Color Render Target
- [var colorPixelFormat: MTLPixelFormat](./colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
- [var colorspace: CGColorSpace?](./colorspace.md)
  The color space of the rendered content.
- [var drawableSize: CGSize](./drawablesize.md)
  The current size of drawable textures.
- [var preferredDrawableSize: CGSize](./preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var autoResizeDrawable: Bool](./autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](./clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/framebufferonly)*