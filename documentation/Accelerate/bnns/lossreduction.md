# BNNS.LossReduction

**Framework**: Accelerate  
**Kind**: enum

An enumeration that describes loss reduction functions.

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
enum LossReduction
```

## Topics

### Loss Reduction Functions
- [BNNS.LossReduction.none](bnns/lossreduction/none.md)
  Returns the loss without any reduction.
- [BNNS.LossReduction.reductionMean](bnns/lossreduction/reductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [BNNS.LossReduction.sum](bnns/lossreduction/sum.md)
  Sums the loss of all samples in the batch.
- [BNNS.LossReduction.weightedMean](bnns/lossreduction/weightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [BNNS.LossReduction.zeroWeightMean](bnns/lossreduction/zeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.
### Instance Properties
- [var bnnsLossReductionFunction: BNNSLossReductionFunction](bnns/lossreduction/bnnslossreductionfunction.md)
  The underlying loss reduction function structure.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossreduction)*