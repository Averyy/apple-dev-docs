# init(name:managedObjectModel:)

**Framework**: Core Data  
**Kind**: init

Create a container with the specified name and managed object model.

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
init(name: String, managedObjectModel model: NSManagedObjectModel)
```

#### Return Value

A persistent container initialized with the given name and model.

#### Discussion

By default, the provided name value of the container is used as the name of the persisent store associated with the container. Passing in the [`NSManagedObjectModel`](nsmanagedobjectmodel.md) object overrides the lookup of the model by the provided name value.

## Parameters

- `name`: The name used by the persistent container.
- `model`: The managed object model to be used by the persistent container.

## See Also

- [convenience init(name: String)](nspersistentcontainer/init(name:).md)
  Creates a container with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/init(name:managedobjectmodel:))*