# Metric.Value.ignore

**Framework**: Evaluations  
**Kind**: case

The metric is not applicable for this sample and should be excluded from aggregation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case ignore
```

#### Discussion

Use this when a sample doesn’t have the necessary data for evaluation (e.g., no tool expectations defined for a tool trajectory metric). Aggregators will skip these results when computing statistics like mean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/value-swift.enum/ignore)*