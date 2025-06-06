# init(_:)

**Framework**: Create ML Components  
**Kind**: init

Creates classification metrics from a temporal sequence of annotated classifications.

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
init<S, Inner>(_ predicted: S) async throws where S : Sequence, Inner : TemporalSequence, S.Element == AnnotatedFeature<Inner, Label>, Inner.Feature == ClassificationDistribution<Label>
```

#### Discussion

- Parameters - predicted: The predicted sequence of annotated temporal sequences of classification distributions.

## See Also

- [init<Predicted, Correct>(Predicted, Correct)](classificationmetrics/init(_:_:).md)
  Creates classification metrics for predicted and ground truth labels.
- [init()](classificationmetrics/init.md)
  Creates empty classification metrics.
- [init(some Sequence<(predicted: Label, label: Label)>)](classificationmetrics/init(_:)-5afx5.md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init(some Sequence<(predicted: Label, label: Label)>, labels: Set<Label>)](classificationmetrics/init(_:labels:).md)
  Creates classification metrics for a sequence of predicted and ground truth label pairs.
- [init<Predicted, Correct>(predicted: Predicted, groundTruth: Correct, labels: Set<Label>)](classificationmetrics/init(predicted:groundtruth:labels:).md)
  Creates classification metrics for predicted and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init(_:)-7nms4)*