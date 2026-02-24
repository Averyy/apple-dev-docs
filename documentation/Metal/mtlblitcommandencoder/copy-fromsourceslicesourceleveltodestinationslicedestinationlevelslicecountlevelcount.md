# copy(from:sourceSlice:sourceLevel:to:destinationSlice:destinationLevel:sliceCount:levelCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies slices of a texture to another texture’s slices.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)
```

## Mentions

- [Copying data into or out of mipmaps](copying-data-into-or-out-of-mipmaps.md)

## Parameters

- `sourceTexture`: A texture the command copies data from.
- `sourceSlice`: A slice within `sourceTexture` the command uses as a starting point to copy data from. Set this to `0` if `sourceTexture` isn’t a texture array or a cube texture.
- `sourceLevel`: A mipmap level within `sourceTexture`.
- `destinationTexture`: Another texture the command copies the data to that has the same pixel format and sample count as `sourceTexture`.
- `destinationSlice`: A slice within `destinationTexture` the command uses as its starting point for coping data. Set this to `0` if `destinationTexture` isn’t a texture array or a cube texture.
- `destinationLevel`: A mipmap level within `destinationTexture` that has the same size as the source texture’s `sourceLevel` mipmap.
- `sliceCount`: The number of slices the command copies so that it satisfies these conditions: - The sum of `sourceLevel` and `sourceSlice` doesn’t exceed the number of slices in `sourceTexture`.
- The sum of `destinationLevel` and `destinationSlice` doesn’t exceed the number of slices in `destinationTexture`.
- `levelCount`: The number of mipmap levels the command copies so that it satisfies these conditions: - The sum of `levelCount` and `sourceLevel` doesn’t exceed the number of mipmap levels in `sourceTexture`.
- The sum of `levelCount` and `destinationLevel` doesn’t exceed the number of mipmap levels in `destinationTexture`.

## See Also

- [func copy(from: any MTLTexture, to: any MTLTexture)](mtlblitcommandencoder/copy(from:to:).md)
  Encodes a command that copies data from one texture to another.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a texture’s slice into another slice.
- [func copy(from: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, to: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](mtlblitcommandencoder/copy(from:sourceorigin:sourcedimensions:to:destinationorigin:destinationdimensions:).md)
  Encodes a command to copy data from a slice of one tensor into a slice of another tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:to:destinationslice:destinationlevel:slicecount:levelcount:))*