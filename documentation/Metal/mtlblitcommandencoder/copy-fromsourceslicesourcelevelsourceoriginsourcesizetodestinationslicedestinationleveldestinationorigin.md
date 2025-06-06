# copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies image data from a texture’s slice into another slice.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)
```

## Mentions

- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)

#### Discussion

For textures that use a PVRTC pixel format, you can use this method to copy the entire texture, but not a subregion of the texture.

> ❗ **Important**:  Copying data to overlapping regions within the same texture may result in unexpected behavior.

 Copying data to overlapping regions within the same texture may result in unexpected behavior.

## Parameters

- `sourceTexture`: For a texture that uses a compressed pixel format, align the copy region (  and  ) to the pixel format’s block size.
- `sourceSlice`: A slice within  .
- `sourceLevel`: A mipmap level within  .
- `sourceOrigin`: Assign   to each dimension that’s not relevant to  . For example:
- `sourceSize`: If   uses a compressed pixel format, set   to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp   to the edge of the texture.
- `destinationTexture`: For a texture that uses a compressed pixel format, align the copy region ( ) to the pixel format’s block size.
- `destinationSlice`: A slice within  .
- `destinationLevel`: A mipmap level within  .
- `destinationOrigin`: Assign   to each dimension that’s not relevant to  . For example:

## See Also

- [func copy(from: any MTLTexture, to: any MTLTexture)](mtlblitcommandencoder/copy(from:to:).md)
  Encodes a command that copies data from one texture to another.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:to:destinationslice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to another texture’s slices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:))*