# applyBackward(batchSize:inputA:inputB:output:outputGradient:generatingInputAGradient:generatingInputBGradient:)

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
func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient inputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient inputBGradient: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `inputA`: The descriptor of the first input.
- `inputB`: The descriptor of the second input.
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `inputAGradient`: The descriptor of the first input gradient.
- `inputBGradient`: The descriptor of the second input gradient.

## See Also

- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/binaryarithmeticlayer/apply(batchsize:inputa:inputb:output:).md)
  Applies the layer to a set of input array descriptors, writing the result to a set of output array descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/binaryarithmeticlayer/applybackward(batchsize:inputa:inputb:output:outputgradient:generatinginputagradient:generatinginputbgradient:))*