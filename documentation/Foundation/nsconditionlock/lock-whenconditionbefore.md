# lock(whenCondition:before:)

**Framework**: Foundation  
**Kind**: method

Attempts to acquire a lock before a specified moment in time.

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
func lock(whenCondition condition: Int, before limit: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the lock is acquired within the time limit, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The receiver’s condition must be equal to `condition` before the locking operation will succeed. This method blocks the thread’s execution until the lock can be acquired or `limit` is reached.

## Parameters

- `condition`: The condition to match on.
- `limit`: The date by which the lock must be acquired or the attempt will time out.

## See Also

- [func lock(before: Date) -> Bool](nsconditionlock/lock(before:).md)
  Attempts to acquire a lock before a specified moment in time.
- [func lock(whenCondition: Int)](nsconditionlock/lock(whencondition:).md)
  Attempts to acquire a lock.
- [func `try`() -> Bool](nsconditionlock/try.md)
  Attempts to acquire a lock without regard to the receiver’s condition.
- [func tryLock(whenCondition: Int) -> Bool](nsconditionlock/trylock(whencondition:).md)
  Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [func unlock(withCondition: Int)](nsconditionlock/unlock(withcondition:).md)
  Relinquishes the lock and sets the receiver’s condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/lock(whencondition:before:))*