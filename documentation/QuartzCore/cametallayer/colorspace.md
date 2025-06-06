# colorspace

**Framework**: Core Animation  
**Kind**: property

The color space of the rendered content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var colorspace: CGColorSpace? { get set }
```

#### Discussion

Set this value to specify a color space for the contents of the layer. When a color space is present, Core Animation performs any necessary color space transformations when compositing this content.

The default value is `nil`, indicating that the rendered content isn’t color-matched.

## See Also

- [var pixelFormat: MTLPixelFormat](cametallayer/pixelformat.md)
  The pixel format of the layer’s textures.
- [var framebufferOnly: Bool](cametallayer/framebufferonly.md)
  A Boolean value that determines whether the layer’s textures are used only for rendering.
- [var drawableSize: CGSize](cametallayer/drawablesize.md)
  The size, in pixels, of textures for rendering layer content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/colorspace)*