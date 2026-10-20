# peakMemoryUsage

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The largest amount of memory used by the app.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PeakMemoryMetric`](../peakmemorymetric.md) instead.

## Declaration

```swift
var peakMemoryUsage: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * peakMemoryUsage;
```

## See Also

### Measuring memory use
- [var averageSuspendedMemory: MXAverage<UnitInformationStorage>](./averagesuspendedmemory.md)
  The average amount of memory in use by the app when it’s suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmemorymetric/peakmemoryusage)*