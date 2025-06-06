# NSLock

**Framework**: Foundation  
**Kind**: class

An object that coordinates the operation of multiple threads of execution within the same application.

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
class NSLock
```

#### Overview

An [`NSLock`](nslock.md) object can be used to mediate access to an application’s global data or to protect a critical section of code, allowing it to run atomically.

> ⚠️ **Warning**:  The [`NSLock`](nslock.md) class uses POSIX threads to implement its locking behavior. When sending an unlock message to an [`NSLock`](nslock.md) object, you must be sure that message is sent from the same thread that sent the initial lock message. Unlocking a lock from a different thread can result in undefined behavior.

 The [`NSLock`](nslock.md) class uses POSIX threads to implement its locking behavior. When sending an unlock message to an [`NSLock`](nslock.md) object, you must be sure that message is sent from the same thread that sent the initial lock message. Unlocking a lock from a different thread can result in undefined behavior.

You should not use this class to implement a recursive lock. Calling the `lock` method twice on the same thread will lock up your thread permanently. Use the [`NSRecursiveLock`](nsrecursivelock.md) class to implement recursive locks instead.

Unlocking a lock that is not locked is considered a programmer error and should be fixed in your code. The [`NSLock`](nslock.md) class reports such errors by printing an error message to the console when they occur.

## Topics

### Acquiring a Lock
- [func lock(before: Date) -> Bool](nslock/lock(before:).md)
  Attempts to acquire a lock before a given time and returns a Boolean value indicating whether the attempt was successful.
- [func `try`() -> Bool](nslock/try.md)
  Attempts to acquire a lock and immediately returns a Boolean value that indicates whether the attempt was successful.
### Naming the Lock
- [var name: String?](nslock/name.md)
  The name associated with the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSLocking](nslocking.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class Thread](thread.md)
  A thread of execution.
- [protocol NSLocking](nslocking.md)
  The elementary methods adopted by classes that define lock objects.
- [class NSRecursiveLock](nsrecursivelock.md)
  A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [class NSDistributedLock](nsdistributedlock.md)
  A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [class NSConditionLock](nsconditionlock.md)
  A lock that can be associated with specific, user-defined conditions.
- [class NSCondition](nscondition.md)
  A condition variable whose semantics follow those used for POSIX-style conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslock)*