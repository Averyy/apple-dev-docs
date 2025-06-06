# lock(before:)

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
func lock(before limit: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the lock is acquired within the time limit, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The condition associated with the receiver isn’t taken into account in this operation. This method blocks the thread’s execution until the receiver acquires the lock or `limit` is reached.

## Parameters

- `limit`: The date by which the lock must be acquired or the attempt will time out.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/lock(before:))*