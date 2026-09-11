# environment

**Framework**: MetricKit  
**Kind**: property

Environment context for the device and app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let environment: MetricReport.Environment?
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

This is `nil` when device or app metadata cannot be determined during metric aggregation.

## See Also

- [let timeRange: DateInterval](metricreport/timerange.md)
  The date interval this report covers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/environment-swift.property)*