# init(name:)

**Framework**: Core Data  
**Kind**: init

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

#### Return Value

A persistent container initialized with the given name.

#### Discussion

By default, the provided name value is used to name the persistent store and is used to look up the name of the [`NSManagedObjectModel`](nsmanagedobjectmodel.md) object to be used with the [`NSPersistentContainer`](nspersistentcontainer.md) object.

## Parameters

- `name`: The name of the   object.

## See Also

- [init(name: String, managedObjectModel: NSManagedObjectModel)](nspersistentcontainer/init(name:managedobjectmodel:).md)
  Create a container with the specified name and managed object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/init(name:))*