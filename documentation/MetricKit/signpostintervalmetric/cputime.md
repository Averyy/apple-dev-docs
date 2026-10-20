# cpuTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of CPU time used during the logged intervals.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let cpuTime: Measurement<UnitDuration>?
```

## Mentions

- [Monitoring app performance with MetricKit](../monitoring-app-performance-with-metrickit.md)

## See Also

### Additional measurements
- [let averageMemory: AverageStatistics<UnitInformationStorage>?](./averagememory.md)
  The average memory used during the logged intervals.
- [let logicalWrites: Measurement<UnitInformationStorage>?](./logicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [let hitchTimeRatio: Measurement<HitchTimeRatio>?](./hitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.
- [let totalHitchTime: Measurement<UnitDuration>?](./totalhitchtime.md)
  The total time spent hitching during the logged intervals.
- [let totalAnimationTime: Measurement<UnitDuration>?](./totalanimationtime.md)
  The total time spent animating during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/signpostintervalmetric/cputime)*