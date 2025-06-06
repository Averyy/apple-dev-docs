# MXSignpostIntervalData

**Framework**: MetricKit  
**Kind**: class

A data object representing the captured data for a custom metric.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MXSignpostIntervalData
```

## Topics

### Reading Histogrammed Custom Metric Durations
- [var histogrammedSignpostDuration: MXHistogram<UnitDuration>](mxsignpostintervaldata/histogrammedsignpostduration.md)
  A histogram of the different time intervals of a custom metric event.
### Reading Power and Performance Information
- [var averageMemory: MXAverage<UnitInformationStorage>?](mxsignpostintervaldata/averagememory.md)
  The average memory used during the logged intervals.
- [var cumulativeCPUTime: Measurement<UnitDuration>?](mxsignpostintervaldata/cumulativecputime.md)
  The total amount of CPU time used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](mxsignpostintervaldata/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [var cumulativeHitchTimeRatio: Measurement<Unit>?](mxsignpostintervaldata/cumulativehitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var signpostIntervalData: MXSignpostIntervalData?](mxsignpostmetric/signpostintervaldata.md)
  The data captured for a custom metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata)*