# meanAveragePrecision

**Framework**: Create ML Components  
**Kind**: property

The mean average precision.

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
var meanAveragePrecision: Float { get }
```

#### Discussion

An average precision score summarizes the precision-recall curve for a label. The mean average precision is the mean of the average precision scores for all the classification labels.

## See Also

- [var confidenceThresholds: [Label : Float]](multilabelclassificationmetrics/confidencethresholds.md)
  A dictionary of label and confidence thresholds.
- [var exampleCount: Int](multilabelclassificationmetrics/examplecount.md)
  The number of examples used to compute the metrics.
- [var labels: Set<Label>](multilabelclassificationmetrics/labels.md)
  The classifier labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/meanaverageprecision)*