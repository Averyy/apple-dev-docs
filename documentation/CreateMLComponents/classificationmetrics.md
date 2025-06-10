# ClassificationMetrics

**Framework**: Create ML Components  
**Kind**: struct

Classification metrics.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct ClassificationMetrics<Label> where Label : Hashable
```

## Topics

### Creating the distribution
- [init<Predicted, Correct>(Predicted, Correct)](classificationmetrics/init(_:_:).md)
  Creates classification metrics for predicted and ground truth labels.
- [init()](classificationmetrics/init.md)
  Creates empty classification metrics.
- [init(some Sequence<(predicted: Label, label: Label)>)](classificationmetrics/init(_:)-5afx5.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<S, Inner>(S) async throws](classificationmetrics/init(_:)-7nms4.md)
  Creates classification metrics from a temporal sequence of annotated classifications.
- [init(some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)](classificationmetrics/init(_:labels:).md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](classificationmetrics/init(predicted:groundtruth:labels:).md)
  Creates classification metrics for predicted and ground truth labels.
### Getting the properties
- [var accuracy: Double](classificationmetrics/accuracy.md)
  The number of correctly classified examples out of the total number of examples.
- [var exampleCount: Int](classificationmetrics/examplecount.md)
  The number of examples used to compute the metrics.
- [var labels: Set<Label>](classificationmetrics/labels.md)
  The set of labels.
- [var restrictToKnownLabels: Bool](classificationmetrics/restricttoknownlabels.md)
  A Boolean value indicating whether to restrict metrics to labels in the labels set.
### Computing and scoring
- [func makeConfusionMatrix() -> MLShapedArray<Float>](classificationmetrics/makeconfusionmatrix.md)
  Computes the confusion matrix.
- [func precisionScore(label: Label) -> Double](classificationmetrics/precisionscore(label:).md)
  Computes the precision score for a class label.
- [func recallScore(label: Label) -> Double](classificationmetrics/recallscore(label:).md)
  Computes the recall score for a class label.
- [func count(label: Label) -> Int](classificationmetrics/count(label:).md)
  Returns the number of times a label appeared in the ground truth collection.
- [func count(predicted: Label) -> Int](classificationmetrics/count(predicted:).md)
  Returns the number of times a label appeared in the predicted collection.
- [func count(predicted: Label, label: Label) -> Int](classificationmetrics/count(predicted:label:).md)
  Returns the number of times a predicted, true label pair appeared in the label collections.
- [func trueNegativeCount(of: Label) -> Int](classificationmetrics/truenegativecount(of:).md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](classificationmetrics/truepositivecount(of:).md)
  Returns the number of times the predicted label matched the true label.
- [func falseNegativeCount(of: Label) -> Int](classificationmetrics/falsenegativecount(of:).md)
  Returns the number of times a true label was not predicted.
- [func falsePositiveCount(of: Label) -> Int](classificationmetrics/falsepositivecount(of:).md)
  Returns the number of times the predicted label did not match the true label.
- [func f1Score(label: Label) -> Double](classificationmetrics/f1score(label:).md)
  Computes the F1 score for a class label.
- [func mapLabels<T>((Label) throws -> T) rethrows -> ClassificationMetrics<T>](classificationmetrics/maplabels(_:).md)
  Returns new classification metrics where the labels are the result of applying a transformation.
### Updating the metrics
- [func add(some Sequence<(predicted: Label, label: Label)>)](classificationmetrics/add(_:).md)
  Updates the metrics with more predicted and ground truth label pairs.
- [func add(predicted: some Sequence<Label>, groundTruth: some Sequence<Label>)](classificationmetrics/add(predicted:groundtruth:).md)
  Updates the metrics with more predicted and ground truth labels.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Classification](classification.md)
  An item in a classification result.
- [struct ClassificationDistribution](classificationdistribution.md)
  A classification distribution that contains a probability for each classification label.
- [struct MultiLabelClassificationMetrics](multilabelclassificationmetrics.md)
  Multi-label classification metrics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics)*