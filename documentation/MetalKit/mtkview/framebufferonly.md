# framebufferOnly

**Framework**: MetalKit  
**Kind**: property

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
@MainActor
var framebufferOnly: Bool { get set }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/swift/true) (the default), the underlying [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) object allocates its textures with only the [`renderTarget`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/renderTarget) usage flag. Core Animation can then optimize the textures for display purposes. However, you may not sample, read from, or write to those textures. If the value is [`false`](https://developer.apple.com/documentation/swift/false), you can sample or perform read/write operations on the textures, but at a cost to performance.

## See Also

- [var colorPixelFormat: MTLPixelFormat](mtkview/colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
- [var colorspace: CGColorSpace?](mtkview/colorspace.md)
  The color space of the rendered content.
- [var drawableSize: CGSize](mtkview/drawablesize.md)
  The current size of drawable textures.
- [var preferredDrawableSize: CGSize](mtkview/preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var autoResizeDrawable: Bool](mtkview/autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](mtkview/clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/framebufferonly)*