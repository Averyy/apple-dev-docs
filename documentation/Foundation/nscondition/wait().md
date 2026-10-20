# wait()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) wait;
```

#### Discussion

You must lock the receiver prior to calling this method.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [func lock()](../nslocking/lock%28%29.md)
  Attempts to acquire a lock, blocking a thread’s execution until the lock can be acquired.
### Waiting for the Lock
- [func wait(until: Date) -> Bool](./wait%28until%29.md)
  Blocks the current thread until the condition is signaled or the specified time limit is reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscondition/wait())*