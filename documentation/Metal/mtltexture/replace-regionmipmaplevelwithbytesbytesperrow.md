# replace(region:mipmapLevel:withBytes:bytesPerRow:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies a block of pixels into a section of texture slice 0.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func replace(region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafeRawPointer, bytesPerRow: Int)
```

## Mentions

- [Optimizing Texture Data](optimizing-texture-data.md)
- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
- [Copying Data into or out of Mipmaps](copying-data-into-or-out-of-mipmaps.md)
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Discussion

This method runs on the CPU and immediately copies the pixel data into the texture. It doesn’t synchronize against any GPU accesses to the texture. Ensure all operations that write or render to the texture complete before reading the texture’s contents, using one of the following methods:

- Synchronize on the GPU with a [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) or [`synchronize(texture:slice:level:)`](mtlblitcommandencoder/synchronize(texture:slice:level:).md) command in an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md).
- Synchronize on the CPU with a callback passed to the [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) method to handle completion asynchronously, or the [`waitUntilCompleted()`](mtlcommandbuffer/waituntilcompleted().md) method to block thread execution until the GPU work completes.

If the texture image has a compressed pixel format, only write to block-aligned regions. If the size of a dimension of region isn’t a multiple of the block size, then include both the edge block and space up to the texture dimensions in `bytesPerRow`.

To copy your data to a private texture, copy your data to a temporary texture with non-private storage, and then use an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) to copy the data to the private texture for GPU use.

## Parameters

- `region`: The location of a block of pixels in the texture slice. The region must be within the dimensions of the slice.
- `level`: A zero-indexed value that specifies which mipmap level is the destination. If the texture doesn’t have mipmaps, use  .
- `pixelBytes`: A pointer to the bytes in memory to copy.
- `bytesPerRow`: Nonzero values smaller than the texture width or not a multiple of the pixel size cause an error.

## See Also

- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
- [func replace(region: MTLRegion, mipmapLevel: Int, slice: Int, withBytes: UnsafeRawPointer, bytesPerRow: Int, bytesPerImage: Int)](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md)
  Copies pixel data into a section of a texture slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:))*