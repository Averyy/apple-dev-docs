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

Passing an empty [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) to the `options` parameter is the equivalent of calling [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md). In Swift, pass `[]` to represent an empty option set, and in Objective-C, pass [`MTLBlitOptionNone`](mtlblitoption/mtlblitoptionnone.md).

## Parameters

- `sourceBuffer`: A buffer the command copies data from.
- `sourceOffset`: A byte offset within   that the command copies from, which needs to be a multiple of the destination texture’s pixel size, in bytes.
- `sourceBytesPerRow`: If   uses a compressed pixel format, set   to the number of bytes between the starts of two row blocks.
- `sourceBytesPerImage`: Set this value to   for 2D textures, which means   is equal to  .
- `sourceSize`: If   uses a compressed pixel format, set   to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp   to the edge of the texture.
- `destinationTexture`: A texture with an   property value of   that the command copies data to.
- `destinationSlice`: For textures that use a combined depth/stencil pixel format, configure the   parameter appropriately.
- `destinationLevel`: A mipmap level within  .
- `destinationOrigin`: Assign   to each dimension that’s not relevant to  . For example:
- `options`: If the texture’s pixel format is a PVRTC format, set   to  .

## See Also

- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command to copy image data from a source buffer into a destination texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:))*