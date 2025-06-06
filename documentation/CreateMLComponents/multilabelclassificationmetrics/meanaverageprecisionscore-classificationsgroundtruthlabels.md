# meanAveragePrecisionScore(classifications:groundTruth:labels:)

**Framework**: Create ML Components  
**Kind**: method

Computes the mean average precision.

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
static func meanAveragePrecisionScore(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, labels: Set<Label>) -> Float
```

#### Return Value

The mean average precision.

#### Discussion

An average precision score summarizes the precision-recall curve for a label. The mean average precision is the mean of the average precision scores for all the classification labels.

## Parameters

- `classifications`: A sequence of multi-label classifications.
- `groundTruth`: A sequence of multi-label correct labels.
- `labels`: The set of labels to consider.

## See Also

- [static func meanAveragePrecisionScore(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(_:).md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, labels: Set<Label>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(_:labels:).md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(classifications:groundtruth:).md)
  Computes the mean average precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/meanaverageprecisionscore(classifications:groundtruth:labels:))*