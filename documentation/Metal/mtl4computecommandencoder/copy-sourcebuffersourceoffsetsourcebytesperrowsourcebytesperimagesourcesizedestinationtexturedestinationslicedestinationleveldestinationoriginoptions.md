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

- `sourceBuffer`: An   instance the command copies data from.
- `sourceOffset`: A byte offset within   the command copies from. Set this value to   a multiple of   pixel size, in bytes.
- `sourceBytesPerRow`: The number of bytes between adjacent rows of pixels in  . Set this value to   a multiple of   pixel size, in bytes, and less than or equal to   the product of   pixel size, in bytes, and the largest pixel width    type allows. If   uses a compressed pixel format,   set   to the number of bytes between the starts of two row blocks.
- `sourceBytesPerImage`: The number of bytes between each 2D image of a 3D texture. Set this value to a   multiple of   pixel size, in bytes, or    if     value is  .
- `sourceSize`: An   instance that represents the size of the region in   , in pixels, that the command copies data to, starting at   . Assign   to each dimension that’s not relevant to   . If   uses a compressed pixel format,   set   to a multiple of      block size. If the block extends outside the bounds of the texture, clamp    to the edge of the texture.
- `destinationTexture`: An   instance the command copies data to. In order to copy the contents into   the destination texture, set its   property to    and don’t   use a combined depth/stencil  .
- `destinationSlice`: A slice within   the command uses as its starting point for   copying data to. Set this to   if   isn’t a texture array   or a cube texture.
- `destinationLevel`: A mipmap level within   the command copies data to.
- `destinationOrigin`: An   instance that represents a location within    that the command begins copying data to. Assign   to each dimension that’s not   relevant to  .
- `options`: An   value that applies to textures with applicable pixel formats,   such as combined depth/stencil or PVRTC formats. If     is a combined depth/stencil format, set   to   either   or   , but not both.   If     is a PVRTC format, set    to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:options:))*