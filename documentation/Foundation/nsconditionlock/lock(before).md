# lock(before:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) lockBeforeDate:(NSDate *) limit;
```

## Return Value

[`true`](../../Swift/true.md) if the lock is acquired within the time limit, [`false`](../../Swift/false.md) otherwise.

## Discussion

The condition associated with the receiver isn’t taken into account in this operation. This method blocks the thread’s execution until the receiver acquires the lock or `limit` is reached.

## Parameters

- `limit`: The date by which the lock must be acquired or the attempt will time out.

## See Also

### Acquiring and Releasing a Lock
- [func lock(whenCondition: Int)](./lock%28whencondition%29.md)
  Attempts to acquire a lock.
- [func lock(whenCondition: Int, before: Date) -> Bool](./lock%28whencondition,before%29.md)
  Attempts to acquire a lock before a specified moment in time.
- [func `try`() -> Bool](./try%28%29.md)
  Attempts to acquire a lock without regard to the receiver’s condition.
- [func tryLock(whenCondition: Int) -> Bool](./trylock%28whencondition%29.md)
  Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [func unlock(withCondition: Int)](./unlock%28withcondition%29.md)
  Relinquishes the lock and sets the receiver’s condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconditionlock/lock(before:))*