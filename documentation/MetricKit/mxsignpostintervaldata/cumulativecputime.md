# cumulativeCPUTime

**Framework**: MetricKit  
**Kind**: property

The total amount of CPU time used during the logged intervals.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var cumulativeCPUTime: Measurement<UnitDuration>? { get }
```

## See Also

- [var averageMemory: MXAverage<UnitInformationStorage>?](mxsignpostintervaldata/averagememory.md)
  The average memory used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](mxsignpostintervaldata/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [var cumulativeHitchTimeRatio: Measurement<Unit>?](mxsignpostintervaldata/cumulativehitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata/cumulativecputime)*