# f1Score(for:)

**Framework**: Create ML Components  
**Kind**: method

Computes the F1 score from predicted and ground truth values.

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
func f1Score(for label: Label) -> Float
```

#### Return Value

The F1 score for the given label.

#### Discussion

The balanced F-score, or F1 score, is computed as the harmonic mean of the precision and recall. If the provided label does not have a confidence threshold, the F1 score is NaN.

## Parameters

- `label`: The label to use as true positive.

## See Also

- [func count(of: Label) -> Int](multilabelclassificationmetrics/count(of:).md)
  Returns the number of times a label appeared in the ground truth collection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/f1score(for:))*