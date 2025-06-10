# copy(from:sourceOrigin:sourceDimensions:to:destinationOrigin:destinationDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy data from a slice of one tensor into a slice of another tensor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceorigin:sourcedimensions:to:destinationorigin:destinationdimensions:))*