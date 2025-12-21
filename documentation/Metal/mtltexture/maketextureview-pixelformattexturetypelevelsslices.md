# makeTextureView(pixelFormat:textureType:levels:slices:)

**Framework**: Metal  
**Kind**: method

Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 9.0+
- visionOS ?+

## Declaration

```swift
func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels levelRange: Range<Int>, slices sliceRange: Range<Int>) -> (any MTLTexture)?
```

#### Return Value

A new texture object that shares the same storage allocation of the calling texture object.

#### Discussion

The texture type can be cast between the targets listed in the following table.

| Original texture type | New texture type |
| --- | --- |
| [`MTLTextureType.type1D`](mtltexturetype/type1d.md) | [`MTLTextureType.type1D`](mtltexturetype/type1d.md) |
| [`MTLTextureType.type2D`](mtltexturetype/type2d.md) | [`MTLTextureType.type2D`](mtltexturetype/type2d.md) or [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md) |
| [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md), [`MTLTextureType.typeCube`](mtltexturetype/typecube.md), or [`MTLTextureType.typeCubeArray`](mtltexturetype/typecubearray.md) | [`MTLTextureType.type2D`](mtltexturetype/type2d.md), [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md), [`MTLTextureType.typeCube`](mtltexturetype/typecube.md), or [`MTLTextureType.typeCubeArray`](mtltexturetype/typecubearray.md) |
| [`MTLTextureType.type3D`](mtltexturetype/type3d.md) | [`MTLTextureType.type3D`](mtltexturetype/type3d.md) |

The `length` value of the `sliceRange` parameter needs to be `6` if the new texture type value is [`MTLTextureType.typeCube`](mtltexturetype/typecube.md), or a multiple of `6` if the new texture type value is [`MTLTextureType.typeCubeArray`](mtltexturetype/typecubearray.md).

For more information on pixel format restrictions, see [`makeTextureView(pixelFormat:)`](mtltexture/maketextureview(pixelformat:).md)

## Parameters

- `pixelFormat`: A new pixel format, which needs to be compatible with the original pixel format.
- `textureType`: A new texture type, which can be cast according to the original texture type as listed the table below.
- `levelRange`: A new base level range that restricts which mipmap levels are visible in the new texture.
- `sliceRange`: A new base slice range that restricts which array slices are visible in the new texture.

## See Also

- [var parentRelativeLevel: Int](mtltexture/parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var parent: (any MTLTexture)?](mtltexture/parent.md)
  The parent texture used to create this texture, if any.
- [var parentRelativeSlice: Int](mtltexture/parentrelativeslice.md)
  The base slice of the parent texture used to create this texture.
- [func makeTextureView(pixelFormat: MTLPixelFormat) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:).md)
  Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>, swizzle: MTLTextureSwizzleChannels) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:).md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/maketextureview(pixelformat:texturetype:levels:slices:))*