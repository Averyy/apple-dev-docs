# copy(from:to:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that copies data from one texture to another.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceTexture: any MTLTexture, to destinationTexture: any MTLTexture)
```

```objc
- (void) copyFromTexture:(id<MTLTexture>) sourceTexture toTexture:(id<MTLTexture>) destinationTexture;
```

## Mentions

- [Copying data into or out of mipmaps](../copying-data-into-or-out-of-mipmaps.md)

#### Discussion

The textures can be different sizes as long as the larger texture has a mipmap level that’s the same size as the smaller texture’s level `0` mipmap.

The command copies all identical mipmap sizes. If both textures are arrays, the command copies as many texture slices (array elements) as possible.

## Parameters

- `sourceTexture`: A texture the command copies data from.
- `destinationTexture`: Another texture the command copies the data to that has the same pixel format and sample count as `sourceTexture`.

## See Also

### Copying texture data to another texture
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](./copy%28from,sourceslice,sourcelevel,to,destinationslice,destinationlevel,slicecount,levelcount%29.md)
  Encodes a command that copies slices of a texture to another texture’s slices.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](./copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationslice,destinationlevel,destinationorigin%29.md)
  Encodes a command that copies image data from a texture’s slice into another slice.
- [func copy(from: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, to: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](./copy%28from,sourceorigin,sourcedimensions,to,destinationorigin,destinationdimensions%29.md)
  Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:to:))*