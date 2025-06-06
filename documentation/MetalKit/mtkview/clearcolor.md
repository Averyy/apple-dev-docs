# clearColor

**Framework**: MetalKit  
**Kind**: property

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
@MainActor
var clearColor: MTLClearColor { get set }
```

#### Discussion

When the view creates a render pass, it sets the load action for the color render target to [`MTLLoadAction.clear`](https://developer.apple.com/documentation/Metal/MTLLoadAction/clear) and uses this color as the clear color. The default value is `(0.0, 0.0, 0.0, 1.0)`.

## See Also

- [var colorPixelFormat: MTLPixelFormat](mtkview/colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/clearcolor)*