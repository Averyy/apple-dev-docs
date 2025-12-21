# copy(from:sourceOrigin:sourceDimensions:to:destinationOrigin:destinationDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy data from a slice of one tensor into a slice of another tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(from sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, to destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)
```

#### Discussion

This command applies reshapes if `sourceTensor` and `destinationTensor` are not aliasable.

## Parameters

- `sourceTensor`: A tensor instance that this command copies data from.
- `sourceOrigin`: An array of offsets, in elements, to the first element of the slice of   that this command copies data from.
- `sourceDimensions`: An array of sizes, in elements, of the slice   that this command copies data from.
- `destinationTensor`: A tensor instance that this command copies data to.
- `destinationOrigin`: An array of offsets, in elements, to the first element of the slice of   that this command copies data to.
- `destinationDimensions`: An array of sizes, in elements, of the slice of   that this command copies data to.

## See Also

- [func copy(from: any MTLTexture, to: any MTLTexture)](mtlblitcommandencoder/copy(from:to:).md)
  Encodes a command that copies data from one texture to another.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:to:destinationslice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to another texture’s slices.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a texture’s slice into another slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceorigin:sourcedimensions:to:destinationorigin:destinationdimensions:))*