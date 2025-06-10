# NSConditionLock

**Framework**: Foundation  
**Kind**: class

A lock that can be associated with specific, user-defined conditions.

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
class NSConditionLock
```

#### Overview

Using an [`NSConditionLock`](nsconditionlock.md) object, you can ensure that a thread can acquire a lock only if a certain condition is met. Once it has acquired the lock and executed the critical section of code, the thread can relinquish the lock and set the associated condition to something new. The conditions themselves are arbitrary: you define them as needed for your application.

## Topics

### Initializing an NSConditionLock Object
- [init(condition: Int)](nsconditionlock/init(condition:).md)
  Initializes a newly allocated `NSConditionLock` object and sets its condition.
### Accessing the Condition
- [var condition: Int](nsconditionlock/condition.md)
  The condition associated with the receiver.
### Acquiring and Releasing a Lock
- [func lock(before: Date) -> Bool](nsconditionlock/lock(before:).md)
  Attempts to acquire a lock before a specified moment in time.
- [func lock(whenCondition: Int)](nsconditionlock/lock(whencondition:).md)
  Attempts to acquire a lock.
- [func lock(whenCondition: Int, before: Date) -> Bool](nsconditionlock/lock(whencondition:before:).md)
  Attempts to acquire a lock before a specified moment in time.
- [func `try`() -> Bool](nsconditionlock/try.md)
  Attempts to acquire a lock without regard to the receiver’s condition.
- [func tryLock(whenCondition: Int) -> Bool](nsconditionlock/trylock(whencondition:).md)
  Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [func unlock(withCondition: Int)](nsconditionlock/unlock(withcondition:).md)
  Relinquishes the lock and sets the receiver’s condition.
### Identifying the Condition Lock
- [var name: String?](nsconditionlock/name.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class Thread](thread.md)
  A thread of execution.
- [protocol NSLocking](nslocking.md)
  The elementary methods adopted by classes that define lock objects.
- [class NSLock](nslock.md)
  An object that coordinates the operation of multiple threads of execution within the same application.
- [class NSRecursiveLock](nsrecursivelock.md)
  A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [class NSDistributedLock](nsdistributedlock.md)
  A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [class NSCondition](nscondition.md)
  A condition variable whose semantics follow those used for POSIX-style conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock)*