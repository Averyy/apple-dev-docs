# applyBackward(batchSize:input:output:outputGradient:generatingInputGradient:generatingWeightsGradient:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer backward to generate input gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient weightsGradient: BNNSNDArrayDescriptor? = nil) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `inputGradient`: The descriptor of the input gradient.
- `weightsGradient`: The descriptor of the weights gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/reductionlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingweightsgradient:))*