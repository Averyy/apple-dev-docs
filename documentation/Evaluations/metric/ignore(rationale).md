# ignore(rationale:)

**Framework**: Evaluations  
**Kind**: method

Returns a metric with an ignored result, excluded from aggregation.

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
func ignore(rationale: String? = nil) -> Metric
```

#### Discussion

```swift
let ignoredResult = metric.ignore()
```

## See Also

- [func passing(rationale: String?) -> Metric](metric/passing(rationale:).md)
  Returns a metric with a passing result.
- [func failing(rationale: String?) -> Metric](metric/failing(rationale:).md)
  Returns a metric with a failing result.
- [func scoring(Double, rationale: String?) -> Metric](metric/scoring(_:rationale:).md)
  Returns a metric with a numeric result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/ignore(rationale:))*