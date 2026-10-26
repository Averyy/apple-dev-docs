# MXSignpostIntervalBegin

**Framework**: MetricKit  
**Kind**: macro  
**Role**: Macro

Post the start time of a custom metric event to a metric kit log.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 12.0+
- tvOS
- visionOS 1.0+

## Declaration

```c
#define MXSignpostIntervalBegin(log, event_id, name, ...)
```

## Parameters

- `log`: A log for the category of the event that was created previously using [`makeLogHandle(category:)`](./mxmetricmanager/makeloghandle%28category%29.md).
- `event_id`: An [`OSSignpostID`](../os/ossignpostid.md) for the underlyng `os_signpost`.
- `name`: A string containing developer assigned name of the custom event.
- `…`: The variable arguments for [`os_signpost_event_emit`](../os/os_signpost_event_emit.md).

## See Also

### Signpost metrics
- [class MXSignpostMetric](./mxsignpostmetric.md)
  An object representing a custom metric.
- [class MXSignpostIntervalData](./mxsignpostintervaldata.md)
  A data object representing the captured data for a custom metric.
- [MXSignpostEventEmit](./mxsignposteventemit.md)
  Post a custom metric event to a metric kit log.
- [MXSignpostAnimationIntervalBegin](./mxsignpostanimationintervalbegin.md)
- [MXSignpostIntervalEnd](./mxsignpostintervalend.md)
  Post the end time of a custom metric event to a metric kit log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervalbegin)*