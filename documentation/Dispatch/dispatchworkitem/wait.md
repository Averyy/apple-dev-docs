# wait()

**Framework**: Dispatch  
**Kind**: method

Causes the caller to wait synchronously until the dispatch work item finishes executing.

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
func wait()
```

#### Discussion

This method returns immediately if the current work item has already finished executing.

## See Also

- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchworkitem/wait(timeout:).md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchworkitem/wait(walltimeout:).md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [struct DispatchTime](dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/wait())*