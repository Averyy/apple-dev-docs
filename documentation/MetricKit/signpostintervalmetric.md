# SignpostIntervalMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the duration and count of custom signpost intervals.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct SignpostIntervalMetric
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

This metric corresponds to the [`MetricResult.signpostInterval(_:)`](metricresult/signpostinterval(_:).md) case. This metric appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when you enable state reporting.

Create signpost log handles with [`logHandle(category:)`](metricmanager/loghandle(category:).md) and wrap each custom operation with [`mxSignpost(_:dso:log:name:signpostID:_:_:)`](mxsignpost(_:dso:log:name:signpostid:_:_:).md):

```swift
let networkLog = MetricManager.logHandle(category: "NetworkRequests")

func loadProfile() async {
    mxSignpost(.begin, log: networkLog, name: "fetchUserProfile")
    await fetchUserProfile()
    mxSignpost(.end, log: networkLog, name: "fetchUserProfile")
}
```

Signpost intervals measure the duration and frequency of specific code operations, such as network requests, database queries, or image processing. State reporting complements this by segmenting MetricKit metrics by user-visible app state.

## Topics

### Signpost details
- [let signpostName: String](signpostintervalmetric/signpostname.md)
  The developer-specified name of the custom metric represented by the object.
- [let signpostCategory: String](signpostintervalmetric/signpostcategory.md)
  The developer-specified category of the custom metric represented by the object.
### Counts and timing
- [let totalCount: Int](signpostintervalmetric/totalcount.md)
  The total number of occurrences of the captured custom metric.
- [let signpostDuration: Histogram<UnitDuration>](signpostintervalmetric/signpostduration.md)
  A histogram of the different time intervals of a custom metric event.
### Additional measurements
- [let averageMemory: AverageStatistics<UnitInformationStorage>?](signpostintervalmetric/averagememory.md)
  The average memory used during the logged intervals.
- [let cpuTime: Measurement<UnitDuration>?](signpostintervalmetric/cputime.md)
  The total amount of CPU time used during the logged intervals.
- [let logicalWrites: Measurement<UnitInformationStorage>?](signpostintervalmetric/logicalwrites.md)
  The total amount of data written to disk or other long term storage during the logged intervals.
- [let hitchTimeRatio: Measurement<Unit>?](signpostintervalmetric/hitchtimeratio.md)
  The ratio of the total time spent hitching to the total time spent animating during the logged intervals.
- [let totalHitchTime: Measurement<UnitDuration>?](signpostintervalmetric/totalhitchtime.md)
  The total time spent hitching during the logged intervals.
- [let totalAnimationTime: Measurement<UnitDuration>?](signpostintervalmetric/totalanimationtime.md)
  The total time spent animating during the logged intervals.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpost(_:dso:log:name:signpostid:_:_:).md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:).md)
  Posts the start time of an animation interval to the log system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/signpostintervalmetric)*