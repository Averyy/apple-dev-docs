# autoResizeDrawable

**Framework**: MetalKit  
**Kind**: property

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
@MainActor
var autoResizeDrawable: Bool { get set }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/swift/true), the view automatically resizes its underlying color, depth, stencil, and multisample textures when the view is resized. If the value is [`false`](https://developer.apple.com/documentation/swift/false), you must explicitly set [`drawableSize`](mtkview/drawablesize.md) to change the size of these objects.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

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
- [var clearColor: MTLClearColor](mtkview/clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/autoresizedrawable)*