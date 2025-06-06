# MultiLabelClassificationMetrics.ThresholdSelectionStrategy.recall(_:minimumPrecision:)

**Framework**: Create ML Components  
**Kind**: case

A confidence threshold strategy for a recall precision that has at least a minimum precision value.

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
case recall(Float, minimumPrecision: Float)
```

#### Discussion

This strategy selects a threshold for each label by searching for the specified recall value on the label’s precision-recall curve. At the recall, the precision must be greater than or equal to the minimum precision value, otherwise a NaN threshold for the corresponding label is returned.

Use this strategy to reduce the rate of false-negative predictions while constraining the false-positive predictions.

## See Also

- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.balancedPrecisionAndRecall](multilabelclassificationmetrics/thresholdselectionstrategy/balancedprecisionandrecall.md)
  A confidence threshold strategy that balances precision and recall equivalently.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.fixed(_:)](multilabelclassificationmetrics/thresholdselectionstrategy/fixed(_:).md)
  A confidence threshold strategy that uses the specified thresholds for each label.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.precision(_:minimumRecall:)](multilabelclassificationmetrics/thresholdselectionstrategy/precision(_:minimumrecall:).md)
  A confidence threshold strategy for a specific precision that has at least a minimum recall value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/thresholdselectionstrategy/recall(_:minimumprecision:))*