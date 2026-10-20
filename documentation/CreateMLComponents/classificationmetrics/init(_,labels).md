# init(_:labels:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

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
init(_ pairs: some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)
```

## Parameters

- `pairs`: A sequence of predicted and true label pairs.
- `labels`: The set of labels to consider.

## See Also

### Creating the distribution
- [init<Predicted, Correct>(Predicted, Correct)](./init%28_,_%29.md)
  Creates classification metrics for predicted and ground truth labels.
- [init()](./init%28%29.md)
  Creates empty classification metrics.
- [init(_:)](./init%28_%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](./init%28predicted,groundtruth,labels%29.md)
  Creates classification metrics for predicted and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init(_:labels:))*