# NSManagedObjectContext.ConcurrencyType

**Framework**: Core Data  
**Kind**: struct

The concurrency types to use with a managed object context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
struct ConcurrencyType
```

## Topics

### Concurrency Types
- [static let mainQueue: NSManagedObjectContext.ConcurrencyType](nsmanagedobjectcontext/concurrencytype-swift.struct/mainqueue.md)
  A concurrency type where the context performs its tasks on the main queue.
- [static let privateQueue: NSManagedObjectContext.ConcurrencyType](nsmanagedobjectcontext/concurrencytype-swift.struct/privatequeue.md)
  A concurrency type where the context performs its tasks on a private queue.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [convenience init(NSManagedObjectContext.ConcurrencyType)](nsmanagedobjectcontext/init(_:).md)
  Creates a context that uses the specified concurrency type.
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](nsmanagedobjectcontext/init(concurrencytype:).md)
  Creates a context that uses the specified concurrency type.
- [enum NSManagedObjectContextConcurrencyType](nsmanagedobjectcontextconcurrencytype.md)
  The concurrency types you can use with a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct)*