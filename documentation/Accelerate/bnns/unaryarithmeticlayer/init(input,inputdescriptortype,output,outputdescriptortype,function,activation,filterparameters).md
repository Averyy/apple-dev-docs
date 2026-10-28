# init(input:inputDescriptorType:output:outputDescriptorType:function:activation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new unary arithmetic layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, inputDescriptorType: BNNS.DescriptorType, output: BNNSNDArrayDescriptor, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticUnaryFunction, activation: BNNS.ActivationFunction = .identity, filterParameters: BNNSFilterParameters? = nil)
```

## Discussion

> ❗ **Important**:  The input data type must be equal to the output data type. The input size must equal the output size or `1`. Arithmetic layers only support arrays with a data type of `float`, and a data layout of [`BNNS.DataLayout.vector`](../datalayout/vector.md), [`BNNS.DataLayout.matrixRowMajor`](../datalayout/matrixrowmajor.md), [`BNNS.DataLayout.matrixColumnMajor`](../datalayout/matrixcolumnmajor.md), or [`BNNS.DataLayout.imageCHW`](../datalayout/imagechw.md).

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