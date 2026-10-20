# EvaluationError.duplicateMetricName(name:)

**Framework**: Evaluations  
**Kind**: case  
**Role**: Case

Two evaluators — or a single evaluator returning multiple metrics — produced a metric with the same name for the same sample.

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
case duplicateMetricName(name: String)
```

#### Discussion

Metric names double as DataFrame column names, so a repeated name would otherwise silently overwrite the first metric’s value instead of failing loudly.

## Parameters

- `name`: The metric name that was produced more than once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror/duplicatemetricname(name:))*