# lock()

**Framework**: Core Data  
**Kind**: method

Attempts to acquire a lock on the context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func lock()
```

#### Discussion

This method blocks a thread’s execution until the lock can be acquired. An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is past, the thread relinquishes the lock by invoking [`unlock()`](nsmanagedobjectcontext/unlock().md).

Sending this message to a managed object context helps the framework to understand the scope of a transaction in a multi-threaded environment. It is preferable to use the `NSManagedObjectContext`’s implementation of `NSLocking` instead using of a separate mutex object.

If you lock (or successfully `tryLock`) a managed object context, the thread in which the lock call is made must keep a strong reference to the context until it invokes unlock, otherwise if the context is deallocated this will result in deadlock.

## See Also

- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](nsmanagedobjectcontext/init(concurrencytype:).md)
  Creates a context that uses the specified concurrency type.
- [convenience init()](nsmanagedobjectcontext/init.md)
- [func tryLock() -> Bool](nsmanagedobjectcontext/trylock.md)
  Attempts to acquire a lock.
- [func unlock()](nsmanagedobjectcontext/unlock.md)
  Relinquishes a previously acquired lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/lock())*