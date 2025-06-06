# init(_:strategy:labels:)

**Framework**: Create ML Components  
**Kind**: init

Creates multi-label classification metrics for classifications and ground truth labels.

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
init(_ pairs: some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws
```

## Parameters

- `pairs`: A sequence of pairs with a classification distribution and a set of labels.
- `strategy`: A label confidence threshold selection strategy.
- `labels`: The set of labels to consider.

## See Also

- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](multilabelclassificationmetrics/init(_:strategy:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](multilabelclassificationmetrics/init(classifications:groundtruth:strategy:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](multilabelclassificationmetrics/init(classifications:groundtruth:strategy:labels:).md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(confidenceThresholds: [Label : Float])](multilabelclassificationmetrics/init(confidencethresholds:).md)
  Creates empty multi-label classification metrics.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy](multilabelclassificationmetrics/thresholdselectionstrategy.md)
  A strategy for selecting a confidence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/init(_:strategy:labels:))*