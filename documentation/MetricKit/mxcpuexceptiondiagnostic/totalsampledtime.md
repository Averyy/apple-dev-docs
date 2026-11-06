# totalSampledTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total time the app was sampled during the exception.

**Availability**:
- iOS 14.0+ - Deprecated in 27.3
- iPadOS 14.0+ - Deprecated in 27.3
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Use [`totalSampledTime`](../cpuexceptiondiagnostic/totalsampledtime.md) instead.

## Declaration

```swift
var totalSampledTime: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * totalSampledTime;
```

## See Also

### Viewing app CPU time
- [var totalCPUTime: Measurement<UnitDuration>](./totalcputime.md)
  The total CPU time used during the exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpuexceptiondiagnostic/totalsampledtime)*