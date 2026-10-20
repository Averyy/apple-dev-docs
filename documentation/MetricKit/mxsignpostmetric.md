# MXSignpostMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing a custom metric.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`SignpostIntervalMetric`](./signpostintervalmetric.md) instead.

## Declaration

```swift
class MXSignpostMetric
```

```objc
@interface MXSignpostMetric : MXMetric
```

#### Overview

A custom metric is an event type with a developer-defined name and category. You can add custom metrics to daily reports to capture information specific to your app.

Custom metrics are a type of signpost saved to custom OS logs created using [`makeLogHandle(category:)`](./mxmetricmanager/makeloghandle%28category%29.md). The daily report contains information about the number and duration of custom events, as well as the power and performance impact of those events. Only custom metric events logged using MetricKit utility functions capture additional power and performance data.

> **Note**:  The system limits the number of custom signpost metrics saved to the log in order to reduce on-device memory overhead. Limit use of custom metrics to critical sections of code.

## Topics

### Logging custom metrics
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](./mxsignpost%28_,dso,log,name,signpostid,_,_%29.md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](./mxsignpostanimationintervalbegin%28dso,log,name,signpostid,_,_%29.md)
  Posts the start time of an animation interval to the log system.
### Reading custom metric data
- [var signpostIntervalData: MXSignpostIntervalData?](./mxsignpostmetric/signpostintervaldata.md)
  The data captured for a custom metric.
- [class MXSignpostIntervalData](./mxsignpostintervaldata.md)
  A data object representing the captured data for a custom metric.
### Reading data about the custom metric
- [var signpostName: String](./mxsignpostmetric/signpostname.md)
  The developer-specified name of the custom metric represented by the object.
- [var signpostCategory: String](./mxsignpostmetric/signpostcategory.md)
  The developer-specified category of the custom metric represented by the object.
- [var totalCount: Int](./mxsignpostmetric/totalcount.md)
  The total number of occurrences of the captured custom metric.

## Relationships

### Inherits From
- [MXMetric](./mxmetric.md)
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

### Related Documentation
- [Logging](../os/logging.md)
  Capture telemetry from your app for debugging and performance analysis using the unified logging system.
### Signpost metrics
- [class MXSignpostIntervalData](./mxsignpostintervaldata.md)
  A data object representing the captured data for a custom metric.
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](./mxsignpost%28_,dso,log,name,signpostid,_,_%29.md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](./mxsignpostanimationintervalbegin%28dso,log,name,signpostid,_,_%29.md)
  Posts the start time of an animation interval to the log system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostmetric)*