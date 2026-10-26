# init(name:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a container with the specified name.

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
convenience init(name: String)
```

```objc
- (instancetype) initWithName:(NSString *) name;
```

#### Return Value

A persistent container initialized with the given name.

#### Discussion

By default, the provided name value is used to name the persistent store and is used to look up the name of the [`NSManagedObjectModel`](../nsmanagedobjectmodel.md) object to be used with the [`NSPersistentContainer`](../nspersistentcontainer.md) object.

## Parameters

- `name`: The name of the [`NSPersistentContainer`](../nspersistentcontainer.md) object.

## See Also

### Creating a Container
- [init(name: String, managedObjectModel: NSManagedObjectModel)](./init%28name,managedobjectmodel%29.md)
  Create a container with the specified name and managed object model.
- [+ persistentContainerWithName:](./persistentcontainerwithname_.md)
  Initializes a new persistent container using the provided name for the container.
- [+ persistentContainerWithName:managedObjectModel:](./persistentcontainerwithname_managedobjectmodel_.md)
  Initializes a new persistent container using the provided name and managed object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/init(name:))*