# init(function:input:output:weights:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new reduction layer.

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
convenience init?(function reductionFunction: BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions, and equal to the number of weights dimensions. The reduction layer only supports `float`, with the exception of [`BNNSReduceFunctionLogicalOr`](bnnsreducefunctionlogicalor.md) and [`BNNSReduceFunctionLogicalAnd`](bnnsreducefunctionlogicaland.md) that support `float` and `BNNSDataTypeBoolean`.

## Parameters

- `reductionFunction`: The variable that specifies the reduction function.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `weights`: The descriptor of the weights.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/reductionlayer/init(function:input:output:weights:filterparameters:))*