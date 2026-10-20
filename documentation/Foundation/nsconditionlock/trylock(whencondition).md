# tryLock(whenCondition:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.

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
func tryLock(whenCondition condition: Int) -> Bool
```

```objc
- (BOOL) tryLockWhenCondition:(NSInteger) condition;
```

#### Return Value

[`true`](../../Swift/true.md) if the lock could be acquired, [`false`](../../Swift/false.md) otherwise.

#### Discussion

As part of its implementation, this method invokes [`lock(whenCondition:before:)`](./lock%28whencondition,before%29.md). This method returns immediately.

## See Also

### Acquiring and Releasing a Lock
- [func lock(before: Date) -> Bool](./lock%28before%29.md)
  Attempts to acquire a lock before a specified moment in time.
- [func lock(whenCondition: Int)](./lock%28whencondition%29.md)
  Attempts to acquire a lock.
- [func lock(whenCondition: Int, before: Date) -> Bool](./lock%28whencondition,before%29.md)
  Attempts to acquire a lock before a specified moment in time.
- [func `try`() -> Bool](./try%28%29.md)
  Attempts to acquire a lock without regard to the receiver’s condition.
- [func unlock(withCondition: Int)](./unlock%28withcondition%29.md)
  Relinquishes the lock and sets the receiver’s condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/trylock(whencondition:))*