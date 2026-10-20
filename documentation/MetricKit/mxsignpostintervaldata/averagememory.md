# averageMemory

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The average memory used during the logged intervals.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`averageMemory`](../signpostintervalmetric/averagememory.md) instead.

## Declaration

```swift
var averageMemory: MXAverage<UnitInformationStorage>? { get }
```

```objc
@property (strong, readonly, nullable) MXAverage<NSUnitInformationStorage *> * averageMemory;
```

## See Also

### Reading Power and Performance Information
- [var cumulativeCPUTime: Measurement<UnitDuration>?](./cumulativecputime.md)
  The total amount of CPU time used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](./cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [var cumulativeHitchTimeRatio: Measurement<Unit>?](./cumulativehitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata/averagememory)*