# init(concurrencyType:)

**Framework**: Core Data  
**Kind**: init

Creates a context that uses the specified concurrency type.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(concurrencyType ct: NSManagedObjectContextConcurrencyType)
```

## Mentions

- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Discussion

For more information, see [`Concurrency`](nsmanagedobjectcontext#Concurrency.md).

## Parameters

- `ct`: The context’s concurrency type. For possible values, see  .

## See Also

- [convenience init(NSManagedObjectContext.ConcurrencyType)](nsmanagedobjectcontext/init(_:).md)
  Creates a context that uses the specified concurrency type.
- [NSManagedObjectContext.ConcurrencyType](nsmanagedobjectcontext/concurrencytype-swift.struct.md)
  The concurrency types to use with a managed object context.
- [enum NSManagedObjectContextConcurrencyType](nsmanagedobjectcontextconcurrencytype.md)
  The concurrency types you can use with a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init(concurrencytype:))*