# init(in:in_type:out:out_type:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new arithmetic structure that takes a single input from the specified parameters.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
init(in: BNNSNDArrayDescriptor, in_type: BNNSDescriptorType, out: BNNSNDArrayDescriptor, out_type: BNNSDescriptorType)
```

## Discussion

> ❗ **Important**:  The input data type must be equal to the output data type. The input size must equal the output size or `1`. Arithmetic layers only support arrays with a data type of `float`, and a data layout of [`BNNS.DataLayout.vector`](../bnns/datalayout/vector.md), [`BNNS.DataLayout.matrixRowMajor`](../bnns/datalayout/matrixrowmajor.md), [`BNNS.DataLayout.matrixColumnMajor`](../bnns/datalayout/matrixcolumnmajor.md), or [`BNNS.DataLayout.imageCHW`](../bnns/datalayout/imagechw.md).

## Parameters

- `in`: The descriptor of the input.
- `in_type`: The descriptor type of the input.
- `out`: The descriptor of the output.
- `out_type`: The descriptor type of the output.

## See Also

### Creating an Arithmetic Structure
- [init()](./init%28%29.md)
  Returns a new arithmetic structure that takes a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsarithmeticunary/init(in:in_type:out:out_type:))*