# performBackgroundTask(_:)

**Framework**: Core Data  
**Kind**: method

Executes a closure on a private queue using an ephemeral managed object context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func performBackgroundTask(_ block: @escaping (NSManagedObjectContext) -> Void)
```

## Mentions

- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Discussion

Each time this method is invoked, the persistent container creates a new [`NSManagedObjectContext`](nsmanagedobjectcontext.md) with the [`concurrencyType`](nsmanagedobjectcontext/concurrencytype-swift.property.md) set to [`NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType`](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md). The persistent container then executes the passed in block against that newly created context on the context’s private queue.

## Parameters

- `block`: A closure that is executed by the persistent container against a newly created private context. The private context is passed into the block as part of the execution of the block.

## See Also

- [func performBackgroundTask<T>((NSManagedObjectContext) throws -> T) async rethrows -> T](nspersistentcontainer/performbackgroundtask(_:)-25nok.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/performbackgroundtask(_:)-39sch)*