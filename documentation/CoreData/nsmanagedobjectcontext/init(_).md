# init(_:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a context that uses the specified concurrency type.

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
nonisolated
convenience init(_ type: NSManagedObjectContext.ConcurrencyType)
```

## Discussion

For more information, see [Concurrency](../nsmanagedobjectcontext.md#Concurrency).

## Parameters

- `type`: The context’s concurrency type. For possible values, see [`NSManagedObjectContext.ConcurrencyType`](./concurrencytype-swift.struct.md).

## See Also

### Creating a context
- [NSManagedObjectContext.ConcurrencyType](./concurrencytype-swift.struct.md)
  The concurrency types to use with a managed object context.
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
- [enum NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md)
  The concurrency types you can use with a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init(_:))*