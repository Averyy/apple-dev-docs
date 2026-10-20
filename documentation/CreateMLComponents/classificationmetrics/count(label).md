# count(label:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Returns the number of times a label appeared in the ground truth collection.

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
func count(label: Label) -> Int
```

## Parameters

- `label`: The label.

## See Also

### Computing and scoring
- [func makeConfusionMatrix() -> MLShapedArray<Float>](./makeconfusionmatrix%28%29.md)
  Computes the confusion matrix.
- [func precisionScore(label: Label) -> Double](./precisionscore%28label%29.md)
  Computes the precision score for a class label.
- [func recallScore(label: Label) -> Double](./recallscore%28label%29.md)
  Computes the recall score for a class label.
- [func count(predicted: Label) -> Int](./count%28predicted%29.md)
  Returns the number of times a label appeared in the predicted collection.
- [func count(predicted: Label, label: Label) -> Int](./count%28predicted,label%29.md)
  Returns the number of times a predicted, true label pair appeared in the label collections.
- [func trueNegativeCount(of: Label) -> Int](./truenegativecount%28of%29.md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](./truepositivecount%28of%29.md)
  Returns the number of times the predicted label matched the true label.
- [func falseNegativeCount(of: Label) -> Int](./falsenegativecount%28of%29.md)
  Returns the number of times a true label was not predicted.
- [func falsePositiveCount(of: Label) -> Int](./falsepositivecount%28of%29.md)
  Returns the number of times the predicted label did not match the true label.
- [func f1Score(label: Label) -> Double](./f1score%28label%29.md)
  Computes the F1 score for a class label.
- [func mapLabels<T>((Label) throws -> T) rethrows -> ClassificationMetrics<T>](./maplabels%28_%29.md)
  Returns new classification metrics where the labels are the result of applying a transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/count(label:))*