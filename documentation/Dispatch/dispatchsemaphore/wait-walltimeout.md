# wait(wallTimeout:)

**Framework**: Dispatch  
**Kind**: method

Waits for, or decrements, a semaphore.

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
func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult
```

#### Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.

## Parameters

- `wallTimeout`: The latest time to wait for a signal.

## See Also

- [func wait()](dispatchsemaphore/wait.md)
  Waits for, or decrements, a semaphore.
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchsemaphore/wait(timeout:).md)
  Waits for, or decrements, a semaphore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsemaphore/wait(walltimeout:))*