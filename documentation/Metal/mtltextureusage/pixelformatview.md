# pixelFormatView

**Framework**: Metal  
**Kind**: property

An option to create texture views with a different component layout.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var pixelFormatView: MTLTextureUsage { get }
```

## Mentions

- [Optimizing texture data](optimizing-texture-data.md)

#### Discussion

Set this option if you need to call any of these methods of the texture to create a texture view with a different component layout:

- [`makeTextureView(pixelFormat:)`](mtltexture/maketextureview(pixelformat:).md)
- [`makeTextureView(pixelFormat:textureType:levels:slices:)`](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:).md)
- [`newTextureViewWithPixelFormat:textureType:levels:slices:`](mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:.md)
- [`makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)`](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:).md)
- [`newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:`](mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:swizzle:.md)

For example, if your texture uses the [`MTLPixelFormat.rgba8Unorm`](mtlpixelformat/rgba8unorm.md) pixel format, you can reinterpret the data as [`MTLPixelFormat.r32Uint`](mtlpixelformat/r32uint.md). The pixel layout is considered different if the number of components differs, or if their size or order is different from the components in the original pixel format.

Don’t set this option if your texture view needs to read the component values in a different order. Instead, create a texture view with a swizzle pattern that specifies the new order.

Don’t set this option if your texture view only converts between linear space and sRGB. For example, if your texture uses the [`MTLPixelFormat.rgba8Unorm`](mtlpixelformat/rgba8unorm.md) pixel format and your texture view uses [`MTLPixelFormat.bgra8Unorm_srgb`](mtlpixelformat/bgra8unorm_srgb.md).

In iOS devices with GPU family 5 and later, Metal doesn’t apply lossless compression to the given texture if you set this option.

## See Also

- [static var unknown: MTLTextureUsage](mtltextureusage/unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](mtltextureusage/shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderWrite: MTLTextureUsage](mtltextureusage/shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var shaderAtomic: MTLTextureUsage](mtltextureusage/shaderatomic.md)
  An option that enables atomic memory operations on texture elements in shader code.
- [static var renderTarget: MTLTextureUsage](mtltextureusage/rendertarget.md)
  An option for rendering to the texture in a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/pixelformatview)*