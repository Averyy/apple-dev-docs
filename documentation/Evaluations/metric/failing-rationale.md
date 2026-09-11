# failing(rationale:)

**Framework**: Evaluations  
**Kind**: method

Returns a metric with a failing result.

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
func failing(rationale: String? = nil) -> Metric
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Discussion

```swift
let failingResult = metric.failing(rationale: "No match found")
```

## See Also

- [func passing(rationale: String?) -> Metric](metric/passing(rationale:).md)
  Returns a metric with a passing result.
- [func scoring(Double, rationale: String?) -> Metric](metric/scoring(_:rationale:).md)
  Returns a metric with a numeric result.
- [func ignore(rationale: String?) -> Metric](metric/ignore(rationale:).md)
  Returns a metric with an ignored result, excluded from aggregation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/failing(rationale:))*