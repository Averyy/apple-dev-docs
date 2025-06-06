# try()

**Framework**: Foundation  
**Kind**: method

Attempts to acquire a lock without regard to the receiver’s condition.

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
func `try`() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the lock could be acquired, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

This method returns immediately.

## See Also

- [func lock(before: Date) -> Bool](nsconditionlock/lock(before:).md)
  Attempts to acquire a lock before a specified moment in time.
- [func lock(whenCondition: Int)](nsconditionlock/lock(whencondition:).md)
  Attempts to acquire a lock.
- [func lock(whenCondition: Int, before: Date) -> Bool](nsconditionlock/lock(whencondition:before:).md)
  Attempts to acquire a lock before a specified moment in time.
- [func tryLock(whenCondition: Int) -> Bool](nsconditionlock/trylock(whencondition:).md)
  Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [func unlock(withCondition: Int)](nsconditionlock/unlock(withcondition:).md)
  Relinquishes the lock and sets the receiver’s condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/try())*