# unlock()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Relinquishes a previously acquired lock.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use a queue style context and -performBlockAndWait: instead

## Declaration

```swift
func unlock()
```

```objc
- (void) unlock;
```

## See Also

### Deprecated instance methods
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
- [convenience init()](./init%28%29.md)
- [func lock()](./lock%28%29.md)
  Attempts to acquire a lock on the context.
- [func tryLock() -> Bool](./trylock%28%29.md)
  Attempts to acquire a lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/unlock())*