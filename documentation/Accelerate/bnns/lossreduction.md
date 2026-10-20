# BNNS.LossReduction

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

An enumeration that describes loss reduction functions.

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
enum LossReduction
```

## Topics

### Loss Reduction Functions
- [BNNS.LossReduction.none](./lossreduction/none.md)
  Returns the loss without any reduction.
- [BNNS.LossReduction.reductionMean](./lossreduction/reductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [BNNS.LossReduction.sum](./lossreduction/sum.md)
  Sums the loss of all samples in the batch.
- [BNNS.LossReduction.weightedMean](./lossreduction/weightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [BNNS.LossReduction.zeroWeightMean](./lossreduction/zeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.
### Instance Properties
- [var bnnsLossReductionFunction: BNNSLossReductionFunction](./lossreduction/bnnslossreductionfunction.md)
  The underlying loss reduction function structure.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossreduction)*