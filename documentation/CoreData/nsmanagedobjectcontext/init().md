# init()

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 3.0+ - Deprecated in 9.0
- iPadOS 3.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.11
- tvOS - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use -initWithConcurrencyType: instead

## Declaration

```swift
convenience init()
```

```objc
- (instancetype) init;
```

## See Also

### Deprecated instance methods
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
- [func lock()](./lock%28%29.md)
  Attempts to acquire a lock on the context.
- [func tryLock() -> Bool](./trylock%28%29.md)
  Attempts to acquire a lock.
- [func unlock()](./unlock%28%29.md)
  Relinquishes a previously acquired lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init())*