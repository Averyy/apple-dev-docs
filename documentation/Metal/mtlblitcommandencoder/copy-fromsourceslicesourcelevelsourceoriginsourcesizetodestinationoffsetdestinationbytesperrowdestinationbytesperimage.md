# copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies image data from a texture slice to a buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to destinationBuffer: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int)
```

## Mentions

- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)

#### Discussion

This method is the equivalent of passing an empty [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) to the `options` parameter of [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md). In Swift, pass `[]` to represent an empty option set, and in Objective-C, pass [`MTLBlitOptionNone`](mtlblitoption/mtlblitoptionnone.md).

> ❗ **Important**:  If the pixel format of `sourceTexture` is a PVRTC format, use [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md) instead.

 If the pixel format of `sourceTexture` is a PVRTC format, use [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md) instead.

## Parameters

- `sourceTexture`: A texture with an   property value of   that the command copies data from.
- `sourceSlice`: For textures that use a combined depth/stencil pixel format, call the   method instead. Configure that method’s   parameter appropriately.
- `sourceLevel`: A mipmap level within  .
- `sourceOrigin`: Assign   to each dimension that’s not relevant to  . For example:
- `sourceSize`: If   uses a compressed pixel format, set   to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp   to the edge of the texture.
- `destinationBuffer`: A buffer the command copies data to.
- `destinationOffset`: A byte offset within   the command copies to, which needs to be a multiple of the source texture’s pixel size, in bytes.
- `destinationBytesPerRow`: If   uses a compressed pixel format, set   to the number of bytes between the starts of two row blocks.
- `destinationBytesPerImage`: Set this value to   for 2D textures, which means   is equal to  .

## See Also

- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md)
  Encodes a command that copies image data from a texture slice to a buffer, and provides options for special texture formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:))*