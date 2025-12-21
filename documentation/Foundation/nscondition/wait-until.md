# wait(until:)

**Framework**: Foundation  
**Kind**: method

Blocks the current thread until the condition is signaled or the specified time limit is reached.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func wait(until limit: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the condition was signaled; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) if the time limit was reached.

#### Discussion

You must lock the receiver prior to calling this method.

## Parameters

- `limit`: The time at which to wake up the thread if the condition has not been signaled.

## See Also

- [func lock()](nslocking/lock.md)
  Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.
- [func wait()](nscondition/wait.md)
  Blocks the current thread until the condition is signaled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscondition/wait(until:))*