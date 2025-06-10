# init(i_desc:o_desc:w_desc:reduce_func:epsilon:)

**Framework**: Accelerate  
**Kind**: init

Returns a structure containing the parameters of a reduction layer from the specified parameters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, reduce_func: BNNSReduceFunction, epsilon: Float)
```

#### Discussion

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions, and equal to the number of weights dimensions. The reduction layer only supports `float`, with the exception of [`BNNSReduceFunctionLogicalOr`](bnnsreducefunctionlogicalor.md) and [`BNNSReduceFunctionLogicalAnd`](bnnsreducefunctionlogicaland.md) that support `float` and `BNNSDataTypeBoolean`.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `w_desc`: The descriptor of the weights.
- `reduce_func`: The variable that specifies the reduction function.
- `epsilon`: A value that the operation adds to each element when computing the sum of logarithms.

## See Also

- [init()](bnnslayerparametersreduction/init.md)
  Returns a structure containing the parameters of a reduction layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersreduction/init(i_desc:o_desc:w_desc:reduce_func:epsilon:))*