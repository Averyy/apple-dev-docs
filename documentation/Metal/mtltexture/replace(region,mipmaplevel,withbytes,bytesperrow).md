# replace(region:mipmapLevel:withBytes:bytesPerRow:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Copies a block of pixels into a section of texture slice 0.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func replace(region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafeRawPointer, bytesPerRow: Int)
```

```objc
- (void) replaceRegion:(MTLRegion) region mipmapLevel:(NSUInteger) level withBytes:(const void *) pixelBytes bytesPerRow:(NSUInteger) bytesPerRow;
```

## Mentions

- [Optimizing texture data](../optimizing-texture-data.md)
- [Copying data into or out of mipmaps](../copying-data-into-or-out-of-mipmaps.md)
- [Copying data to a private resource](../copying-data-to-a-private-resource.md)
- [Synchronizing a managed resource in macOS](../synchronizing-a-managed-resource-in-macos.md)

## Discussion

This method runs on the CPU and immediately copies the pixel data into the texture. It doesn’t synchronize against any GPU memory operations to the texture. Ensure all operations that write or render to the texture complete before reading the texture’s contents using one of the following methods:

- Synchronize on the GPU with a [`synchronize(resource:)`](../mtlblitcommandencoder/synchronize%28resource%29.md) or [`synchronize(texture:slice:level:)`](../mtlblitcommandencoder/synchronize%28texture,slice,level%29.md) command in an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md).
- Synchronize on the CPU with a callback passed to the [`addCompletedHandler(_:)`](../mtlcommandbuffer/addcompletedhandler%28_%29.md) method to handle completion asynchronously, or the [`waitUntilCompleted()`](../mtlcommandbuffer/waituntilcompleted%28%29.md) method to block thread execution until the GPU work completes.

If the texture image has a compressed pixel format, only write to block-aligned regions. If the size of a dimension of region isn’t a multiple of the block size, then include both the edge block and space up to the texture dimensions in `bytesPerRow`.

To copy your data to a private texture, copy your data to a temporary texture with non-private storage, and then use an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md) to copy the data to the private texture for GPU use.

## Parameters

- `region`: The location of a block of pixels in the texture slice. The region needs to be within the dimensions of the slice.
- `level`: A zero-indexed value that specifies which mipmap level is the destination. If the texture doesn’t have mipmaps, use `0`.
- `pixelBytes`: A pointer to the bytes in memory to copy.
- `bytesPerRow`: The stride, in bytes, of one row in the source data. For [`MTLTextureType.type1D`](../mtltexturetype/type1d.md) and [`MTLTextureType.type1DArray`](../mtltexturetype/type1darray.md), use `0`. For raw and packed pixel types, the stride is the number of pixels in one row. For compressed pixel formats, the stride is the number of bytes from the beginning of one row of blocks to the beginning of the next. When source data consists of only a single row, use `0`.

  Your data type determines how you should compute `bytesPerRow`:

  - For raw or packed pixel data, use a value greater than or equal to the size of data in one row, and less than [`max`](../../Swift/int32/max.md) `* pixel size`.
  - For compressed pixel data, use a multiple of the compression block size. When working with PowerVR Texture Compression (PVRTC), use `0.`

  Nonzero values smaller than the texture width or not a multiple of the pixel size cause an error.

## See Also

### Related Documentation
- [enum MTLPixelFormat](../mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
### Copying data into a texture image
- [func replace(region: MTLRegion, mipmapLevel: Int, slice: Int, withBytes: UnsafeRawPointer, bytesPerRow: Int, bytesPerImage: Int)](./replace%28region,mipmaplevel,slice,withbytes,bytesperrow,bytesperimage%29.md)
  Copies pixel data into a section of a texture slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:))*