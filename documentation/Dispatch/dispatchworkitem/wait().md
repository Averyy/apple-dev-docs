# wait()

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Causes the caller to wait synchronously until the dispatch work item finishes executing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func wait()
```

## Discussion

This method returns immediately if the current work item has already finished executing.

## See Also

### Waiting for the Completion of a Work Item
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](./wait%28timeout%29.md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](./wait%28walltimeout%29.md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [struct DispatchTime](../dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](../dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/wait())*