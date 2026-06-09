# copy(sourceTensor:sourceOrigin:sourceDimensions:sourcePlane:destinationTensor:destinationOrigin:destinationDimensions:destinationPlane:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy data from a slice of a plane of a tensor into a slice of a plane of another tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, sourcePlane: MTLTensorPlaneType, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents, destinationPlane: MTLTensorPlaneType)
```

#### Discussion

If `sourceTensor` and `destinationTensor` are not aliasable, this command applies a reshape operation. For auxiliary planes, specify origin and dimensions in plane coordinates by applying the corresponding auxiliary plane’s block factors.

Ensure the first dimension of `sourceOrigin`, `sourceDimensions`, `destinationOrigin`, and `destinationDimensions` is byte aligned.

## Parameters

- `sourceTensor`: A tensor instance the method copies data from.
- `sourceOrigin`: An array of per-dimension offsets that together locate the first element to copy in `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `sourceDimensions`: An array of per-dimension sizes that together define the extent of the slice to copy from `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sourceOrigin`.
- `sourcePlane`: The plane the method copies data from.
- `destinationTensor`: A tensor instance the method copies data to.
- `destinationOrigin`: An array of per-dimension offsets that together locate the first element to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `destinationDimensions`: An array of per-dimension sizes that together define the extent of the slice to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `destinationOrigin`.
- `destinationPlane`: The plane the method copies data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:sourceplane:destinationtensor:destinationorigin:destinationdimensions:destinationplane:))*