# copy(sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:)

**Framework**: Metal  
**Kind**: method

Encodes a command to copy image data from a buffer into a texture with options for special texture formats.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption = [])
```

## Parameters

- `sourceBuffer`: An [`MTLBuffer`](mtlbuffer.md) instance the command copies data from.
- `sourceOffset`: A byte offset within `sourceBuffer` the command copies from. Set this value to a multiple of `destinationTexture's` pixel size, in bytes.
- `sourceBytesPerRow`: The number of bytes between adjacent rows of pixels in `sourceBuffer`. Set this value to a multiple of `destinationTexture's` pixel size, in bytes, and less than or equal to the product of `destinationTexture's` pixel size, in bytes, and the largest pixel width `destinationTexture's` type allows. If `destinationTexture` uses a compressed pixel format, set `sourceBytesPerRow` to the number of bytes between the starts of two row blocks.
- `sourceBytesPerImage`: The number of bytes between each 2D image of a 3D texture. Set this value to a multiple of `destinationTexture's` pixel size, in bytes, or `0` if `sourceSize's` [`depth`](mtlsize/depth.md) value is `1`.
- `sourceSize`: An [`MTLSize`](mtlsize.md) instance that represents the size of the region in `destinationTexture`, in pixels, that the command copies data to, starting at `destinationOrigin`. Assign `1` to each dimension that’s not relevant to `destinationTexture`. If `destinationTexture` uses a compressed pixel format, set `sourceSize` to a multiple of `destinationTexture's` [`pixelFormat`](mtltexture/pixelformat.md) block size. If the block extends outside the bounds of the texture, clamp `sourceSize` to the edge of the texture.
- `destinationTexture`: An [`MTLTexture`](mtltexture.md) instance the command copies data to. In order to copy the contents into the destination texture, set its [`isFramebufferOnly`](mtltexture/isframebufferonly.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) and don’t use a combined depth/stencil [`pixelFormat`](mtltexture/pixelformat.md).
- `destinationSlice`: A slice within `destinationTexture` the command uses as its starting point for copying data to. Set this to `0` if `destinationTexture` isn’t a texture array or a cube texture.
- `destinationLevel`: A mipmap level within `destinationTexture` the command copies data to.
- `destinationOrigin`: An [`MTLOrigin`](mtlorigin.md) instance that represents a location within `destinationTexture` that the command begins copying data to. Assign `0` to each dimension that’s not relevant to `destinationTexture`.
- `options`: An [`MTLBlitOption`](mtlblitoption.md) value that applies to textures with applicable pixel formats, such as combined depth/stencil or PVRTC formats. If `destinationTexture's` [`pixelFormat`](mtltexture/pixelformat.md) is a combined depth/stencil format, set `options` to either [`depthFromDepthStencil`](mtlblitoption/depthfromdepthstencil.md) or [`stencilFromDepthStencil`](mtlblitoption/stencilfromdepthstencil.md), but not both. If `destinationTexture's` [`pixelFormat`](mtltexture/pixelformat.md) is a PVRTC format, set `options` to [`rowLinearPVRTC`](mtlblitoption/rowlinearpvrtc.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:options:))*