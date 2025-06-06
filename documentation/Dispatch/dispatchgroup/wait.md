# wait()

**Framework**: Dispatch  
**Kind**: method

Waits synchronously for the previously submitted work to finish.

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
func wait()
```

## See Also

- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchgroup/wait(timeout:).md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchgroup/wait(walltimeout:).md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/wait())*