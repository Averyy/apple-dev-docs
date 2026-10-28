# break()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Forces the lock to be relinquished.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func `break`()
```

```objc
- (void) breakLock;
```

## Discussion

This method always succeeds unless the lock has been damaged. If another process has already unlocked or broken the lock, this method has no effect. You should generally use [`unlock()`](./unlock%28%29.md) rather than [`break()`](./break%28%29.md) to relinquish a lock.

> ⚠️ **Warning**:  Because `breakLock` can release another process’s lock, it should be used with great caution.

Even if you break a lock, there’s no guarantee that you will then be able to acquire the lock—another process might get it before your [`try()`](./try%28%29.md) is invoked.

Raises an `NSGenericException` if the lock could not be removed.

## See Also

### Relinquishing a Lock
- [func unlock()](./unlock%28%29.md)
  Relinquishes the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/break())*