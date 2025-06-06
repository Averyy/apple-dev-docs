# makeTextureView(pixelFormat:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new view of the texture, reinterpreting its data using a different pixel format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeTextureView(pixelFormat: MTLPixelFormat) -> (any MTLTexture)?
```

#### Return Value

A new texture object that shares the same storage allocation of the texture.

#### Discussion

When you create a texture normally, Metal allocates memory for the textureʼs pixel data. These storage allocations can be quite large. You can reduce memory use and avoid copying texture data by using a —a texture object that shares another textureʼs storage allocation, reinterpreting the pixel data in some other format.

Not all pixel formats are compatible with one another. Reinterpretation of image data between pixel formats is supported within the following groups:

- All 8-, 16-, 32-, 64-, and 128-bit color formats are compatible with other formats with the same bit length.
- sRGB and non-sRGB forms of the same compressed format (for example, [`MTLPixelFormat.bc1_rgba`](mtlpixelformat/bc1_rgba.md) and [`MTLPixelFormat.bc1_rgba_srgb`](mtlpixelformat/bc1_rgba_srgb.md))
- Combined depth-stencil texture formats and the related format used to access the stencil from a shader (for example, [`MTLPixelFormat.depth24Unorm_stencil8`](mtlpixelformat/depth24unorm_stencil8.md) and [`MTLPixelFormat.x24_stencil8`](mtlpixelformat/x24_stencil8.md))

This method doesn’t change the original texture image data in any way, but it may drastically change how the data is interpreted. For example, given a texture with the [`MTLPixelFormat.rg16Uint`](mtlpixelformat/rg16uint.md) pixel format that contains image data for Red `0xFFFE` and Green `0x0001`, this method would reinterpret that data in an [`MTLPixelFormat.r32Uint`](mtlpixelformat/r32uint.md) format as Red `0x0001FFFE`.

Some format reinterpretations are supported but may not be useful. For example, this method considers the 32-bit packed color formats [`MTLPixelFormat.bgr10a2Unorm`](mtlpixelformat/bgr10a2unorm.md) and [`MTLDataType.rg11b10Float`](mtldatatype/rg11b10float.md) to be compatible, but it’s unlikely that the same data can be interpreted by both formats in a meaningful way.

Some format reinterpretations require you to create the source texture with a special usage flag. Set that flag only when necessary, as it can affect performance. For more details, see [`pixelFormatView`](mtltextureusage/pixelformatview.md).

## Parameters

- `pixelFormat`: A new pixel format, which must be compatible with the original pixel format.

## See Also

- [var parentRelativeLevel: Int](mtltexture/parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var parent: (any MTLTexture)?](mtltexture/parent.md)
  The parent texture used to create this texture, if any.
- [var parentRelativeSlice: Int](mtltexture/parentrelativeslice.md)
  The base slice of the parent texture used to create this texture.
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:).md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>, swizzle: MTLTextureSwizzleChannels) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:).md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/maketextureview(pixelformat:))*