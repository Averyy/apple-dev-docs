# cumulativeGPUTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of GPU time used by the app.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`GPUTimeMetric`](../gputimemetric.md) instead.

## Declaration

```swift
var cumulativeGPUTime: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * cumulativeGPUTime;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxgpumetric/cumulativegputime)*