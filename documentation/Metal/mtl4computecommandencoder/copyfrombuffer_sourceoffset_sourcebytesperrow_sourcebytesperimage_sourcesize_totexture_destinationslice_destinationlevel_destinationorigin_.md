# copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command to copy image data from a buffer instance into a texture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) copyFromBuffer:(id<MTLBuffer>) sourceBuffer sourceOffset:(NSUInteger) sourceOffset sourceBytesPerRow:(NSUInteger) sourceBytesPerRow sourceBytesPerImage:(NSUInteger) sourceBytesPerImage sourceSize:(MTLSize) sourceSize toTexture:(id<MTLTexture>) destinationTexture destinationSlice:(NSUInteger) destinationSlice destinationLevel:(NSUInteger) destinationLevel destinationOrigin:(MTLOrigin) destinationOrigin;
```

## Parameters

- `sourceBuffer`: A [`MTLBuffer`](../mtlbuffer.md) instance the command copies data from.
- `sourceOffset`: A byte offset within `sourceBuffer` the command copies from. Set this value to a multiple of `destinationTexture's` pixel size, in bytes.
- `sourceBytesPerRow`: The number of bytes between adjacent rows of pixels in `sourceBuffer`. Set this value to a multiple of `destinationTexture's` pixel size, in bytes, and less than or equal to the product of `destinationTexture's` pixel size, in bytes, and the largest pixel width `destinationTexture's` type allows. If `destinationTexture` uses a compressed pixel format, set `sourceBytesPerRow` to the number of bytes between the starts of two row blocks.
- `sourceBytesPerImage`: The number of bytes between each 2D image of a 3D texture. Set this value to a multiple of `destinationTexture's` pixel size, in bytes, or `0` if `sourceSize's` [`depth`](../mtlsize/depth.md) value is `1`.
- `sourceSize`: A [`MTLSize`](../mtlsize.md) instance that represents the size of the region in `destinationTexture`, in pixels, that the command copies data to, starting at `destinationOrigin`. Assign `1` to each dimension that’s not relevant to `destinationTexture`. If `destinationTexture` uses a compressed pixel format, set `sourceSize` to a multiple of `destinationTexture's` [`pixelFormat`](../mtltexture/pixelformat.md) block size. If the block extends outside the bounds of the texture, clamp `sourceSize` to the edge of the texture.
- `destinationTexture`: An [`MTLTexture`](../mtltexture.md) instance the command copies data to. In order to copy the contents into the destination texture, set its [`isFramebufferOnly`](../mtltexture/isframebufferonly.md) property to [`false`](../../Swift/false.md) and don’t use a combined depth/stencil [`pixelFormat`](../mtltexture/pixelformat.md).
- `destinationSlice`: A slice within `destinationTexture` the command uses as its starting point for copying data to. Set this to `0` if `destinationTexture` isn’t a texture array or a cube texture.
- `destinationLevel`: A mipmap level within `destinationTexture` the command copies data to.
- `destinationOrigin`: An [`MTLOrigin`](../mtlorigin.md) instance that represents a location within `destinationTexture` that the command begins copying data to. Assign `0` to each dimension that’s not relevant to `destinationTexture`.

## See Also

### Encoding buffer-to-texture copy commands
- [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](./copyfrombuffer_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_totexture_destinationslice_destinationlevel_destinationorigin_options_.md)
  Encodes a command to copy image data from a buffer into a texture with options for special texture formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copyfrombuffer:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:totexture:destinationslice:destinationlevel:destinationorigin:)*