# tryLock()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use a queue style context and -performBlock: instead

## Declaration

```swift
func tryLock() -> Bool
```

```objc
- (BOOL) tryLock;
```

## Return Value

[`true`](../../Swift/true.md) if a lock was acquired, [`false`](../../Swift/false.md) otherwise.

## Discussion

This method returns immediately after the attempt to acquire a lock.

## See Also

### Deprecated instance methods
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
- [convenience init()](./init%28%29.md)
- [func lock()](./lock%28%29.md)
  Attempts to acquire a lock on the context.
- [func unlock()](./unlock%28%29.md)
  Relinquishes a previously acquired lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/trylock())*