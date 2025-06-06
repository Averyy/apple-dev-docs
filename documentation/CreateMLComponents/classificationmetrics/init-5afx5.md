# init(_:)

**Framework**: Create ML Components  
**Kind**: init

Creates classification metrics for a sequence of predicted and ground truth label pairs.

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
init(_ pairs: some Sequence<(predicted: Label, label: Label)>)
```

## Parameters

- `pairs`: A sequence of predicted and true label pairs.

## See Also

- [init<Predicted, Correct>(Predicted, Correct)](classificationmetrics/init(_:_:).md)
  Creates classification metrics for predicted and ground truth labels.
- [init()](classificationmetrics/init.md)
  Creates empty classification metrics.
- [init<S, Inner>(S) async throws](classificationmetrics/init(_:)-7nms4.md)
  Creates classification metrics from a temporal sequence of annotated classifications.
- [init(some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)](classificationmetrics/init(_:labels:).md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](classificationmetrics/init(predicted:groundtruth:labels:).md)
  Creates classification metrics for predicted and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init(_:)-5afx5)*