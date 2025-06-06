# MXSignpostMetric

**Framework**: MetricKit  
**Kind**: class

An object representing a custom metric.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MXSignpostMetric
```

#### Overview

A custom metric is an event type with a developer-defined name and category. You can add custom metrics to daily reports to capture information specific to your app.

Custom metrics are a type of signpost saved to custom OS logs created using [`makeLogHandle(category:)`](mxmetricmanager/makeloghandle(category:).md). The daily report contains information about the number and duration of custom events, as well as the power and performance impact of those events. Only custom metric events logged using MetricKit utility functions capture additional power and performance data.

> **Note**:  The system limits the number of custom signpost metrics saved to the log in order to reduce on-device memory overhead. Limit use of custom metrics to critical sections of code.

 The system limits the number of custom signpost metrics saved to the log in order to reduce on-device memory overhead. Limit use of custom metrics to critical sections of code.

## Topics

### Logging custom metrics
- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpost(_:dso:log:name:signpostid:_:_:).md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.
- [func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:).md)
  Posts the start time of an animation interval to the log system.
### Reading custom metric data
- [var signpostIntervalData: MXSignpostIntervalData?](mxsignpostmetric/signpostintervaldata.md)
  The data captured for a custom metric.
- [class MXSignpostIntervalData](mxsignpostintervaldata.md)
  A data object representing the captured data for a custom metric.
### Reading data about the custom metric
- [var signpostName: String](mxsignpostmetric/signpostname.md)
  The developer-specified name of the custom metric represented by the object.
- [var signpostCategory: String](mxsignpostmetric/signpostcategory.md)
  The developer-specified category of the custom metric represented by the object.
- [var totalCount: Int](mxsignpostmetric/totalcount.md)
  The total number of occurrences of the captured custom metric.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
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

- [Logging](../os/logging.md)
  Capture telemetry from your app for debugging and performance analysis using the unified logging system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostmetric)*