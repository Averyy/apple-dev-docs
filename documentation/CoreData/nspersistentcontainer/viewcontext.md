# viewContext

**Framework**: Core Data  
**Kind**: property

The main queue’s managed object context.

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
var viewContext: NSManagedObjectContext { get }
```

## Mentions

- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)
- [Syncing a Core Data Store with CloudKit](syncing-a-core-data-store-with-cloudkit.md)
- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Discussion

This property contains a reference to the [`NSManagedObjectContext`](nsmanagedobjectcontext.md) that is created and owned by the persistent container which is associated with the main queue of the application. This context is created automatically as part of the initialization of the persistent container.

This context is associated directly with the [`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md) and is non-generational by default.

## See Also

- [func newBackgroundContext() -> NSManagedObjectContext](nspersistentcontainer/newbackgroundcontext.md)
  Returns a new managed object context that executes on a private queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/viewcontext)*