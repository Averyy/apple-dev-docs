# init(concurrencyType:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a context that uses the specified concurrency type.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`init(_:)`](./init%28_%29.md) instead.

## Declaration

```swift
init(concurrencyType ct: NSManagedObjectContextConcurrencyType)
```

```objc
- (instancetype) initWithConcurrencyType:(NSManagedObjectContextConcurrencyType) ct;
```

## Mentions

- [Using Core Data in the background](../using-core-data-in-the-background.md)

#### Discussion

For more information, see [Concurrency](../nsmanagedobjectcontext.md#Concurrency).

## Parameters

- `ct`: The context’s concurrency type. For possible values, see [`NSManagedObjectContextConcurrencyType`](../nsmanagedobjectcontextconcurrencytype.md).

## See Also

### Creating a context
- [convenience init(NSManagedObjectContext.ConcurrencyType)](./init%28_%29.md)
  Creates a context that uses the specified concurrency type.
- [NSManagedObjectContext.ConcurrencyType](./concurrencytype-swift.struct.md)
  The concurrency types to use with a managed object context.
- [enum NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md)
  The concurrency types you can use with a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init(concurrencytype:))*