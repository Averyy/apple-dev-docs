# preferredDrawableSize

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The recommended dimensions of the drawable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredDrawableSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize preferredDrawableSize;
```

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
- [var autoResizeDrawable: Bool](./autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](./clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/preferreddrawablesize)*