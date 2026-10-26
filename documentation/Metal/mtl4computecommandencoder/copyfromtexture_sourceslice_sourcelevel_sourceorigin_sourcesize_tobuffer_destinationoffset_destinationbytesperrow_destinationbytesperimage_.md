# copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that copies image data from a slice of an [`MTLTexture`](../mtltexture.md) instance to an [`MTLBuffer`](../mtlbuffer.md) instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) copyFromTexture:(id<MTLTexture>) sourceTexture sourceSlice:(NSUInteger) sourceSlice sourceLevel:(NSUInteger) sourceLevel sourceOrigin:(MTLOrigin) sourceOrigin sourceSize:(MTLSize) sourceSize toBuffer:(id<MTLBuffer>) destinationBuffer destinationOffset:(NSUInteger) destinationOffset destinationBytesPerRow:(NSUInteger) destinationBytesPerRow destinationBytesPerImage:(NSUInteger) destinationBytesPerImage;
```

## Parameters

- `sourceTexture`: An [`MTLTexture`](../mtltexture.md) texture that the command copies data from. To read the source texture contents, you need to set its [`isFramebufferOnly`](../mtltexture/isframebufferonly.md) property to [`false`](../../Swift/false.md) prior to drawing into it.
- `sourceSlice`: A slice within `sourceTexture` the command uses as a starting point to copy data from. Set this to `0` if `sourceTexture` isn’t a texture array or a cube texture.
- `sourceLevel`: A mipmap level within `sourceTexture`.
- `sourceOrigin`: An [`MTLOrigin`](../mtlorigin.md) instance that represents a location within `sourceTexture` that the command begins copying data from. Assign `0` to each dimension that’s not relevant to `sourceTexture`.
- `sourceSize`: An [`MTLSize`](../mtlsize.md) instance that represents the size of the region, in pixels, that the command copies from `sourceTexture`, starting at `sourceOrigin`. Assign `1` to each dimension that’s not relevant to `sourceTexture`. If `sourceTexture` uses a compressed pixel format, set `sourceSize` to a multiple of the `sourceTexture's` [`pixelFormat`](../mtltexture/pixelformat.md) block size. If the block extends outside the bounds of the texture, clamp `sourceSize` to the edge of the texture.
- `destinationBuffer`: An [`MTLBuffer`](../mtlbuffer.md) instance the command copies data to.
- `destinationOffset`: A byte offset within `destinationBuffer` the command copies to. The value you provide as this argument needs to be a multiple of `sourceTexture's` pixel size, in bytes.
- `destinationBytesPerRow`: The number of bytes between adjacent rows of pixels in `destinationBuffer`. This value must be a multiple of `sourceTexture's` pixel size, in bytes, and less than or equal to the product of `sourceTexture's` pixel size, in bytes, and the largest pixel width `sourceTexture’s` type allows. If `sourceTexture` uses a compressed pixel format, set `destinationBytesPerRow` to the number of bytes between the starts of two row blocks.
- `destinationBytesPerImage`: The number of bytes between each 2D image of a 3D texture. This value must be a multiple of `sourceTexture's` pixel size, in bytes. Set this value to `0` if `sourceSize's` [`depth`](../mtlsize/depth.md) value is `1`.

## See Also

### Encoding texture-to-buffer copy commands
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](./copyfromtexture_sourceslice_sourcelevel_sourceorigin_sourcesize_tobuffer_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_.md)
  Encodes a command that copies image data from a slice of a texture instance to a buffer, with options for special texture formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copyfromtexture:sourceslice:sourcelevel:sourceorigin:sourcesize:tobuffer:destinationoffset:destinationbytesperrow:destinationbytesperimage:)*