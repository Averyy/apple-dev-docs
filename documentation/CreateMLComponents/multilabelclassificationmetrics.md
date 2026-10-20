# MultiLabelClassificationMetrics

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](./multilabelclassificationmetrics/init%28_,strategy%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](./multilabelclassificationmetrics/init%28_,strategy,labels%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy) throws](./multilabelclassificationmetrics/init%28classifications,groundtruth,strategy%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, strategy: MultiLabelClassificationMetrics<Label>.ThresholdSelectionStrategy, labels: Set<Label>) throws](./multilabelclassificationmetrics/init%28classifications,groundtruth,strategy,labels%29.md)
  Creates multi-label classification metrics for classifications and ground truth labels.
- [init(confidenceThresholds: [Label : Float])](./multilabelclassificationmetrics/init%28confidencethresholds%29.md)
  Creates empty multi-label classification metrics.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy](./multilabelclassificationmetrics/thresholdselectionstrategy.md)
  A strategy for selecting a confidence threshold.
### Getting the properties
- [var confidenceThresholds: [Label : Float]](./multilabelclassificationmetrics/confidencethresholds.md)
  A dictionary of label and confidence thresholds.
- [var exampleCount: Int](./multilabelclassificationmetrics/examplecount.md)
  The number of examples used to compute the metrics.
- [var labels: Set<Label>](./multilabelclassificationmetrics/labels.md)
  The classifier labels.
- [var meanAveragePrecision: Float](./multilabelclassificationmetrics/meanaverageprecision.md)
  The mean average precision.
### Computing and scoring
- [func count(of: Label) -> Int](./multilabelclassificationmetrics/count%28of%29.md)
  Returns the number of times a label appeared in the ground truth collection.
- [func f1Score(for: Label) -> Float](./multilabelclassificationmetrics/f1score%28for%29.md)
  Computes the F1 score from predicted and ground truth values.
- [func falseNegativeCount(of: Label) -> Int](./multilabelclassificationmetrics/falsenegativecount%28of%29.md)
  Returns the number of times a true label was not predicted.
- [func falsePositiveCount(of: Label) -> Int](./multilabelclassificationmetrics/falsepositivecount%28of%29.md)
  Returns the number of times the predicted label did not match the true label.
- [func precisionScore(for: Label) -> Float](./multilabelclassificationmetrics/precisionscore%28for%29.md)
  Computes the precision score for a class label.
- [func recallScore(for: Label) -> Float](./multilabelclassificationmetrics/recallscore%28for%29.md)
  Computes the recall score for a class label.
- [func trueNegativeCount(of: Label) -> Int](./multilabelclassificationmetrics/truenegativecount%28of%29.md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](./multilabelclassificationmetrics/truepositivecount%28of%29.md)
  Returns the number of times the predicted label matched the true label.
### Updating the metrics
- [func add(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>)](./multilabelclassificationmetrics/add%28_%29.md)
  Updates the metrics with more pairs of classifications and ground truth labels.
- [func add(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>)](./multilabelclassificationmetrics/add%28classifications,groundtruth%29.md)
  Updates the metrics with more classifications and ground truth labels.
### Computing the precision
- [static func meanAveragePrecisionScore(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>) -> Float](./multilabelclassificationmetrics/meanaverageprecisionscore%28_%29.md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>, labels: Set<Label>) -> Float](./multilabelclassificationmetrics/meanaverageprecisionscore%28_,labels%29.md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>) -> Float](./multilabelclassificationmetrics/meanaverageprecisionscore%28classifications,groundtruth%29.md)
  Computes the mean average precision.
- [static func meanAveragePrecisionScore(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>, labels: Set<Label>) -> Float](./multilabelclassificationmetrics/meanaverageprecisionscore%28classifications,groundtruth,labels%29.md)
  Computes the mean average precision.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Metrics
- [struct Classification](./classification.md)
  An item in a classification result.
- [struct ClassificationDistribution](./classificationdistribution.md)
  A classification distribution that contains a probability for each classification label.
- [struct ClassificationMetrics](./classificationmetrics.md)
  Classification metrics.
- [func rootMeanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](./rootmeansquarederror%28_%29.md)
  Computes the root mean squared error between predicted and ground truth values.
- [func rootMeanSquaredError<T>(some Collection, some Collection) -> T](./rootmeansquarederror%28_,_%29.md)
  Computes the root mean squared error between predicted and ground truth values.
- [func maximumAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](./maximumabsoluteerror%28_%29.md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func maximumAbsoluteError<T>(some Collection, some Collection) -> T](./maximumabsoluteerror%28_,_%29.md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](./meanabsoluteerror%28_%29.md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>(some Collection, some Collection) -> T](./meanabsoluteerror%28_,_%29.md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T](./meanabsolutepercentageerror%28_%29.md)
  Computes the mean absolute percentage error between predicted and ground truth values.
- [func meanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](./meansquarederror%28_%29.md)
  Computes the root mean squared error between predicted and ground truth values.
- [func meanSquaredError<T>(some Collection, some Collection) -> T](./meansquarederror%28_,_%29.md)
  Computes the mean squared error between predicted and ground truth values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics)*