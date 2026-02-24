# copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies image data from a texture slice to a buffer, and provides options for special texture formats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to destinationBuffer: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)
```

#### Discussion

Passing an empty [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) to the `options` parameter is the equivalent of calling [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:).md). In Swift, pass `[]` to represent an empty option set, and in Objective-C, pass [`MTLBlitOptionNone`](mtlblitoption/mtlblitoptionnone.md).

## Parameters

- `sourceTexture`: A texture with an [`isFramebufferOnly`](mtltexture/isframebufferonly.md) property value of [`false`](https://developer.apple.com/documentation/Swift/false) that the command copies data from.
- `sourceSlice`: A slice within `sourceTexture`. For textures that use a combined depth/stencil pixel format, configure the `options` parameter appropriately.
- `sourceLevel`: A mipmap level within `sourceTexture`.
- `sourceOrigin`: A location within `sourceTexture` that the command begins copying data from. Assign `0` to each dimension that’s not relevant to `sourceTexture`. For example: - If the source texture is a 2D texture, set the origin’s [`z`](mtlorigin/z.md) property to `0`.
- If the source texture is a 1D texture, set the origin’s [`y`](mtlorigin/y.md) and [`z`](mtlorigin/z.md) properties to `0`.
- `sourceSize`: An [`MTLSize`](mtlsize.md) instance, which can represent a 3D region, that instructs the command how many pixels to copy from `sourceTexture`, starting at `sourceOrigin`. Assign `1` to each dimension that’s not relevant to `sourceTexture`. For example: - If the source texture is a 2D texture, set the size’s [`depth`](mtlsize/depth.md) property to `1`.
- If the source texture is a 1D texture, set the size’s [`height`](mtlsize/height.md) and [`depth`](mtlsize/depth.md) properties to `1`. If `sourceTexture` uses a compressed pixel format, set `sourceSize` to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp `sourceSize` to the edge of the texture.
- `destinationBuffer`: A buffer the command copies data to.
- `destinationOffset`: A byte offset within `destinationBuffer` the command copies to, which needs to be a multiple of the source texture’s pixel size, in bytes.
- `destinationBytesPerRow`: The number of bytes between adjacent rows of pixels in the destination buffer’s memory, which needs to be: - A multiple of the source texture’s pixel size, in bytes
- Less than or equal to the product of the source texture’s pixel size, in bytes, and the largest pixel width the source texture’s type allows If `sourceTexture` uses a compressed pixel format, set `destinationBytesPerRow` to the number of bytes between the starts of two row blocks.
- `destinationBytesPerImage`: The number of bytes between each 2D image of a 3D texture. This value needs to be a multiple of the source texture’s pixel size, in bytes. Set this value to `0` for 2D textures, which means `sourceSize.`[`depth`](mtlsize/depth.md) is equal to `1`.
- `options`: An option set that applies to textures with applicable pixel formats, such as combined depth/stencil or PVRTC formats. If the texture’s pixel format is a combined depth/stencil format, set `options` to either [`depthFromDepthStencil`](mtlblitoption/depthfromdepthstencil.md) or [`stencilFromDepthStencil`](mtlblitoption/stencilfromdepthstencil.md), but not both. If the texture’s pixel format is a PVRTC format, set `options` to [`rowLinearPVRTC`](mtlblitoption/rowlinearpvrtc.md).

## See Also

- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:).md)
  Encodes a command that copies image data from a texture slice to a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:))*