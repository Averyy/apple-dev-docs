# BNNS.LossReduction.sum

**Framework**: Accelerate  
**Kind**: case

Sums the loss of all samples in the batch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
case sum
```

## See Also

- [BNNS.LossReduction.none](bnns/lossreduction/none.md)
  Returns the loss without any reduction.
- [BNNS.LossReduction.reductionMean](bnns/lossreduction/reductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [BNNS.LossReduction.weightedMean](bnns/lossreduction/weightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [BNNS.LossReduction.zeroWeightMean](bnns/lossreduction/zeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossreduction/sum)*