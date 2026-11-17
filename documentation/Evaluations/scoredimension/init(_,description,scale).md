# init(_:description:scale:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a scoring dimension.

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
init(_ name: String, description: String? = nil, scale: ScoringScale)
```

## Parameters

- `name`: The dimension name. An [`Evaluation`](../evaluation.md) uses this name as the [`Column`](../../TabularData/column.md) name in its results, and [`MetricsAggregator`](../metricsaggregator.md) uses it to look up the dimension’s metric.
- `description`: Optional description providing context about what this dimension measures.
- `scale`: The scoring scale for this dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoredimension/init(_:description:scale:))*