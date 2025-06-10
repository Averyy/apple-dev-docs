# init(function:i_desc:o_desc:reduction:huber_delta:)

**Framework**: Accelerate  
**Kind**: init

Returns a new Huber loss layer parameters structure from the specified parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(function: BNNSLossFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, reduction: BNNSLossReductionFunction, huber_delta: Float)
```

#### Discussion

> ❗ **Important**:  The input data type and output data type must be `float`. The output size must be `1`, unless the reduction is [`BNNS.LossReduction.none`](bnns/lossreduction/none.md).

## Parameters

- `function`: The function that’s used to compute loss.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `reduction`: The function that’s used to reduce the computed loss.
- `huber_delta`: The boundary value that defines where Huber loss returns mean absolute error or mean square error.

## See Also

- [init()](bnnslayerparameterslosshuber/init.md)
  Returns a new Huber loss layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslosshuber/init(function:i_desc:o_desc:reduction:huber_delta:))*