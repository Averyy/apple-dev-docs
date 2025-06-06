# wait(timeout:)

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
func wait(timeout: DispatchTime) -> DispatchTimeoutResult
```

#### Return Value

A result value indicating whether the method returned due to a timeout.

## Parameters

- `timeout`: The latest time to wait for a group to complete.

## See Also

- [func wait()](dispatchgroup/wait.md)
  Waits synchronously for the previously submitted work to finish.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchgroup/wait(walltimeout:).md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/wait(timeout:))*