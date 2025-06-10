# cumulativeHitchTimeRatio

**Framework**: MetricKit  
**Kind**: property

The ratio of the total time spent hitching to the total time spent animating during the logged intervals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeHitchTimeRatio: Measurement<Unit>? { get }
```

## See Also

- [var averageMemory: MXAverage<UnitInformationStorage>?](mxsignpostintervaldata/averagememory.md)
  The average memory used during the logged intervals.
- [var cumulativeCPUTime: Measurement<UnitDuration>?](mxsignpostintervaldata/cumulativecputime.md)
  The total amount of CPU time used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](mxsignpostintervaldata/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata/cumulativehitchtimeratio)*