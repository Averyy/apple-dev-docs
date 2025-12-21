# copy(sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)

**Framework**: Metal  
**Kind**: method

Encodes a command that copies image data from a slice of a texture instance to a buffer, with options for special texture formats.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationBuffer: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption = [])
```

## Parameters

- `sourceTexture`: An   texture that the command copies data from. To read the source   texture contents, you need to set its   property   to   prior to drawing into it.
- `sourceSlice`: A slice within   the command uses as a starting point to copy   data from. Set this to   if   isn’t a texture array or a   cube texture.
- `sourceLevel`: A mipmap level within  .
- `sourceOrigin`: An   instance that represents a location within    that the command begins copying data from. Assign   to each dimension   that’s not relevant to  .
- `sourceSize`: An   instance that represents the size of the region, in pixels,   that the command copies from  , starting at  .   Assign   to each dimension that’s not relevant to  .   If   uses a compressed pixel format, set   to a   multiple of the     block size.   If the block extends outside the bounds of the texture, clamp    to the edge of the texture.
- `destinationBuffer`: An   instance the command copies data to.
- `destinationOffset`: A byte offset within   the command copies to. The value   you provide as this argument needs to be a multiple of   pixel size,   in bytes.
- `destinationBytesPerRow`: The number of bytes between adjacent rows of pixels in  .   This value must be a multiple of   pixel size, in bytes,   and less than or equal to the product of   pixel size,   in bytes, and the largest pixel width   type allows. If    uses a compressed pixel format, set    to the number of bytes between the starts of two row blocks.
- `destinationBytesPerImage`: The number of bytes between each 2D image of a 3D texture. This value must   be a multiple of   pixel size, in bytes. Set this value to    if     value is  .
- `options`: A   value that applies to textures with applicable pixel   formats, such as combined depth/stencil or PVRTC formats. If     is a combined depth/stencil format, set    to either   or   , but not both.   If     is a PVRTC format, set    to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationbuffer:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:))*