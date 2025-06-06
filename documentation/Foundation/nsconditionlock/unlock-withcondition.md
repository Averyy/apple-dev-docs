# unlock(withCondition:)

**Framework**: Foundation  
**Kind**: method

Relinquishes the lock and sets the receiver’s condition.

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
func unlock(withCondition condition: Int)
```

## Parameters

- `condition`: The user-defined condition for the lock. The value of   is user-defined; see the class description for more information.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/unlock(withcondition:))*