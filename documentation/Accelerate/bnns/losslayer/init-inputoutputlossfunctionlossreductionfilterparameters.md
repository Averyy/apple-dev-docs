# init(input:output:lossFunction:lossReduction:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new loss layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, lossFunction: BNNS.LossFunction, lossReduction: BNNS.LossReduction, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The input data type and output data type must be `float`. The output size must be `1`, unless the reduction is [`BNNS.LossReduction.none`](bnns/lossreduction/none.md).

 The input data type and output data type must be `float`. The output size must be `1`, unless the reduction is [`BNNS.LossReduction.none`](bnns/lossreduction/none.md).

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `lossFunction`: The function that’s used to compute the loss.
- `lossReduction`: The function that’s used to reduce the computed loss.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/losslayer/init(input:output:lossfunction:lossreduction:filterparameters:))*