# trueNegativeCount(of:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Returns the number of times a label was not in the predicted or ground truth collections.

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
func trueNegativeCount(of label: Label) -> Int
```

Available when `Label` conforms to `Hashable`.

#### Return Value

The true negative count.

#### Discussion

If the label does not have a confidence threshold, the true negative count is 0. If the label has a confidence threshold NaN, the true negative count is the number elements in the ground truth collection that do not contain the label. If the label is not in the known set of labels, the true negative count is 0.

## Parameters

- `label`: The label to use as true positive.

## See Also

### Computing and scoring
- [func count(of: Label) -> Int](./count%28of%29.md)
  Returns the number of times a label appeared in the ground truth collection.
- [func f1Score(for: Label) -> Float](./f1score%28for%29.md)
  Computes the F1 score from predicted and ground truth values.
- [func falseNegativeCount(of: Label) -> Int](./falsenegativecount%28of%29.md)
  Returns the number of times a true label was not predicted.
- [func falsePositiveCount(of: Label) -> Int](./falsepositivecount%28of%29.md)
  Returns the number of times the predicted label did not match the true label.
- [func precisionScore(for: Label) -> Float](./precisionscore%28for%29.md)
  Computes the precision score for a class label.
- [func recallScore(for: Label) -> Float](./recallscore%28for%29.md)
  Computes the recall score for a class label.
- [func truePositiveCount(of: Label) -> Int](./truepositivecount%28of%29.md)
  Returns the number of times the predicted label matched the true label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/truenegativecount(of:))*