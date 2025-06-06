# BNNS.LossReduction.none

**Framework**: Accelerate  
**Kind**: case

Returns the loss without any reduction.

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
case none
```

## See Also

- [BNNS.LossReduction.reductionMean](bnns/lossreduction/reductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [BNNS.LossReduction.sum](bnns/lossreduction/sum.md)
  Sums the loss of all samples in the batch.
- [BNNS.LossReduction.weightedMean](bnns/lossreduction/weightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [BNNS.LossReduction.zeroWeightMean](bnns/lossreduction/zeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossreduction/none)*