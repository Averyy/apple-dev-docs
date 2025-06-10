# averageMemory

**Framework**: MetricKit  
**Kind**: property

The average memory used during the logged intervals.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var averageMemory: MXAverage<UnitInformationStorage>? { get }
```

## See Also

- [var cumulativeCPUTime: Measurement<UnitDuration>?](mxsignpostintervaldata/cumulativecputime.md)
  The total amount of CPU time used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](mxsignpostintervaldata/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [var cumulativeHitchTimeRatio: Measurement<Unit>?](mxsignpostintervaldata/cumulativehitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata/averagememory)*