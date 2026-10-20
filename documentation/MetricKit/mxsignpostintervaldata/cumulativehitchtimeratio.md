# cumulativeHitchTimeRatio

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The ratio of the total time spent hitching to the total time spent animating during the logged intervals.

**Availability**:
- iOS 15.0+ - Deprecated in 27.2
- iPadOS 15.0+ - Deprecated in 27.2
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`hitchTimeRatio`](../signpostintervalmetric/hitchtimeratio.md) instead.

## Declaration

```swift
var cumulativeHitchTimeRatio: Measurement<Unit>? { get }
```

```objc
@property (strong, readonly, nullable) NSMeasurement<NSUnit *> * cumulativeHitchTimeRatio;
```

## See Also

### Reading Power and Performance Information
- [var averageMemory: MXAverage<UnitInformationStorage>?](./averagememory.md)
  The average memory used during the logged intervals.
- [var cumulativeCPUTime: Measurement<UnitDuration>?](./cumulativecputime.md)
  The total amount of CPU time used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](./cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata/cumulativehitchtimeratio)*