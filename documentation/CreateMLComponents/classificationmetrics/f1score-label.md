# f1Score(label:)

**Framework**: Create ML Components  
**Kind**: method

Computes the F1 score for a class label.

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
func f1Score(label: Label) -> Double
```

#### Return Value

The F1 score for the given label.

#### Discussion

The balanced F-score, or F1 score, is computed as the harmonic mean of the precision and recall.

## Parameters

- `label`: The label to use as true positive.

## See Also

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
- [func mapLabels<T>((Label) throws -> T) rethrows -> ClassificationMetrics<T>](classificationmetrics/maplabels(_:).md)
  Returns new classification metrics where the labels are the result of applying a transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/f1score(label:))*