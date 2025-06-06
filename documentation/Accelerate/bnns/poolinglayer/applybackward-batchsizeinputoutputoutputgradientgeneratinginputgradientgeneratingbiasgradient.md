# applyBackward(batchSize:input:output:outputGradient:generatingInputGradient:generatingBiasGradient:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer backward to generate input gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor, generatingBiasGradient biasGradient: BNNSNDArrayDescriptor? = nil) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `inputGradient`: The descriptor of the input gradient.
- `biasGradient`: The descriptor of the bias gradient.

## See Also

- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/poolinglayer/apply(batchsize:input:output:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/poolinglayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingbiasgradient:))*