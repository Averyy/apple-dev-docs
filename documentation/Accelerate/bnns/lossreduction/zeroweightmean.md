# BNNS.LossReduction.zeroWeightMean

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

Sums the loss of all samples in the batch and divides by the number of non-zero weights.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
case zeroWeightMean
```

## See Also

### Loss Reduction Functions
- [BNNS.LossReduction.none](./none.md)
  Returns the loss without any reduction.
- [BNNS.LossReduction.reductionMean](./reductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [BNNS.LossReduction.sum](./sum.md)
  Sums the loss of all samples in the batch.
- [BNNS.LossReduction.weightedMean](./weightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossreduction/zeroweightmean)*