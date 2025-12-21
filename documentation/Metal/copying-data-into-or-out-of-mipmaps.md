# Copying data into or out of mipmaps

**Framework**: Metal

Specify which mipmaps that the data transfer affects.

#### Overview

When you copy data between resources, and the source or destination is a texture, specify which mipmaps that the data transfer affects.

##### Copy Data From System Memory to a Mipmap

When you copy data from system memory into a texture, using the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) or similar method, state which mipmap is the destination of that copy.

Call this routine once for each mipmap you want to fill, changing the region to match the size of the mipmap level you’re writing to.

##### Copy Mipmap Data Between Metal Resources

If you already have data in Metal resources, use an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) to copy data to and from different mipmaps in a texture.

To copy all matching data between two textures, encode a command using the [`copy(from:to:)`](mtlblitcommandencoder/copy(from:to:).md): method. The two textures need to have the same pixel format and type. Metal copies all matching mipmap sizes to the destination texture.

To copy a selection of mipmaps from one texture to another, use the [`copy(from:sourceSlice:sourceLevel:to:destinationSlice:destinationLevel:sliceCount:levelCount:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:to:destinationslice:destinationlevel:slicecount:levelcount:).md) method. Specify the first source mipmap level and first destination mipmap level, both of which need to have the same dimensions. Also specify the number of mipmap levels you want to copy.

For example, the following code assumes that the destination texture is twice as large in both dimensions as the source texture. Mipmap `1` in the destination matches the size of the source mipmap `0`, so the code passes `0` as the source level and `1` as the destination level. It also passes `5` as the level count to copy `5` mipmaps.

If you need to copy data between buffers and textures, encode a separate blit command for each mipmap level to copy. See [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) for other methods that copy data to and from textures.

## See Also

- [Improving texture sampling quality and performance with mipmaps](improving-texture-sampling-quality-and-performance-with-mipmaps.md)
  Avoid texture-rendering artifacts and reduce the GPU’s workload by creating smaller versions of a texture.
- [Creating a mipmapped texture](creating-a-mipmapped-texture.md)
  Decide whether a texture that you’re creating needs mipmaps.
- [Generating mipmap data](generating-mipmap-data.md)
  Create your mipmaps either when you author content or at runtime.
- [Adding mipmap filtering to samplers](adding-mipmap-filtering-to-samplers.md)
  Specify how the GPU samples mipmaps in your textures.
- [Restricting access to specific mipmaps](restricting-access-to-specific-mipmaps.md)
  Set the range of mipmap levels that a sampler can access.
- [Predicting which mips the GPU samples with level-of-detail queries](predicting-which-mips-the-gpu-samples-with-level-of-detail-queries.md)
  Determine in advance which mipmap levels the GPU requires to sample a texture.
- [Dynamically adjusting texture level of detail](dynamically-adjusting-texture-level-of-detail.md)
  Defer generating or loading larger mipmaps until that level of detail is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/copying-data-into-or-out-of-mipmaps)*