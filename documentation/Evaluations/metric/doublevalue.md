# doubleValue

**Framework**: Evaluations  
**Kind**: property

The numeric value of this metric.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
var doubleValue: Double? { get }
```

#### Discussion

- `passing` → `1.0`
- `failing` → `0.0`
- `scoring(x)` → `x`
- `ignore` → `nil`

## See Also

- [let name: String](metric/name.md)
  The name of the metric, used as the DataFrame column name.
- [let value: Metric.Value](metric/value-swift.property.md)
  The result value of this metric.
- [let rationale: String?](metric/rationale.md)
  An optional rationale describing the result.
- [Metric.Value](metric/value-swift.enum.md)
  A metric result value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/doublevalue)*