# framebufferOnly

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL framebufferOnly;
```

## Discussion

If the value is [`true`](../../Swift/true.md) (the default), the [`CAMetalLayer`](../cametallayer.md) class allocates its [`MTLTexture`](../../Metal/mtltexture.md) objects with only the [`renderTarget`](../../Metal/mtltextureusage/rendertarget.md) usage flag. Core Animation can then optimize the texture for display purposes. However, you may not sample, read from, or write to those textures. To support sampling and pixel read/write operations (at a cost to performance), set this value to [`false`](../../Swift/false.md).

## See Also

### Configuring the Layer’s Drawable Objects
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The pixel format of the layer’s textures.
- [var colorspace: CGColorSpace?](./colorspace.md)
  The color space of the rendered content.
- [var drawableSize: CGSize](./drawablesize.md)
  The size, in pixels, of textures for rendering layer content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/framebufferonly)*