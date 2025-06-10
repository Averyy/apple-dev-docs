# copy(sourceTensor:sourceOrigin:sourceDimensions:destinationTensor:destinationOrigin:destinationDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy data from a tensor instance into another.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)
```

#### Discussion

If the `sourceTensor` and `destinationTensor` instances are not aliasable, this command applies the correct reshapes to enable this operation.

## Parameters

- `sourceTensor`: An   instance the command copies data from.
- `destinationTensor`: An   instance the command copies data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:))*