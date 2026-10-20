# cumulativeBackgroundTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total time the app is active in the background.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalBackgroundTimeMetric`](../totalbackgroundtimemetric.md) instead.

## Declaration

```swift
var cumulativeBackgroundTime: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * cumulativeBackgroundTime;
```

## See Also

### Reading application run time
- [var cumulativeForegroundTime: Measurement<UnitDuration>](./cumulativeforegroundtime.md)
  The total time the app is in the foreground.
- [var cumulativeBackgroundAudioTime: Measurement<UnitDuration>](./cumulativebackgroundaudiotime.md)
  The total time the app is in the background and playing audio.
- [var cumulativeBackgroundLocationTime: Measurement<UnitDuration>](./cumulativebackgroundlocationtime.md)
  The total time the app is in the background and using location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappruntimemetric/cumulativebackgroundtime)*