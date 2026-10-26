# newTextureViewWithPixelFormat:textureType:levels:slices:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (id<MTLTexture>) newTextureViewWithPixelFormat:(MTLPixelFormat) pixelFormat textureType:(MTLTextureType) textureType levels:(NSRange) levelRange slices:(NSRange) sliceRange;
```

#### Return Value

A new texture object that shares the same storage allocation of the calling texture object.

#### Discussion

The texture type can be cast between the targets listed in the following table.

| Original texture type | New texture type |
| --- | --- |
| [`MTLTextureType.type1D`](../mtltexturetype/type1d.md) | [`MTLTextureType.type1D`](../mtltexturetype/type1d.md) |
| [`MTLTextureType.type2D`](../mtltexturetype/type2d.md) | [`MTLTextureType.type2D`](../mtltexturetype/type2d.md) or [`MTLTextureType.type2DArray`](../mtltexturetype/type2darray.md) |
| [`MTLTextureType.type2DArray`](../mtltexturetype/type2darray.md), [`MTLTextureType.typeCube`](../mtltexturetype/typecube.md), or [`MTLTextureType.typeCubeArray`](../mtltexturetype/typecubearray.md) | [`MTLTextureType.type2D`](../mtltexturetype/type2d.md), [`MTLTextureType.type2DArray`](../mtltexturetype/type2darray.md), [`MTLTextureType.typeCube`](../mtltexturetype/typecube.md), or [`MTLTextureType.typeCubeArray`](../mtltexturetype/typecubearray.md) |
| [`MTLTextureType.type3D`](../mtltexturetype/type3d.md) | [`MTLTextureType.type3D`](../mtltexturetype/type3d.md) |

The `length` value of the `sliceRange` parameter needs to be `6` if the new texture type value is [`MTLTextureType.typeCube`](../mtltexturetype/typecube.md), or a multiple of `6` if the new texture type value is [`MTLTextureType.typeCubeArray`](../mtltexturetype/typecubearray.md).

For more information on pixel format restrictions, see [`makeTextureView(pixelFormat:)`](./maketextureview%28pixelformat%29.md)

## Parameters

- `pixelFormat`: A new pixel format, which needs to be compatible with the original pixel format.
- `textureType`: A new texture type, which can be cast according to the original texture type as listed in the table below.
- `levelRange`: A new base level range that restricts which mipmap levels are visible in the new texture.
- `sliceRange`: A new base slice range that restricts which array slices are visible in the new texture.

## Default Implementations

### MTLTexture Implementations
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>) -> (any MTLTexture)?](./maketextureview%28pixelformat,texturetype,levels,slices%29.md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.

## See Also

### Related Documentation
- [var parentRelativeLevel: Int](./parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var parent: (any MTLTexture)?](./parent.md)
  The parent texture used to create this texture, if any.
- [var parentRelativeSlice: Int](./parentrelativeslice.md)
  The base slice of the parent texture used to create this texture.
### Creating textures by reinterpreting existing texture data
- [func makeTextureView(pixelFormat: MTLPixelFormat) -> (any MTLTexture)?](./maketextureview%28pixelformat%29.md)
  Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [- newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:](./newtextureviewwithpixelformat_texturetype_levels_slices_swizzle_.md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:)*