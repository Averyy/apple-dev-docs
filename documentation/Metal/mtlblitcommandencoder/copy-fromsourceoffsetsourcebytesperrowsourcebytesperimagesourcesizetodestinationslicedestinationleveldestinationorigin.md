# copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy image data from a source buffer into a destination texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceBuffer: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)
```

## Mentions

- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)

#### Discussion

This method is the equivalent of passing an empty [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) to the `options` parameter of [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:).md). In Swift, pass `[]` to represent an empty option set, and in Objective-C, pass [`MTLBlitOptionNone`](mtlblitoption/mtlblitoptionnone.md).

> ❗ **Important**:  If the pixel format of `sourceTexture` is a PVRTC format, use [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:).md) instead.

 If the pixel format of `sourceTexture` is a PVRTC format, use [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:).md) instead.

## Parameters

- `sourceBuffer`: A buffer the command copies data from.
- `sourceOffset`: A byte offset within   that the command copies from, which needs to be a multiple of the destination texture’s pixel size, in bytes.
- `sourceBytesPerRow`: If   uses a compressed pixel format, set   to the number of bytes between the starts of two row blocks.
- `sourceBytesPerImage`: Set this value to   for 2D textures, which means   is equal to  .
- `sourceSize`: If   uses a compressed pixel format, set   to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp   to the edge of the texture.
- `destinationTexture`: A texture with an   property value of   that the command copies data to.
- `destinationSlice`: For textures that use a combined depth/stencil pixel format, call the   method instead. Configure that method’s   parameter appropriately.
- `destinationLevel`: A mipmap level within  .
- `destinationOrigin`: Assign   to each dimension that’s not relevant to  . For example:

## See Also

- [func copy(from: any MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:).md)
  Encodes a command to copy image data from a source buffer into a destination texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:))*