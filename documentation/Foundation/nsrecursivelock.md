# NSRecursiveLock

**Framework**: Foundation  
**Kind**: class

A lock that may be acquired multiple times by the same thread without causing a deadlock.

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
class NSRecursiveLock
```

#### Overview

[`NSRecursiveLock`](nsrecursivelock.md) defines a lock that may be acquired multiple times by the same thread without causing a deadlock, a situation where a thread is permanently blocked waiting for itself to relinquish a lock. While the locking thread has one or more locks, all other threads are prevented from accessing the code protected by the lock.

## Topics

### Acquiring a Lock
- [func lock(before: Date) -> Bool](nsrecursivelock/lock(before:).md)
  Attempts to acquire a lock before a given date.
- [func `try`() -> Bool](nsrecursivelock/try.md)
  Attempts to acquire a lock, and immediately returns a Boolean value that indicates whether the attempt was successful.
### Naming the Lock
- [var name: String?](nsrecursivelock/name.md)
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
- [class NSLock](nslock.md)
  An object that coordinates the operation of multiple threads of execution within the same application.
- [class NSDistributedLock](nsdistributedlock.md)
  A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [class NSConditionLock](nsconditionlock.md)
  A lock that can be associated with specific, user-defined conditions.
- [class NSCondition](nscondition.md)
  A condition variable whose semantics follow those used for POSIX-style conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrecursivelock)*