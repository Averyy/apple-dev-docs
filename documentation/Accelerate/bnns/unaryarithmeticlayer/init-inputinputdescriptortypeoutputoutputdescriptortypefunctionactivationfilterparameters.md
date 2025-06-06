# init(input:inputDescriptorType:output:outputDescriptorType:function:activation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new unary arithmetic layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, inputDescriptorType: BNNS.DescriptorType, output: BNNSNDArrayDescriptor, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticUnaryFunction, activation: BNNS.ActivationFunction = .identity, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The input data type must be equal to the output data type. The input size must equal the output size or `1`. Arithmetic layers only support arrays with a data type of `float`, and a data layout of [`BNNS.DataLayout.vector`](bnns/datalayout/vector.md), [`BNNS.DataLayout.matrixRowMajor`](bnns/datalayout/matrixrowmajor.md), [`BNNS.DataLayout.matrixColumnMajor`](bnns/datalayout/matrixcolumnmajor.md), or [`BNNS.DataLayout.imageCHW`](bnns/datalayout/imagechw.md).

 The input data type must be equal to the output data type. The input size must equal the output size or `1`. Arithmetic layers only support arrays with a data type of `float`, and a data layout of [`BNNS.DataLayout.vector`](bnns/datalayout/vector.md), [`BNNS.DataLayout.matrixRowMajor`](bnns/datalayout/matrixrowmajor.md), [`BNNS.DataLayout.matrixColumnMajor`](bnns/datalayout/matrixcolumnmajor.md), or [`BNNS.DataLayout.imageCHW`](bnns/datalayout/imagechw.md).

## Parameters

- `input`: The descriptor of the input.
- `inputDescriptorType`: The descriptor type of the input.
- `output`: The descriptor of the output.
- `outputDescriptorType`: The descriptor type of the output.
- `function`: The arithmetic function.
- `activation`: The activation function that the layer applies to the output.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/unaryarithmeticlayer/init(input:inputdescriptortype:output:outputdescriptortype:function:activation:filterparameters:))*