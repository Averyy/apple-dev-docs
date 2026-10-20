# clearColor

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The color to use to clear the color target when creating a render pass descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var clearColor: MTLClearColor { get set }
```

```objc
@property (nonatomic) MTLClearColor clearColor;
```

#### Discussion

When the view creates a render pass, it sets the load action for the color render target to [`MTLLoadAction.clear`](../../Metal/mtlloadaction/clear.md) and uses this color as the clear color. The default value is `(0.0, 0.0, 0.0, 1.0)`.

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
- [var autoResizeDrawable: Bool](./autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/clearcolor)*