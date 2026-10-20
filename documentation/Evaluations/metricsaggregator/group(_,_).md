# group(_:_:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Instance Method

Creates a group of related metrics.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
mutating func group(_ name: String, _ body: (inout MetricsAggregator.Group) -> Void)
```

## Mentions

- [Evaluating tool-calling behavior](../evaluating-tool-calling-behavior.md)

#### Discussion

Use this to organize your metrics into logical groups for better readability.

#### Example

```swift
let accuracy = Metric("Accuracy")

func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.group("Quality Metrics") { group in
        group.computeMean(of: accuracy)
        group.computeMedian(of: accuracy)
    }
}
```

## See Also

### Grouping metrics
- [MetricsAggregator.Group](./group.md)
  A grouped collection of related metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metricsaggregator/group(_:_:))*