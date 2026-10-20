# name

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The container’s name.

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
var name: String { get }
```

```objc
@property (copy, readonly) NSString * name;
```

#### Discussion

This property is passed in as part of the initialization of the persistent container. This name is used to locate the [`NSManagedObjectModel`](../nsmanagedobjectmodel.md) (if the [`NSManagedObjectModel`](../nsmanagedobjectmodel.md) object is not passed in as part of the initialization) and is used to name the persistent store.

## See Also

### Getting the Container’s Configuration
- [var managedObjectModel: NSManagedObjectModel](./managedobjectmodel.md)
  The container’s managed object model.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator](./persistentstorecoordinator.md)
  The container’s persistent store coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/name)*