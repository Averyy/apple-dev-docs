# managedObjectModel

**Framework**: Core Data  
**Kind**: property

The container’s managed object model.

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
var managedObjectModel: NSManagedObjectModel { get }
```

## Mentions

- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)

#### Discussion

This property contains a reference to the [`NSManagedObjectModel`](nsmanagedobjectmodel.md) object associated with this persistent container.

## See Also

- [var name: String](nspersistentcontainer/name.md)
  The container’s name.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator](nspersistentcontainer/persistentstorecoordinator.md)
  The container’s persistent store coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/managedobjectmodel)*