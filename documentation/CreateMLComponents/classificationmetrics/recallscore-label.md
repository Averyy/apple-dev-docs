# recallScore(label:)

**Framework**: Create ML Components  
**Kind**: method

Computes the recall score for a class label.

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
func recallScore(label: Label) -> Double
```

#### Return Value

The recall score for the given label.

#### Discussion

Precision score is computed as the ratio `tp / (tp + fn)` where `tp` is the number of true positives and `fn` is the number of false negatives.

## Parameters

- `label`: The label to use as true positive.

## See Also

- [func makeConfusionMatrix() -> MLShapedArray<Float>](classificationmetrics/makeconfusionmatrix.md)
  Computes the confusion matrix.
- [func precisionScore(label: Label) -> Double](classificationmetrics/precisionscore(label:).md)
  Computes the precision score for a class label.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/recallscore(label:))*