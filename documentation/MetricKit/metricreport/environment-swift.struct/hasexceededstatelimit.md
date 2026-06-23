# hasExceededStateLimit

**Framework**: MetricKit  
**Kind**: property

A Boolean indicating if the number of emitted states exceeded the aggregation limit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let hasExceededStateLimit: Bool
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)
- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

When `true`, some states may have been omitted from the report. Metrics associated with the omitted states will be included in the full day interval entry along with non-state-aggregated metrics.

## See Also

- [let lowPowerModeEnabled: Bool](metricreport/environment-swift.struct/lowpowermodeenabled.md)
  Indicates whether low power mode is enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricreport/environment-swift.struct/hasexceededstatelimit)*