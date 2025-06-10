# applyBackward(batchSize:inputA:inputB:inputC:output:outputGradient:generatingInputAGradient:generatingInputBGradient:generatingInputCGradient:generatingParameterGradients:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer backward to generate input gradients, where the first layer accepts three inputs.

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
func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient inputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient inputBGradient: BNNSNDArrayDescriptor, generatingInputCGradient inputCGradient: BNNSNDArrayDescriptor, generatingParameterGradients parameterGradients: [BNNSNDArrayDescriptor]) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `inputA`: The descriptor of the first input.
- `inputB`: The descriptor of the second input.
- `inputC`: The descriptor of the third input.
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `inputAGradient`: The descriptor of the input gradient.
- `inputBGradient`: The descriptor of the input gradient.
- `inputCGradient`: The descriptor of the input gradient.
- `parameterGradients`: An array that contains the parameter gradients.

## See Also

- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedparameterslayer/apply(batchsize:inputa:inputb:output:for:).md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedparameterslayer/apply(batchsize:inputa:inputb:inputc:output:for:).md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](bnns/fusedparameterslayer/applybackward(batchsize:inputa:inputb:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatingparametergradients:).md)
  Applies the layer backward to generate input gradients, where the first layer accepts two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedparameterslayer/applybackward(batchsize:inputa:inputb:inputc:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatinginputcgradient:generatingparametergradients:))*