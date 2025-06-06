# init(predicted:groundTruth:labels:)

**Framework**: Create ML Components  
**Kind**: init

Creates classification metrics for predicted and ground truth labels.

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
init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>) where Label == Predicted.Element, Predicted : Sequence, Correct : Sequence, Predicted.Element == Correct.Element
```

#### Discussion

The predicted and ground truth collections are matched element by element in the order they are provided. Both collections must have the same number of elements. Labels not in the labels set are ignored.

- Parameters - predicted: The predicted labels.
- groundTruth: The true labels.
- labels: The set of labels to consider.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init(predicted:groundtruth:labels:))*