# framebufferOnly

**Framework**: Core Animation  
**Kind**: property

A Boolean value that determines whether the layer’s textures are used only for rendering.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var framebufferOnly: Bool { get set }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/Swift/true) (the default), the [`CAMetalLayer`](cametallayer.md) class allocates its [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) objects with only the [`renderTarget`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/renderTarget) usage flag. Core Animation can then optimize the texture for display purposes. However, you may not sample, read from, or write to those textures. To support sampling and pixel read/write operations (at a cost to performance), set this value to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var pixelFormat: MTLPixelFormat](cametallayer/pixelformat.md)
  The pixel format of the layer’s textures.
- [var colorspace: CGColorSpace?](cametallayer/colorspace.md)
  The color space of the rendered content.
- [var drawableSize: CGSize](cametallayer/drawablesize.md)
  The size, in pixels, of textures for rendering layer content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/framebufferonly)*