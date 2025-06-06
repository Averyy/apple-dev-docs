# persistentStoreCoordinator

**Framework**: Core Data  
**Kind**: property

The container’s persistent store coordinator.

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
var persistentStoreCoordinator: NSPersistentStoreCoordinator { get }
```

## Mentions

- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)

#### Discussion

When the persistent container is initialized, it creates a persistent store coordinator as part of that initialization. That persistent store coordinator is referenced in this property.

## See Also

- [var managedObjectModel: NSManagedObjectModel](nspersistentcontainer/managedobjectmodel.md)
  The container’s managed object model.
- [var name: String](nspersistentcontainer/name.md)
  The container’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentstorecoordinator)*