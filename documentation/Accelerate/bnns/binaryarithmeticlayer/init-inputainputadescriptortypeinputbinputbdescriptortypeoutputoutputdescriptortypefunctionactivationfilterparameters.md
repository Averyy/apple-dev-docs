# init(inputA:inputADescriptorType:inputB:inputBDescriptorType:output:outputDescriptorType:function:activation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new binary arithmetic layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
convenience init?(inputA: BNNSNDArrayDescriptor, inputADescriptorType: BNNS.DescriptorType, inputB: BNNSNDArrayDescriptor, inputBDescriptorType: BNNS.DescriptorType, output: BNNSNDArrayDescriptor, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticBinaryFunction, activation: BNNS.ActivationFunction = .identity, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The data types of the inputs must be equal to the output data type. The size of the inputs must either 1, or the maximum size of either input and the output. Arithmetic layers only support arrays with a data type of `float`, and a data layout of [`BNNS.DataLayout.vector`](bnns/datalayout/vector.md), [`BNNS.DataLayout.matrixRowMajor`](bnns/datalayout/matrixrowmajor.md), [`BNNS.DataLayout.matrixColumnMajor`](bnns/datalayout/matrixcolumnmajor.md), or [`BNNS.DataLayout.imageCHW`](bnns/datalayout/imagechw.md).

 The data types of the inputs must be equal to the output data type. The size of the inputs must either 1, or the maximum size of either input and the output. Arithmetic layers only support arrays with a data type of `float`, and a data layout of [`BNNS.DataLayout.vector`](bnns/datalayout/vector.md), [`BNNS.DataLayout.matrixRowMajor`](bnns/datalayout/matrixrowmajor.md), [`BNNS.DataLayout.matrixColumnMajor`](bnns/datalayout/matrixcolumnmajor.md), or [`BNNS.DataLayout.imageCHW`](bnns/datalayout/imagechw.md).

## Parameters

- `inputA`: The descriptor of the first input.
- `inputADescriptorType`: The descriptor type of the first input.
- `inputB`: The descriptor of the second input.
- `inputBDescriptorType`: The descriptor type of the second input.
- `output`: The descriptor of the output.
- `outputDescriptorType`: The descriptor type of the output.
- `function`: The arithmetic function.
- `activation`: The activation function that the layer applies to the output.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/binaryarithmeticlayer/init(inputa:inputadescriptortype:inputb:inputbdescriptortype:output:outputdescriptortype:function:activation:filterparameters:))*