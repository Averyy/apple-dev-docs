# wait()

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
func wait()
```

#### Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.

## See Also

- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchsemaphore/wait(timeout:).md)
  Waits for, or decrements, a semaphore.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchsemaphore/wait(walltimeout:).md)
  Waits for, or decrements, a semaphore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsemaphore/wait())*