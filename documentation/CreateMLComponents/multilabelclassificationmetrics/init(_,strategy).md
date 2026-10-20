# init(_:strategy:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

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
init(_ pairs: some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws
```

## Parameters

- `pairs`: A sequence of classifications and true label pairs.
- `strategy`: A label confidence threshold selection strategy.

## See Also

### Creating the distribution
- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](./init%28_,strategy,labels%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](./init%28classifications,groundtruth,strategy%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](./init%28classifications,groundtruth,strategy,labels%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(confidenceThresholds: [Label : Float])](./init%28confidencethresholds%29.md)
  Creates empty multi-label classification metrics.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy](./thresholdselectionstrategy.md)
  A strategy for selecting a confidence threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/init(_:strategy:))*