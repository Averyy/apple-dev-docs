# totalCPUTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total CPU time used during the exception.

**Availability**:
- iOS 14.0+ - Deprecated in 27.3
- iPadOS 14.0+ - Deprecated in 27.3
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Use [`totalCPUTime`](../cpuexceptiondiagnostic/totalcputime.md) instead.

## Declaration

```swift
var totalCPUTime: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * totalCPUTime;
```

## See Also

### Viewing app CPU time
- [var totalSampledTime: Measurement<UnitDuration>](./totalsampledtime.md)
  The total time the app was sampled during the exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpuexceptiondiagnostic/totalcputime)*