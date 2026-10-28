# copy(sourceTensor:sourceOrigin:sourceDimensions:destinationTensor:destinationOrigin:destinationDimensions:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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
func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)
```

```objc
- (void) copyFromTensor:(id<MTLTensor>) sourceTensor sourceOrigin:(MTLTensorExtents *) sourceOrigin sourceDimensions:(MTLTensorExtents *) sourceDimensions toTensor:(id<MTLTensor>) destinationTensor destinationOrigin:(MTLTensorExtents *) destinationOrigin destinationDimensions:(MTLTensorExtents *) destinationDimensions;
```

## Discussion

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

### Encoding texture copy commands
- [func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](./copy%28sourcetexture,destinationtexture%29.md)
  Encodes a command that copies data from a texture to another.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)](./copy%28sourcetexture,sourceslice,sourcelevel,destinationtexture,destinationslice,destinationlevel,slicecount,levelcount%29.md)
  Encodes a command that copies slices of a texture to slices of another texture.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](./copy%28sourcetexture,sourceslice,sourcelevel,sourceorigin,sourcesize,destinationtexture,destinationslice,destinationlevel,destinationorigin%29.md)
  Encodes a command that copies image data from a slice of a texture into a slice of another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:))*