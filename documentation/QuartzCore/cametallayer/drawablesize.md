# drawableSize

**Framework**: Core Animation  
**Kind**: property

The size, in pixels, of textures for rendering layer content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var drawableSize: CGSize { get set }
```

#### Discussion

By default, a layer creates textures sized to match its content—that is, this property’s value is the layer’s [`bounds`](calayer/bounds.md) size multiplied by its [`contentsScale`](calayer/contentsscale.md) factor.

## See Also

- [var pixelFormat: MTLPixelFormat](cametallayer/pixelformat.md)
  The pixel format of the layer’s textures.
- [var colorspace: CGColorSpace?](cametallayer/colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](cametallayer/framebufferonly.md)
  A Boolean value that determines whether the layer’s textures are used only for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/drawablesize)*