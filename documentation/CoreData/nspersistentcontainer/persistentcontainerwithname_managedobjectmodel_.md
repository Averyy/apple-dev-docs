# persistentContainerWithName:managedObjectModel:

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Initializes a new persistent container using the provided name and managed object model.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
+ (instancetype) persistentContainerWithName:(NSString *) name managedObjectModel:(NSManagedObjectModel *) model;
```

#### Return Value

An initialized persistent container using the passed in name and model; or `nil` if the container could not be initialized.

#### Discussion

This method invokes [`init(name:managedObjectModel:)`](./init%28name,managedobjectmodel%29.md) and returns the initialized persistent container. This method uses the provided [`NSManagedObjectModel`](../nsmanagedobjectmodel.md) object, whereas [`persistentContainerWithName:`](./persistentcontainerwithname_.md) searches the application bundle for a model with the passed in name.

## Parameters

- `name`: Name of the persistent container.
- `model`: The [`NSManagedObjectModel`](../nsmanagedobjectmodel.md) object to be used by the persistent container.

## See Also

### Creating a Container
- [convenience init(name: String)](./init%28name%29.md)
  Creates a container with the specified name.
- [init(name: String, managedObjectModel: NSManagedObjectModel)](./init%28name,managedobjectmodel%29.md)
  Create a container with the specified name and managed object model.
- [+ persistentContainerWithName:](./persistentcontainerwithname_.md)
  Initializes a new persistent container using the provided name for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentcontainerwithname:managedobjectmodel:)*