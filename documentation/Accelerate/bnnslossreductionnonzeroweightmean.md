# BNNSLossReductionNonZeroWeightMean

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

Sums the loss of all samples in the batch and divides by the number of non-zero weights.

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
var BNNSLossReductionNonZeroWeightMean: BNNSLossReductionFunction { get }
```

```c
BNNSLossReductionNonZeroWeightMean
```

#### Discussion

[`BNNSLossReductionNonZeroWeightMean`](./bnnslossreductionnonzeroweightmean.md) sums the loss of all samples in the batch and divides by number of non-zero weights.

Non-zero weighted mean reduction returns 0 in case all weights are zero.

## See Also

### Reduction Functions
- [var rawValue: UInt32](./bnnslossreductionfunction/rawvalue.md)
- [init(UInt32)](./bnnslossreductionfunction/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnslossreductionfunction/init%28rawvalue%29.md)
- [var BNNSLossReductionMean: BNNSLossReductionFunction](./bnnslossreductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [var BNNSLossReductionSum: BNNSLossReductionFunction](./bnnslossreductionsum.md)
  Sums the loss of all samples in the batch.
- [var BNNSLossReductionWeightedMean: BNNSLossReductionFunction](./bnnslossreductionweightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [var BNNSLossReductionNone: BNNSLossReductionFunction](./bnnslossreductionnone.md)
  Returns the loss without any reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossreductionnonzeroweightmean)*