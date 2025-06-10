# getBytes(_:bytesPerRow:bytesPerImage:from:mipmapLevel:slice:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies pixel data from the texture to a buffer in system memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func getBytes(_ pixelBytes: UnsafeMutableRawPointer, bytesPerRow: Int, bytesPerImage: Int, from region: MTLRegion, mipmapLevel level: Int, slice: Int)
```

#### Discussion

> ❗ **Important**:  Don’t use this method for textures where [`storageMode`](mtlresource/storagemode.md) is [`MTLStorageMode.private`](mtlstoragemode/private.md). Instead, copy data from the private texture with an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) to another texture accessible from the CPU, and then call this method on the accessible texture.

This method runs on the CPU and immediately copies the pixel data from the texture to system memory but doesn’t synchronize with any GPU texture accesses. Ensure all operations that write or render to the texture complete before reading the texture’s contents, using one of the following methods:

- Synchronize on the GPU with a [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) or [`synchronize(texture:slice:level:)`](mtlblitcommandencoder/synchronize(texture:slice:level:).md) command in an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md).
- Synchronize on the CPU with a callback passed to the [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) method to handle completion asynchronously, or the [`waitUntilCompleted()`](mtlcommandbuffer/waituntilcompleted().md) method to block thread execution until the GPU work completes.

For multisample textures, the method consecutively positions each sample within a pixel in memory and treats the pixels as part of one row.

## Parameters

- `pixelBytes`: A pointer to a destination buffer in system memory.
- `bytesPerRow`: Nonzero values smaller than the texture width or any values not a multiple of the pixel or block size cause an error.
- `bytesPerImage`: The stride between adjacent images in the destination buffer.
- `region`: The location of a block of pixels in the texture slice. For textures compressed as PVRTC, use the entire texture for the region.
- `level`: A zero-indexed value that selects the texture’s mipmap level as the method’s data source. Use   for textures that don’t have mipmaps.
- `slice`: A zero-indexed value specifying the destination texture slice:

## See Also

- [func getBytes(UnsafeMutableRawPointer, bytesPerRow: Int, from: MTLRegion, mipmapLevel: Int)](mtltexture/getbytes(_:bytesperrow:from:mipmaplevel:).md)
  Copies pixel data from the first slice of the texture to a buffer in system memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/getbytes(_:bytesperrow:bytesperimage:from:mipmaplevel:slice:))*