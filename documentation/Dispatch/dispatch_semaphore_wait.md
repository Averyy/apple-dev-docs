# dispatch_semaphore_wait

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Waits for (decrements) a semaphore.

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
extern intptr_t dispatch_semaphore_wait(dispatch_semaphore_t dsema, dispatch_time_t timeout);
```

#### Return Value

Returns zero on success, or non-zero if the timeout occurred.

#### Discussion

Decrement the counting semaphore. If the resulting value is less than zero, this function waits for a signal to occur before returning.

## Parameters

- `dsema`: The semaphore. This parameter cannot be `NULL`.
- `timeout`: When to timeout (see [`dispatch_time`](./dispatch_time.md)). The constants [`DISPATCH_TIME_NOW`](./dispatch_time_now.md) and [`DISPATCH_TIME_FOREVER`](./dispatch_time_forever.md) are available as a convenience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_semaphore_wait)*