# applyBackward(batchSize:input:output:outputGradient:generatingWeightsGradient:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer backward to generate input gradients.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient weightsGradient: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `weightsGradient`: The descriptor of the input gradient.

## See Also

- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/embeddinglayer/apply(batchsize:input:output:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/embeddinglayer/applybackward(batchsize:input:output:outputgradient:generatingweightsgradient:))*