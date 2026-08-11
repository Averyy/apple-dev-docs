# totalAnimationTime

**Framework**: MetricKit  
**Kind**: property

The total time spent animating during the logged intervals.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let totalAnimationTime: Measurement<UnitDuration>?
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

## See Also

- [let averageMemory: AverageStatistics<UnitInformationStorage>?](signpostintervalmetric/averagememory.md)
  The average memory used during the logged intervals.
- [let cpuTime: Measurement<UnitDuration>?](signpostintervalmetric/cputime.md)
  The total amount of CPU time used during the logged intervals.
- [let logicalWrites: Measurement<UnitInformationStorage>?](signpostintervalmetric/logicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [let hitchTimeRatio: Measurement<HitchTimeRatio>?](signpostintervalmetric/hitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.
- [let totalHitchTime: Measurement<UnitDuration>?](signpostintervalmetric/totalhitchtime.md)
  The total time spent hitching during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/signpostintervalmetric/totalanimationtime)*