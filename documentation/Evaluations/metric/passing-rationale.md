# passing(rationale:)

**Framework**: Evaluations  
**Kind**: method

Returns a metric with a passing result.

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
func passing(rationale: String? = nil) -> Metric
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Discussion

```swift
let passingResult = metric.passing(rationale: "Exact match")
```

## See Also

- [func failing(rationale: String?) -> Metric](metric/failing(rationale:).md)
  Returns a metric with a failing result.
- [func scoring(Double, rationale: String?) -> Metric](metric/scoring(_:rationale:).md)
  Returns a metric with a numeric result.
- [func ignore(rationale: String?) -> Metric](metric/ignore(rationale:).md)
  Returns a metric with an ignored result, excluded from aggregation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/passing(rationale:))*