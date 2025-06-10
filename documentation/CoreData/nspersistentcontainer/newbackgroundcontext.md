# newBackgroundContext()

**Framework**: Core Data  
**Kind**: method

Returns a new managed object context that executes on a private queue.

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
func newBackgroundContext() -> NSManagedObjectContext
```

## Mentions

- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Return Value

A newly created private managed object context.

#### Discussion

Invoking this method causes the persistent container to create and return a new [`NSManagedObjectContext`](nsmanagedobjectcontext.md) with the [`concurrencyType`](nsmanagedobjectcontext/concurrencytype-swift.property.md) set to [`NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType`](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md). This new context will be associated with the [`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md) directly and is set to consume [`NSManagedObjectContextDidSave`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextDidSave) broadcasts automatically.

## See Also

- [var viewContext: NSManagedObjectContext](nspersistentcontainer/viewcontext.md)
  The main queue’s managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/newbackgroundcontext())*