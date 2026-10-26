# persistentContainerWithName:

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Initializes a new persistent container using the provided name for the container.

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
+ (instancetype) persistentContainerWithName:(NSString *) name;
```

#### Return Value

An initialized persistent container using the passed in name, or `nil` if the container could not be initialized.

#### Discussion

This convenience method will invoke [`init(name:)`](./init%28name%29.md) and returns the initialized persistent container.

## Parameters

- `name`: The name of the persistent container.

## See Also

### Creating a Container
- [convenience init(name: String)](./init%28name%29.md)
  Creates a container with the specified name.
- [init(name: String, managedObjectModel: NSManagedObjectModel)](./init%28name,managedobjectmodel%29.md)
  Create a container with the specified name and managed object model.
- [+ persistentContainerWithName:managedObjectModel:](./persistentcontainerwithname_managedobjectmodel_.md)
  Initializes a new persistent container using the provided name and managed object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentcontainerwithname:)*