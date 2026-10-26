# dispatch_semaphore_signal

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Signals (increments) a semaphore.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern intptr_t dispatch_semaphore_signal(dispatch_semaphore_t dsema);
```

#### Return Value

If the previous value was less than zero, this function wakes a process currently waiting.

#### Discussion

Increment the counting semaphore. If the previous value was less than zero, this function wakes a thread currently waiting in [`dispatch_semaphore_wait`](./dispatch_semaphore_wait.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_semaphore_signal)*