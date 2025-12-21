# apply(batchSize:inputA:inputB:inputC:output:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input array descriptors, writing the result to a set of output array descriptors.

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
func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `inputA`: The descriptor of the first input.
- `inputB`: The descriptor of the second input.
- `inputC`: The descriptor of the third input.
- `output`: The descriptor of the output.

## See Also

- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingInputCGradient: BNNSNDArrayDescriptor) throws](bnns/ternaryarithmeticlayer/applybackward(batchsize:inputa:inputb:inputc:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatinginputcgradient:).md)
  Applies the layer backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/ternaryarithmeticlayer/apply(batchsize:inputa:inputb:inputc:output:))*