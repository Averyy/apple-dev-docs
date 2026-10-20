# MXSignpostIntervalData

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

A data object representing the captured data for a custom metric.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`SignpostIntervalMetric`](./signpostintervalmetric.md) instead.

## Declaration

```swift
class MXSignpostIntervalData
```

```objc
@interface MXSignpostIntervalData : NSObject
```

## Topics

### Reading Histogrammed Custom Metric Durations
- [var histogrammedSignpostDuration: MXHistogram<UnitDuration>](./mxsignpostintervaldata/histogrammedsignpostduration.md)
  A histogram of the different time intervals of a custom metric event.
### Reading Power and Performance Information
- [var averageMemory: MXAverage<UnitInformationStorage>?](./mxsignpostintervaldata/averagememory.md)
  The average memory used during the logged intervals.
- [var cumulativeCPUTime: Measurement<UnitDuration>?](./mxsignpostintervaldata/cumulativecputime.md)
  The total amount of CPU time used during the logged intervals.
- [var cumulativeLogicalWrites: Measurement<UnitInformationStorage>?](./mxsignpostintervaldata/cumulativelogicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [var cumulativeHitchTimeRatio: Measurement<Unit>?](./mxsignpostintervaldata/cumulativehitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.
### Initializers
- [init?(coder: NSCoder)](./mxsignpostintervaldata/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Signpost metrics
- [class MXSignpostMetric](./mxsignpostmetric.md)
  An object representing a custom metric.
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](./mxsignpost%28_,dso,log,name,signpostid,_,_%29.md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](./mxsignpostanimationintervalbegin%28dso,log,name,signpostid,_,_%29.md)
  Posts the start time of an animation interval to the log system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata)*