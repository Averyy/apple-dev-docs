# lock()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock on the context.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use a queue style context and -performBlockAndWait: instead

## Declaration

```swift
func lock()
```

```objc
- (void) lock;
```

#### Discussion

This method blocks a thread’s execution until the lock can be acquired. An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is past, the thread relinquishes the lock by invoking [`unlock()`](./unlock%28%29.md).

Sending this message to a managed object context helps the framework to understand the scope of a transaction in a multi-threaded environment. It is preferable to use the `NSManagedObjectContext`’s implementation of `NSLocking` instead using of a separate mutex object.

If you lock (or successfully `tryLock`) a managed object context, the thread in which the lock call is made must keep a strong reference to the context until it invokes unlock, otherwise if the context is deallocated this will result in deadlock.

## See Also

### Deprecated instance methods
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
- [convenience init()](./init%28%29.md)
- [func tryLock() -> Bool](./trylock%28%29.md)
  Attempts to acquire a lock.
- [func unlock()](./unlock%28%29.md)
  Relinquishes a previously acquired lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/lock())*