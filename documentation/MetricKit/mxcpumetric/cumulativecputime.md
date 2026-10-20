# cumulativeCPUTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of CPU the app used.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CPUTimeMetric`](../cputimemetric.md) instead.

## Declaration

```swift
var cumulativeCPUTime: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * cumulativeCPUTime;
```

## See Also

### Reading CPU use
- [var cumulativeCPUInstructions: Measurement<Unit>](./cumulativecpuinstructions.md)
  The total number of CPU instructions the app executed during the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpumetric/cumulativecputime)*