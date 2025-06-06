# lock()

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func lock()
```

#### Discussion

An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is completed, the thread relinquishes the lock by invoking [`unlock()`](nslocking/unlock().md).

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [func unlock()](nslocking/unlock.md)
  Relinquishes a previously acquired lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocking/lock())*