# init()

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates empty classification metrics.

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
init()
```

## See Also

### Creating the distribution
- [init<Predicted, Correct>(Predicted, Correct)](./init%28_,_%29.md)
  Creates classification metrics for predicted and ground truth labels.
- [init(_:)](./init%28_%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init(some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)](./init%28_,labels%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](./init%28predicted,groundtruth,labels%29.md)
  Creates classification metrics for predicted and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init())*