# init(function:i_desc:o_desc:reduction:label_smooth:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new softmax cross entropy loss layer parameters structure from the specified parameters.

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
init(function: BNNSLossFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, reduction: BNNSLossReductionFunction, label_smooth: Float)
```

#### Discussion

> ❗ **Important**:  The input data type and output data type must be `float`. The output size must be `1`, unless the reduction is [`BNNS.LossReduction.none`](../bnns/lossreduction/none.md).

## Parameters

- `function`: The function that’s used to compute loss.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `reduction`: The function that’s used to reduce the computed loss.
- `label_smooth`: A value that defines the smoothing that the loss function applies to the labels.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new softmax cross entropy loss layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslosssoftmaxcrossentropy/init(function:i_desc:o_desc:reduction:label_smooth:))*