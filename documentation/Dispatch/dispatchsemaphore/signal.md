# signal()

**Framework**: Dispatch  
**Kind**: method

Signals (increments) a semaphore.

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
@discardableResult
func signal() -> Int
```

#### Return Value

This function returns non-zero if a thread is woken. Otherwise, zero is returned.

#### Discussion

Increment the counting semaphore. If the previous value was less than zero, this function wakes a thread currently waiting in [`dispatch_semaphore_wait`](dispatch_semaphore_wait.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsemaphore/signal())*