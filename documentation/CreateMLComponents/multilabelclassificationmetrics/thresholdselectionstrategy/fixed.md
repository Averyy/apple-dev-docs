# MultiLabelClassificationMetrics.ThresholdSelectionStrategy.fixed(_:)

**Framework**: Create ML Components  
**Kind**: case

A confidence threshold strategy that uses the specified thresholds for each label.

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
case fixed([Label : Float])
```

## See Also

- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.balancedPrecisionAndRecall](multilabelclassificationmetrics/thresholdselectionstrategy/balancedprecisionandrecall.md)
  A confidence threshold strategy that balances precision and recall equivalently.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.precision(_:minimumRecall:)](multilabelclassificationmetrics/thresholdselectionstrategy/precision(_:minimumrecall:).md)
  A confidence threshold strategy for a specific precision that has at least a minimum recall value.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.recall(_:minimumPrecision:)](multilabelclassificationmetrics/thresholdselectionstrategy/recall(_:minimumprecision:).md)
  A confidence threshold strategy for a recall precision that has at least a minimum precision value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/thresholdselectionstrategy/fixed(_:))*