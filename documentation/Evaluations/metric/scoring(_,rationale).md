# scoring(_:rationale:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Instance Method

Returns a metric with a numeric result.

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
func scoring(_ value: Double, rationale: String? = nil) -> Metric
```

## Mentions

- [Evaluating language model responses](../evaluating-language-model-responses.md)

## Discussion

```swift
let scoreResult = metric.scoring(0.85, rationale: "Partial match")
```

## See Also

### Producing results
- [func passing(rationale: String?) -> Metric](./passing%28rationale%29.md)
  Returns a metric with a passing result.
- [func failing(rationale: String?) -> Metric](./failing%28rationale%29.md)
  Returns a metric with a failing result.
- [func ignore(rationale: String?) -> Metric](./ignore%28rationale%29.md)
  Returns a metric with an ignored result, excluded from aggregation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/scoring(_:rationale:))*