# tryLock()

**Framework**: Core Data  
**Kind**: method

Attempts to acquire a lock.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func tryLock() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a lock was acquired, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

This method returns immediately after the attempt to acquire a lock.

## See Also

- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](nsmanagedobjectcontext/init(concurrencytype:).md)
  Creates a context that uses the specified concurrency type.
- [convenience init()](nsmanagedobjectcontext/init.md)
- [func lock()](nsmanagedobjectcontext/lock.md)
  Attempts to acquire a lock on the context.
- [func unlock()](nsmanagedobjectcontext/unlock.md)
  Relinquishes a previously acquired lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/trylock())*