# autoResizeDrawable

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether to resize the drawable as the view changes size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var autoResizeDrawable: Bool { get set }
```

```objc
@property (nonatomic) BOOL autoResizeDrawable;
```

## Discussion

If the value is [`true`](../../Swift/true.md), the view automatically resizes its underlying color, depth, stencil, and multisample textures when the view is resized. If the value is [`false`](../../Swift/false.md), you must explicitly set [`drawableSize`](./drawablesize.md) to change the size of these objects.

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring the Color Render Target
- [var colorPixelFormat: MTLPixelFormat](./colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
- [var colorspace: CGColorSpace?](./colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](./framebufferonly.md)
  A Boolean value that determines whether the drawable’s textures are used only for rendering.
- [var drawableSize: CGSize](./drawablesize.md)
  The current size of drawable textures.
- [var preferredDrawableSize: CGSize](./preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var clearColor: MTLClearColor](./clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/autoresizedrawable)*