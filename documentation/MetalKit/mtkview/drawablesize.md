# drawableSize

**Framework**: MetalKit  
**Kind**: property

The current size of drawable textures.

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
var drawableSize: CGSize { get set }
```

#### Discussion

Changing this value adjusts the size of any color, depth, stencil, and multisampling textures created by the view. If [`autoResizeDrawable`](mtkview/autoresizedrawable.md) is [`true`](https://developer.apple.com/documentation/swift/true), this property is updated automatically whenever the view’s size changes. If [`autoResizeDrawable`](mtkview/autoresizedrawable.md) is [`false`](https://developer.apple.com/documentation/swift/false), set this value to change the size of the texture objects.

The default value is derived from the current view’s size, in native pixels.

## See Also

- [var colorPixelFormat: MTLPixelFormat](mtkview/colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
- [var colorspace: CGColorSpace?](mtkview/colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](mtkview/framebufferonly.md)
  A Boolean value that determines whether the drawable’s textures are used only for rendering.
- [var preferredDrawableSize: CGSize](mtkview/preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var autoResizeDrawable: Bool](mtkview/autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](mtkview/clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/drawablesize)*