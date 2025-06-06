# wait(timeout:)

**Framework**: Dispatch  
**Kind**: method

Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func wait(timeout: DispatchTime) -> DispatchTimeoutResult
```

#### Return Value

[`DispatchTimeoutResult.success`](dispatchtimeoutresult/success.md) if the method returned because the work item finished executing, or [`DispatchTimeoutResult.timedOut`](dispatchtimeoutresult/timedout.md) if the timeout value was reached.

#### Discussion

This method returns immediately if the current work item has already finished executing.

## Parameters

- `timeout`: The time at which to stop waiting for the dispatch item to finish. Specifying   is equivalent to calling the   method.

## See Also

- [func wait()](dispatchworkitem/wait.md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchworkitem/wait(walltimeout:).md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [struct DispatchTime](dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/wait(timeout:))*