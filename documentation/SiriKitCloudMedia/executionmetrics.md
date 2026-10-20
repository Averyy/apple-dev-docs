# ExecutionMetrics

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Timing information to isolate service performance from network delays.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object ExecutionMetrics
```

## Properties

- `received` (date-time): The UTC time the service receives the request.
- `completed` (date-time): The UTC time the service finishes processing this [`Invocation`](./invocation.md).
- `duration` (float): The time, in seconds, that elapses while the service processes this request. Provide millisecond precision, if possible.

## See Also

### Instrumenting Your Service
- [type ServiceDebugReference](./servicedebugreference.md)
  A URI that references debugging information for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/executionmetrics)*