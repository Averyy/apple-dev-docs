# failing(rationale:)

**Framework**: Evaluations  
**Kind**: method

Returns a metric with a failing result.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func failing(rationale: String? = nil) -> Metric
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)

## See Also

- [func passing(rationale: String?) -> Metric](metric/passing(rationale:).md)
  Returns a metric with a passing result.
- [func scoring(Double, rationale: String?) -> Metric](metric/scoring(_:rationale:).md)
  Returns a metric with a numeric result.
- [func ignore(rationale: String?) -> Metric](metric/ignore(rationale:).md)
  Returns a metric with an ignored result, excluded from aggregation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/failing(rationale:))*