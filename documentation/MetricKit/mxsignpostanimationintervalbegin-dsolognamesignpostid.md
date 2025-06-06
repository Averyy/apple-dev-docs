# mxSignpostAnimationIntervalBegin(dso:log:name:signpostID:_:_:)

**Framework**: MetricKit  
**Kind**: func

Posts the start time of an animation interval to the log system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
func mxSignpostAnimationIntervalBegin(dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive, _ format: StaticString = "isAnimation=YES \n%{public, signpost:metrics}@", _ arguments: [any CVarArg] = [Unmanaged<NSObject>.fromOpaque(_MXSignpostMetricsSnapshot()).takeUnretainedValue()])
```

#### Discussion

Call this function to mark the beginning of an animation interval in the metric kit log. Provide a `log` that you create with [`makeLogHandle(category:)`](mxmetricmanager/makeloghandle(category:).md), a `name` for the event, and variable `arguments` for [`os_signpost_event_emit`](https://developer.apple.com/documentation/os/os_signpost_event_emit). Don’t alter the parameters `dso`, `signpostID`, or `format`.

## Parameters

- `dso`: A parameter for internal system use.
- `log`: A log object to log the signpost to.
- `name`: A string containing the developer-assigned name of the custom event.
- `signpostID`: A parameter for internal system use.
- `format`: A parameter for internal system use.
- `arguments`: An array of arguments with a format string, followed by the expected number of arguments in the order that they appear in the string.

## See Also

- [func mxSignpost(OSSignpostType, dso: UnsafeRawPointer, log: OSLog, name: StaticString, signpostID: OSSignpostID, StaticString, [any CVarArg])](mxsignpost(_:dso:log:name:signpostid:_:_:).md)
  Posts a single custom metric, the start time of a custom metric, or the end time of a custom metric to the log system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostanimationintervalbegin(dso:log:name:signpostid:_:_:))*