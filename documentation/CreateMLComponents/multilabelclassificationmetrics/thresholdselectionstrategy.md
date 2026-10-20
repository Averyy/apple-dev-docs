# MultiLabelClassificationMetrics.ThresholdSelectionStrategy

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

A strategy for selecting a confidence threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum ThresholdSelectionStrategy
```

Available when `Label` conforms to `Hashable`.

## Topics

### Selection strategies
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.balancedPrecisionAndRecall](./thresholdselectionstrategy/balancedprecisionandrecall.md)
  A confidence threshold strategy that balances precision and recall equivalently.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.fixed(_:)](./thresholdselectionstrategy/fixed%28_%29.md)
  A confidence threshold strategy that uses the specified thresholds for each label.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.precision(_:minimumRecall:)](./thresholdselectionstrategy/precision%28_,minimumrecall%29.md)
  A confidence threshold strategy for a specific precision that has at least a minimum recall value.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.recall(_:minimumPrecision:)](./thresholdselectionstrategy/recall%28_,minimumprecision%29.md)
  A confidence threshold strategy for a recall precision that has at least a minimum precision value.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating the distribution
- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](./init%28_,strategy%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](./init%28_,strategy,labels%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](./init%28classifications,groundtruth,strategy%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](./init%28classifications,groundtruth,strategy,labels%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(confidenceThresholds: [Label : Float])](./init%28confidencethresholds%29.md)
  Creates empty multi-label classification metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/thresholdselectionstrategy)*