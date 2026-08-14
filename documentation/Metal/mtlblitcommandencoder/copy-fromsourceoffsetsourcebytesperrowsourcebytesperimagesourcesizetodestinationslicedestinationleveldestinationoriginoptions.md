# copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy image data from a source buffer into a destination texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceBuffer: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)
```

#### Discussion

Passing an empty [`OptionSet`](https://developer.apple.com/documentation/swift/optionset) to the `options` parameter is the equivalent of calling [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md). In Swift, pass `[]` to represent an empty option set, and in Objective-C, pass [`MTLBlitOptionNone`](mtlblitoption/mtlblitoptionnone.md).

## Parameters

- `sourceBuffer`: A buffer the command copies data from.
- `sourceOffset`: A byte offset within `sourceBuffer` that the command copies from, which needs to be a multiple of the destination texture’s pixel size, in bytes.
- `sourceBytesPerRow`: The number of bytes between adjacent rows of pixels in the source buffer’s memory, which needs to be: - A multiple of the source texture’s pixel size, in bytes
- Less than or equal to the product of the destination texture’s pixel size, in bytes, and the largest pixel width the destination texture’s type allows If `destinationTexture` uses a compressed pixel format, set `sourceBytesPerRow` to the number of bytes between the starts of two row blocks.
- `sourceBytesPerImage`: The number of bytes between each 2D image of a 3D texture. This value needs to be a multiple of the source texture’s pixel size, in bytes. Set this value to `0` for 2D textures, which means `sourceSize.`[`depth`](mtlsize/depth.md) is equal to `1`.
- `sourceSize`: An [`MTLSize`](mtlsize.md) instance, which can represent a 3D region, that instructs the command how many pixels to copy to `destinationTexture`, starting at `destinationOrigin`. Assign `1` to each dimension that’s not relevant to `destinationTexture`. For example: - If the destination texture is a 2D texture, set the size’s [`depth`](mtlsize/depth.md) property to `1`.
- If the destination texture is a 1D texture, set the size’s [`height`](mtlsize/height.md) and [`depth`](mtlsize/depth.md) properties to `1`. If `destinationTexture` uses a compressed pixel format, set `sourceSize` to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp `sourceSize` to the edge of the texture.
- `destinationTexture`: A texture with an [`isFramebufferOnly`](mtltexture/isframebufferonly.md) property value of [`false`](https://developer.apple.com/documentation/swift/false) that the command copies data to.
- `destinationSlice`: A slice within `destinationTexture`. For textures that use a combined depth/stencil pixel format, configure the `options` parameter appropriately.
- `destinationLevel`: A mipmap level within `destinationTexture`.
- `destinationOrigin`: A location within `destinationTexture` that the command begins copying data to. Assign `0` to each dimension that’s not relevant to `destinationTexture`. For example: - If the destination texture is a 2D texture, set the origin’s [`z`](mtlorigin/z.md) property to `0`.
- If the destination texture is a 1D texture, set the origin’s [`y`](mtlorigin/y.md) and [`z`](mtlorigin/z.md) properties to `0`.
- `options`: An option set that applies to textures with applicable pixel formats, such as combined depth/stencil or PVRTC formats. If the texture’s pixel format is a combined depth/stencil format, set `options` to either [`depthFromDepthStencil`](mtlblitoption/depthfromdepthstencil.md) or [`stencilFromDepthStencil`](mtlblitoption/stencilfromdepthstencil.md), but not both. If the texture’s pixel format is a PVRTC format, set `options` to [`rowLinearPVRTC`](mtlblitoption/rowlinearpvrtc.md).

## See Also

- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command to copy image data from a source buffer into a destination texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:))*