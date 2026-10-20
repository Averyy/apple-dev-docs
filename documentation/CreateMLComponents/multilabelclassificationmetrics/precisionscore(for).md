# precisionScore(for:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Computes the precision score for a class label.

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
func precisionScore(for label: Label) -> Float
```

Available when `Label` conforms to `Hashable`.

#### Return Value

The precision score for the given label.

#### Discussion

Precision score is computed as the ratio `truePositive / (truePositive + falsePositive)`.

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
- [func recallScore(for: Label) -> Float](./recallscore%28for%29.md)
  Computes the recall score for a class label.
- [func trueNegativeCount(of: Label) -> Int](./truenegativecount%28of%29.md)
  Returns the number of times a label was not in the predicted or ground truth collections.
- [func truePositiveCount(of: Label) -> Int](./truepositivecount%28of%29.md)
  Returns the number of times the predicted label matched the true label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/precisionscore(for:))*