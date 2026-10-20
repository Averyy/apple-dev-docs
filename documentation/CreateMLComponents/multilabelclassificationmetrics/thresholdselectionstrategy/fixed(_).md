# MultiLabelClassificationMetrics.ThresholdSelectionStrategy.fixed(_:)

**Framework**: Create ML Components  
**Kind**: case  
**Role**: Case

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

### Selection strategies
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.balancedPrecisionAndRecall](./balancedprecisionandrecall.md)
  A confidence threshold strategy that balances precision and recall equivalently.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.precision(_:minimumRecall:)](./precision%28_,minimumrecall%29.md)
  A confidence threshold strategy for a specific precision that has at least a minimum recall value.
- [MultiLabelClassificationMetrics.ThresholdSelectionStrategy.recall(_:minimumPrecision:)](./recall%28_,minimumprecision%29.md)
  A confidence threshold strategy for a recall precision that has at least a minimum precision value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/thresholdselectionstrategy/fixed(_:))*