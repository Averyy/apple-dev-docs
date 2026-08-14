# MXSignpostIntervalData

**Framework**: MetricKit  
**Kind**: class

A data object representing the captured data for a custom metric.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
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
### Initializers
- [init?(coder: NSCoder)](mxsignpostintervaldata/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXSignpostMetric](mxsignpostmetric.md)
  An object representing a custom metric.
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpost(_:dso:log:name:signpostid:_:_:).md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:).md)
  Posts the start time of an animation interval to the log system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata)*