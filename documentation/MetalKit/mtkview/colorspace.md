# colorspace

**Framework**: MetalKit  
**Kind**: property

The color space of the rendered content.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
var colorspace: CGColorSpace? { get set }
```

#### Discussion

The default value is `nil`, indicating that the rendered content isn’t color-matched. If you set this to a different color space, Core Animation performs any necessary color transformations when compositing the view’s contents.

## See Also

- [var colorPixelFormat: MTLPixelFormat](mtkview/colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/colorspace)*