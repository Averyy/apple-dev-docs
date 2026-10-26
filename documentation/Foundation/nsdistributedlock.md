# NSDistributedLock

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSDistributedLock
```

```objc
@interface NSDistributedLock : NSObject
```

#### Overview

The lock is implemented by an entry (such as a file or directory) in the file system. For multiple applications to use an [`NSDistributedLock`](./nsdistributedlock.md) object to coordinate their activities, the lock must be writable on a file system accessible to all hosts on which the applications might be running.

Use the [`try()`](./nsdistributedlock/try%28%29.md) method to attempt to acquire a lock. You should generally use the [`unlock()`](./nsdistributedlock/unlock%28%29.md) method to release the lock rather than [`break()`](./nsdistributedlock/break%28%29.md).

[`NSDistributedLock`](./nsdistributedlock.md) doesn’t conform to the [`NSLocking`](./nslocking.md) protocol, nor does it have a `lock` method. The protocol’s [`lock()`](./nslocking/lock%28%29.md) method is intended to block the execution of the thread until successful. For an [`NSDistributedLock`](./nsdistributedlock.md) object, this could mean polling the file system at some predetermined rate. A better solution is to provide the [`try()`](./nsdistributedlock/try%28%29.md) method and let you determine the polling frequency that makes sense for your application.

## Topics

### Creating an NSDistributedLock
- [init?(path: String)](./nsdistributedlock/init%28path%29.md)
  Initializes an `NSDistributedLock` object to use as the lock the file-system entry specified by a given path.
- [+ lockWithPath:](./nsdistributedlock/lockwithpath_.md)
  Returns an `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by a given path.
### Acquiring a Lock
- [func `try`() -> Bool](./nsdistributedlock/try%28%29.md)
  Attempts to acquire the receiver and immediately returns a Boolean value that indicates whether the attempt was successful.
### Relinquishing a Lock
- [func `break`()](./nsdistributedlock/break%28%29.md)
  Forces the lock to be relinquished.
- [func unlock()](./nsdistributedlock/unlock%28%29.md)
  Relinquishes the receiver.
### Getting Lock Information
- [var lockDate: Date](./nsdistributedlock/lockdate.md)
  Returns the time the receiver was acquired by any of the `NSDistributedLock` objects using the same path.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Threads and Locking
- [class Thread](./thread.md)
  A thread of execution.
- [protocol NSLocking](./nslocking.md)
  The elementary methods adopted by classes that define lock objects.
- [class NSLock](./nslock.md)
  An object that coordinates the operation of multiple threads of execution within the same application.
- [class NSRecursiveLock](./nsrecursivelock.md)
  A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [class NSConditionLock](./nsconditionlock.md)
  A lock that can be associated with specific, user-defined conditions.
- [class NSCondition](./nscondition.md)
  A condition variable whose semantics follow those used for POSIX-style conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock)*