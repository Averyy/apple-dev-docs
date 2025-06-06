# init(_:)

**Framework**: Accelerate  
**Kind**: init

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(_ rawValue: UInt32)
```

## See Also

- [var rawValue: UInt32](bnnslossreductionfunction/rawvalue.md)
- [init(rawValue: UInt32)](bnnslossreductionfunction/init(rawvalue:).md)
- [var BNNSLossReductionMean: BNNSLossReductionFunction](bnnslossreductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [var BNNSLossReductionNonZeroWeightMean: BNNSLossReductionFunction](bnnslossreductionnonzeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.
- [var BNNSLossReductionSum: BNNSLossReductionFunction](bnnslossreductionsum.md)
  Sums the loss of all samples in the batch.
- [var BNNSLossReductionWeightedMean: BNNSLossReductionFunction](bnnslossreductionweightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [var BNNSLossReductionNone: BNNSLossReductionFunction](bnnslossreductionnone.md)
  Returns the loss without any reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossreductionfunction/init(_:))*