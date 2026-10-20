# init(_:_:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates classification metrics for predicted and ground truth labels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init<Predicted, Correct>(_ predicted: Predicted, _ groundTruth: Correct) where Label == Predicted.Element, Predicted : Collection, Correct : Collection, Predicted.Element == Correct.Element
```

#### Discussion

The predicted and ground truth collections are matched element by element in the order they are provided. Both collections must have the same number of elements.

- Parameters

  - predicted: The predicted labels.
  - groundTruth: The true labels.

## See Also

### Creating the distribution
- [init()](./init%28%29.md)
  Creates empty classification metrics.
- [init(_:)](./init%28_%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init(some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)](./init%28_,labels%29.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](./init%28predicted,groundtruth,labels%29.md)
  Creates classification metrics for predicted and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init(_:_:))*