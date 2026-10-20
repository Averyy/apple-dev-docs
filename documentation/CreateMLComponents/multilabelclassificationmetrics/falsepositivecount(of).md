# falsePositiveCount(of:)

**Framework**: Create ML Components  
**Kind**: method

Returns the number of times the predicted label did not match the true label.

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
func falsePositiveCount(of label: Label) -> Int
```

#### Return Value

The false positive count.

#### Discussion

If the label does not have a confidence threshold, the false positive count is the number of elements in the ground truth labels collection that do not contain the label. If the label has a confidence threshold NaN, the false positive count is 0. If the label is not in the known set of labels, the false positive count is 0.

## Parameters

- `label`: The label to use as true positive.

## See Also

- [func count(of: Label) -> Int](multilabelclassificationmetrics/count(of:).md)
  Returns the number of times a label appeared in the ground truth collection.
- [func f1Score(for: Label) -> Float](multilabelclassificationmetrics/f1score(for:).md)
  Computes the F1 score from predicted and ground truth values.
- [func falseNegativeCount(of: Label) -> Int](multilabelclassificationmetrics/falsenegativecount(of:).md)
  Returns the number of times a true label was not predicted.
- [func precisionScore(for: Label) -> Float](multilabelclassificationmetrics/precisionscore(for:).md)
  Computes the precision score for a class label.
- [func recallScore(for: Label) -> Float](multilabelclassificationmetrics/recallscore(for:).md)
  Computes the recall score for a class label.
- [func trueNegativeCount(of: Label) -> Int](multilabelclassificationmetrics/truenegativecount(of:).md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](multilabelclassificationmetrics/truepositivecount(of:).md)
  Returns the number of times the predicted label matched the true label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/falsepositivecount(of:))*