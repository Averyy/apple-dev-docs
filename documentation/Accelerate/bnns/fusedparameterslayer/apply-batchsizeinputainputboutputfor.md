# apply(batchSize:inputA:inputB:output:for:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for learningPhase: BNNS.LearningPhase) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `inputA`: The descriptor of the first input.
- `inputB`: The descriptor of the second input.
- `output`: The descriptor of the output.
- `learningPhase`: An enumeration that specifies whether the function call context is training or inference.

## See Also

- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedparameterslayer/apply(batchsize:inputa:inputb:inputc:output:for:).md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](bnns/fusedparameterslayer/applybackward(batchsize:inputa:inputb:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatingparametergradients:).md)
  Applies the layer backward to generate input gradients, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingInputCGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](bnns/fusedparameterslayer/applybackward(batchsize:inputa:inputb:inputc:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatinginputcgradient:generatingparametergradients:).md)
  Applies the layer backward to generate input gradients, where the first layer accepts three inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedparameterslayer/apply(batchsize:inputa:inputb:output:for:))*