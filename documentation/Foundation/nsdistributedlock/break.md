# break()

**Framework**: Foundation  
**Kind**: method

Forces the lock to be relinquished.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func `break`()
```

#### Discussion

This method always succeeds unless the lock has been damaged. If another process has already unlocked or broken the lock, this method has no effect. You should generally use [`unlock()`](nsdistributedlock/unlock().md) rather than [`break()`](nsdistributedlock/break().md) to relinquish a lock.

> ⚠️ **Warning**:  Because `breakLock` can release another process’s lock, it should be used with great caution.

Even if you break a lock, there’s no guarantee that you will then be able to acquire the lock—another process might get it before your [`try()`](nsdistributedlock/try().md) is invoked.

Raises an `NSGenericException` if the lock could not be removed.

## See Also

- [func unlock()](nsdistributedlock/unlock.md)
  Relinquishes the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/break())*