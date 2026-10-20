# averageSuspendedMemory

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The average amount of memory in use by the app when it’s suspended.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`SuspendedMemoryMetric`](../suspendedmemorymetric.md) instead.

## Declaration

```swift
var averageSuspendedMemory: MXAverage<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) MXAverage<NSUnitInformationStorage *> * averageSuspendedMemory;
```

## See Also

### Measuring memory use
- [var peakMemoryUsage: Measurement<UnitInformationStorage>](./peakmemoryusage.md)
  The largest amount of memory used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmemorymetric/averagesuspendedmemory)*