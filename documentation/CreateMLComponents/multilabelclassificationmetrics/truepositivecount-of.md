# truePositiveCount(of:)

**Framework**: Create ML Components  
**Kind**: method

Returns the number of times the predicted label matched the true label.

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
func truePositiveCount(of label: Label) -> Int
```

#### Return Value

The true positive count.

#### Discussion

If the label does not have a confidence threshold, the true positive count is number of elements in the ground truth labels collection that contains the label. If the label has a confidence threshold NaN, the true positive count is 0. If the label is not in the known set of labels, the true positive count is 0.

## Parameters

- `label`: The label to use as true positive.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/truepositivecount(of:))*