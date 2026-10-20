# ClassificationMetrics

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init<Predicted, Correct>(Predicted, Correct)](./classificationmetrics/init%28_,_%29.md)
  Creates classification metrics for predicted and ground truth labels.
- [init()](./classificationmetrics/init%28%29.md)
  Creates empty classification metrics.
- [init(_:)](./classificationmetrics/init%28_%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init(some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)](./classificationmetrics/init%28_,labels%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](./classificationmetrics/init%28predicted,groundtruth,labels%29.md)
  Creates classification metrics for predicted and ground truth labels.
### Getting the properties
- [var accuracy: Double](./classificationmetrics/accuracy.md)
  The number of correctly classified examples out of the total number of examples.
- [var exampleCount: Int](./classificationmetrics/examplecount.md)
  The number of examples used to compute the metrics.
- [var labels: Set<Label>](./classificationmetrics/labels.md)
  The set of labels.
- [var restrictToKnownLabels: Bool](./classificationmetrics/restricttoknownlabels.md)
  A Boolean value indicating whether to restrict metrics to labels in the labels set.
### Computing and scoring
- [func makeConfusionMatrix() -> MLShapedArray<Float>](./classificationmetrics/makeconfusionmatrix%28%29.md)
  Computes the confusion matrix.
- [func precisionScore(label: Label) -> Double](./classificationmetrics/precisionscore%28label%29.md)
  Computes the precision score for a class label.
- [func recallScore(label: Label) -> Double](./classificationmetrics/recallscore%28label%29.md)
  Computes the recall score for a class label.
- [func count(label: Label) -> Int](./classificationmetrics/count%28label%29.md)
  Returns the number of times a label appeared in the ground truth collection.
- [func count(predicted: Label) -> Int](./classificationmetrics/count%28predicted%29.md)
  Returns the number of times a label appeared in the predicted collection.
- [func count(predicted: Label, label: Label) -> Int](./classificationmetrics/count%28predicted,label%29.md)
  Returns the number of times a predicted, true label pair appeared in the label collections.
- [func trueNegativeCount(of: Label) -> Int](./classificationmetrics/truenegativecount%28of%29.md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](./classificationmetrics/truepositivecount%28of%29.md)
  Returns the number of times the predicted label matched the true label.
- [func falseNegativeCount(of: Label) -> Int](./classificationmetrics/falsenegativecount%28of%29.md)
  Returns the number of times a true label was not predicted.
- [func falsePositiveCount(of: Label) -> Int](./classificationmetrics/falsepositivecount%28of%29.md)
  Returns the number of times the predicted label did not match the true label.
- [func f1Score(label: Label) -> Double](./classificationmetrics/f1score%28label%29.md)
  Computes the F1 score for a class label.
- [func mapLabels<T>((Label) throws -> T) rethrows -> ClassificationMetrics<T>](./classificationmetrics/maplabels%28_%29.md)
  Returns new classification metrics where the labels are the result of applying a transformation.
### Updating the metrics
- [func add(some Sequence<(predicted: Label, label: Label)>)](./classificationmetrics/add%28_%29.md)
  Updates the metrics with more predicted and ground truth label pairs.
- [func add(predicted: some Sequence<Label>, groundTruth: some Sequence<Label>)](./classificationmetrics/add%28predicted,groundtruth%29.md)
  Updates the metrics with more predicted and ground truth labels.

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
- [struct MultiLabelClassificationMetrics](./multilabelclassificationmetrics.md)
  Multi-label classification metrics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics)*