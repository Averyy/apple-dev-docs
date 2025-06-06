# BNNSLossReductionNone

**Framework**: Accelerate  
**Kind**: var

Returns the loss without any reduction.

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
var BNNSLossReductionNone: BNNSLossReductionFunction { get }
```

#### Discussion

## See Also

- [var rawValue: UInt32](bnnslossreductionfunction/rawvalue.md)
- [init(UInt32)](bnnslossreductionfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnslossreductionfunction/init(rawvalue:).md)
- [var BNNSLossReductionMean: BNNSLossReductionFunction](bnnslossreductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [var BNNSLossReductionNonZeroWeightMean: BNNSLossReductionFunction](bnnslossreductionnonzeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.
- [var BNNSLossReductionSum: BNNSLossReductionFunction](bnnslossreductionsum.md)
  Sums the loss of all samples in the batch.
- [var BNNSLossReductionWeightedMean: BNNSLossReductionFunction](bnnslossreductionweightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossreductionnone)*