# wait()

**Framework**: Foundation  
**Kind**: method

Blocks the current thread until the condition is signaled.

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
func wait()
```

#### Discussion

You must lock the receiver prior to calling this method.

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [func lock()](nslocking/lock.md)
  Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.
- [func wait(until: Date) -> Bool](nscondition/wait(until:).md)
  Blocks the current thread until the condition is signaled or the specified time limit is reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscondition/wait())*