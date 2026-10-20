# NSManagedObjectContext.ConcurrencyType

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

The concurrency types to use with a managed object context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
struct ConcurrencyType
```

## Topics

### Concurrency Types
- [static let mainQueue: NSManagedObjectContext.ConcurrencyType](./concurrencytype-swift.struct/mainqueue.md)
  A concurrency type where the context performs its tasks on the main queue.
- [static let privateQueue: NSManagedObjectContext.ConcurrencyType](./concurrencytype-swift.struct/privatequeue.md)
  A concurrency type where the context performs its tasks on a private queue.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Creating a context
- [convenience init(NSManagedObjectContext.ConcurrencyType)](./init%28_%29.md)
  Creates a context that uses the specified concurrency type.
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
- [enum NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md)
  The concurrency types you can use with a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct)*