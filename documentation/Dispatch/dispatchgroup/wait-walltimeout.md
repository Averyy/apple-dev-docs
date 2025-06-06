# wait(wallTimeout:)

**Framework**: Dispatch  
**Kind**: method

Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func wait(wallTimeout timeout: DispatchWallTime) -> DispatchTimeoutResult
```

#### Return Value

[`DispatchTimeoutResult.timedOut`](dispatchtimeoutresult/timedout.md) if the method returned due to a timeout, or [`DispatchTimeoutResult.success`](dispatchtimeoutresult/success.md) if the tasks completed.

## Parameters

- `timeout`: The latest time to wait for a group to complete.

## See Also

- [func wait()](dispatchgroup/wait.md)
  Waits synchronously for the previously submitted work to finish.
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchgroup/wait(timeout:).md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/wait(walltimeout:))*