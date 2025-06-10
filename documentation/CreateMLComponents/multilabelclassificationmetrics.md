# MultiLabelClassificationMetrics

**Framework**: Create ML Components  
**Kind**: struct

Multi-label classification metrics.

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
struct MultiLabelClassificationMetrics<Label> where Label : Hashable
```

## Topics

### Creating the distribution
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
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy](multilabelclassificationmetrics/thresholdselectionstrategy.md)
  A strategy for selecting a confidence threshold.
### Getting the properties
- [var confidenceThresholds: [Label : Float]](multilabelclassificationmetrics/confidencethresholds.md)
  A dictionary of label and confidence thresholds.
- [var exampleCount: Int](multilabelclassificationmetrics/examplecount.md)
  The number of examples used to compute the metrics.
- [var labels: Set<Label>](multilabelclassificationmetrics/labels.md)
  The classifier labels.
- [var meanAveragePrecision: Float](multilabelclassificationmetrics/meanaverageprecision.md)
  The mean average precision.
### Computing and scoring
- [func count(of: Label) -> Int](multilabelclassificationmetrics/count(of:).md)
  Returns the number of times a label appeared in the ground truth collection.
- [func f1Score(for: Label) -> Float](multilabelclassificationmetrics/f1score(for:).md)
  Computes the F1 score from predicted and ground truth values.
- [func falseNegativeCount(of: Label) -> Int](multilabelclassificationmetrics/falsenegativecount(of:).md)
  Returns the number of times a true label was not predicted.
- [func falsePositiveCount(of: Label) -> Int](multilabelclassificationmetrics/falsepositivecount(of:).md)
  Returns the number of times the predicted label did not match the true label.
- [func precisionScore(for: Label) -> Float](multilabelclassificationmetrics/precisionscore(for:).md)
  Computes the precision score for a class label.
- [func recallScore(for: Label) -> Float](multilabelclassificationmetrics/recallscore(for:).md)
  Computes the recall score for a class label.
- [func trueNegativeCount(of: Label) -> Int](multilabelclassificationmetrics/truenegativecount(of:).md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](multilabelclassificationmetrics/truepositivecount(of:).md)
  Returns the number of times the predicted label matched the true label.
### Updating the metrics
- [func add(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>)](multilabelclassificationmetrics/add(_:).md)
  Updates the metrics with more pairs of classifications and ground truth labels.
- [func add(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>)](multilabelclassificationmetrics/add(classifications:groundtruth:).md)
  Updates the metrics with more classifications and ground truth labels.
### Computing the precision
- [static func meanAveragePrecisionScore(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(_:).md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, labels: Set<Label>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(_:labels:).md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(classifications:groundtruth:).md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, labels: Set<Label>) -> Float](multilabelclassificationmetrics/meanaverageprecisionscore(classifications:groundtruth:labels:).md)
  Computes the mean average precision.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Classification](classification.md)
  An item in a classification result.
- [struct ClassificationDistribution](classificationdistribution.md)
  A classification distribution that contains a probability for each classification label.
- [struct ClassificationMetrics](classificationmetrics.md)
  Classification metrics.
- [func rootMeanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](rootmeansquarederror(_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func rootMeanSquaredError<T>(some Collection, some Collection) -> T](rootmeansquarederror(_:_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func maximumAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](maximumabsoluteerror(_:).md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func maximumAbsoluteError<T>(some Collection, some Collection) -> T](maximumabsoluteerror(_:_:).md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](meanabsoluteerror(_:).md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>(some Collection, some Collection) -> T](meanabsoluteerror(_:_:).md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T](meanabsolutepercentageerror(_:).md)
  Computes the mean absolute percentage error between predicted and ground truth values.
- [func meanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](meansquarederror(_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func meanSquaredError<T>(some Collection, some Collection) -> T](meansquarederror(_:_:).md)
  Computes the mean squared error between predicted and ground truth values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics)*