# BNNSLossReductionMean

**Framework**: Accelerate  
**Kind**: var

Sums the loss of all samples in the batch and divides by the number of samples.

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
var BNNSLossReductionMean: BNNSLossReductionFunction { get }
```

#### Discussion

[`BNNSLossReductionMean`](bnnslossreductionmean.md) sums the loss of all samples in the batch and divides by number of samples.

## See Also

- [var rawValue: UInt32](bnnslossreductionfunction/rawvalue.md)
- [init(UInt32)](bnnslossreductionfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnslossreductionfunction/init(rawvalue:).md)
- [var BNNSLossReductionNonZeroWeightMean: BNNSLossReductionFunction](bnnslossreductionnonzeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.
- [var BNNSLossReductionSum: BNNSLossReductionFunction](bnnslossreductionsum.md)
  Sums the loss of all samples in the batch.
- [var BNNSLossReductionWeightedMean: BNNSLossReductionFunction](bnnslossreductionweightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [var BNNSLossReductionNone: BNNSLossReductionFunction](bnnslossreductionnone.md)
  Returns the loss without any reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossreductionmean)*