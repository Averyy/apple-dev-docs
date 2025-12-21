# copy(sourceTensor:sourceOrigin:sourceDimensions:destinationTensor:destinationOrigin:destinationDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy data from a tensor instance into another.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)
```

#### Discussion

If the `sourceTensor` and `destinationTensor` instances are not aliasable, this command applies the correct reshapes to enable this operation.

## Parameters

- `sourceTensor`: An   instance the command copies data from.
- `destinationTensor`: An   instance the command copies data to.

## See Also

- [func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mtl4computecommandencoder/copy(sourcetexture:destinationtexture:).md)
  Encodes a command that copies data from a texture to another.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to slices of another texture.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a slice of a texture into a slice of another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:))*