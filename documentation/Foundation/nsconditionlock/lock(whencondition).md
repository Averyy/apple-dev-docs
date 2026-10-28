# lock(whenCondition:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock.

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
func lock(whenCondition condition: Int)
```

```objc
- (void) lockWhenCondition:(NSInteger) condition;
```

## Discussion

The receiver’s condition must be equal to `condition` before the locking operation will succeed. This method blocks the thread’s execution until the lock can be acquired.

## Parameters

- `condition`: The condition to match on.

## See Also

### Acquiring and Releasing a Lock
- [func lock(before: Date) -> Bool](./lock%28before%29.md)
  Attempts to acquire a lock before a specified moment in time.
- [func lock(whenCondition: Int, before: Date) -> Bool](./lock%28whencondition,before%29.md)
  Attempts to acquire a lock before a specified moment in time.
- [func `try`() -> Bool](./try%28%29.md)
  Attempts to acquire a lock without regard to the receiver’s condition.
- [func tryLock(whenCondition: Int) -> Bool](./trylock%28whencondition%29.md)
  Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [func unlock(withCondition: Int)](./unlock%28withcondition%29.md)
  Relinquishes the lock and sets the receiver’s condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/lock(whencondition:))*