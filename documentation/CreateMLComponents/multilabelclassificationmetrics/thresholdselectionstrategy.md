# MultiLabelClassificationMetrics.ThresholdSelectionStrategy

**Framework**: Create ML Components  
**Kind**: enum

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

## Topics

### Selection strategies
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.balancedPrecisionAndRecall](multilabelclassificationmetrics/thresholdselectionstrategy/balancedprecisionandrecall.md)
  A confidence threshold strategy that balances precision and recall equivalently.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.fixed(_:)](multilabelclassificationmetrics/thresholdselectionstrategy/fixed(_:).md)
  A confidence threshold strategy that uses the specified thresholds for each label.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.precision(_:minimumRecall:)](multilabelclassificationmetrics/thresholdselectionstrategy/precision(_:minimumrecall:).md)
  A confidence threshold strategy for a specific precision that has at least a minimum recall value.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.recall(_:minimumPrecision:)](multilabelclassificationmetrics/thresholdselectionstrategy/recall(_:minimumprecision:).md)
  A confidence threshold strategy for a recall precision that has at least a minimum precision value.
### Operators
- [static func == (MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) -> Bool](multilabelclassificationmetrics/thresholdselectionstrategy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](multilabelclassificationmetrics/thresholdselectionstrategy/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](multilabelclassificationmetrics/thresholdselectionstrategy/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Decodable Implementations](multilabelclassificationmetrics/thresholdselectionstrategy/decodable-implementations.md)
- [Encodable Implementations](multilabelclassificationmetrics/thresholdselectionstrategy/encodable-implementations.md)
- [Equatable Implementations](multilabelclassificationmetrics/thresholdselectionstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](multilabelclassificationmetrics/init(_:strategy:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](multilabelclassificationmetrics/init(_:strategy:labels:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](multilabelclassificationmetrics/init(classifications:groundtruth:strategy:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](multilabelclassificationmetrics/init(classifications:groundtruth:strategy:labels:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(confidenceThresholds: [Label : Float])](multilabelclassificationmetrics/init(confidencethresholds:).md)
  Creates empty multi-label classification metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/thresholdselectionstrategy)*