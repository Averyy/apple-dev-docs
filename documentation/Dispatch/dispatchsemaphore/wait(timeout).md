# wait(timeout:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Waits for, or decrements, a semaphore.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func wait(timeout: DispatchTime) -> DispatchTimeoutResult
```

#### Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.

## Parameters

- `timeout`: The latest time to wait for a signal.

## See Also

### Blocking on the Semaphore
- [func wait()](./wait%28%29.md)
  Waits for, or decrements, a semaphore.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](./wait%28walltimeout%29.md)
  Waits for, or decrements, a semaphore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsemaphore/wait(timeout:))*