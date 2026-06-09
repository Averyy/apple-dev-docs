# copy(from:sourceOrigin:sourceDimensions:to:destinationOrigin:destinationDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.

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

If `sourceTensor` and `destinationTensor` are not aliasable, this command applies a reshape operation.

Ensure the first dimension of `sourceOrigin`, `sourceDimensions`, `destinationOrigin`, and `destinationDimensions` is byte aligned.

## Parameters

- `sourceTensor`: A tensor instance the method copies data from.
- `sourceOrigin`: An array of per-dimension offsets that together locate the first element to copy in `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `sourceDimensions`: An array of per-dimension sizes that together define the extent of the slice to copy from `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sourceOrigin`.
- `destinationTensor`: A tensor instance the method copies data to.
- `destinationOrigin`: An array of per-dimension offsets that together locate the first element to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `destinationDimensions`: An array of per-dimension sizes that together define the extent of the slice to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `destinationOrigin`.

## See Also

- [func copy(from: any MTLTexture, to: any MTLTexture)](mtlblitcommandencoder/copy(from:to:).md)
  Encodes a command that copies data from one texture to another.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:to:destinationslice:destinationlevel:slicecount:levelcount:).md)
  Encodes a command that copies slices of a texture to another texture’s slices.
- [func copy(from: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a texture’s slice into another slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceorigin:sourcedimensions:to:destinationorigin:destinationdimensions:))*