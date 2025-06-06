# withLockIfAvailable(_:)

**Framework**: Synchronization  
**Kind**: method

Attempts to acquire the lock and then calls the given closure if successful.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
borrowing func withLockIfAvailable<Result, E>(_ body: (inout sending Value) throws(E) -> sending Result) throws(E) -> sending Result? where E : Error, Result : ~Copyable
```

#### Return Value

The return value, if any, of the `body` closure parameter or nil if the lock couldn’t be acquired.

#### Discussion

If the calling thread was successful in acquiring the lock, the closure will be executed and then immediately after it will release ownership of the lock. If we were unable to acquire the lock, this will return `nil`.

This method is equivalent to the following sequence of code:

```swift
guard mutex.tryLock() else {
  return nil
}
defer {
  mutex.unlock()
}
return try body(&value)
```

> ⚠️ **Warning**: Recursive calls to `withLockIfAvailable` within the closure parameter has behavior that is platform dependent. Some platforms may choose to panic the process, deadlock, or leave this behavior unspecified. This will never reacquire the lock however.

Recursive calls to `withLockIfAvailable` within the closure parameter has behavior that is platform dependent. Some platforms may choose to panic the process, deadlock, or leave this behavior unspecified. This will never reacquire the lock however.

## Parameters

- `body`: A closure with a parameter of    that has exclusive access to the value being stored within   this mutex. This closure is considered the critical section   as it will only be executed if the calling thread acquires   the lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/mutex/withlockifavailable(_:))*