# NSManagedObjectContextConcurrencyType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

The concurrency types you can use with a managed object context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum NSManagedObjectContextConcurrencyType
```

```c
enum NSManagedObjectContextConcurrencyType : NSUInteger;
```

## Topics

### Concurrency Types
- [NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType](./nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md)
  Specifies that the context will be associated with a private dispatch queue.
- [NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType](./nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.md)
  Specifies that the context will be associated with the main queue.
- [NSManagedObjectContextConcurrencyType.confinementConcurrencyType](./nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype.md)
  Specifies that the context will use the thread confinement pattern.
### Initializers
- [init?(rawValue: UInt)](./nsmanagedobjectcontextconcurrencytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a context
- [convenience init(NSManagedObjectContext.ConcurrencyType)](./nsmanagedobjectcontext/init%28_%29.md)
  Creates a context that uses the specified concurrency type.
- [NSManagedObjectContext.ConcurrencyType](./nsmanagedobjectcontext/concurrencytype-swift.struct.md)
  The concurrency types to use with a managed object context.
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./nsmanagedobjectcontext/init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype)*