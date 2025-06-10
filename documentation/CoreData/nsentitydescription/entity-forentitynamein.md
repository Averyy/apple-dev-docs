# entity(forEntityName:in:)

**Framework**: Core Data  
**Kind**: method

Returns the entity with the specified name from the managed object model associated with the specified managed object context’s persistent store coordinator.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func entity(forEntityName entityName: String, in context: NSManagedObjectContext) -> NSEntityDescription?
```

#### Return Value

The entity with the specified name from the managed object model associated with `context`’s persistent store coordinator.

#### Discussion

Raises [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException) if `context` is `nil`.

This method is functionally equivalent to the following code example.

```objc
NSManagedObjectModel *managedObjectModel = [[context persistentStoreCoordinator] managedObjectModel];
NSEntityDescription *entity = [[managedObjectModel entitiesByName] objectForKey:entityName];
return entity;
```

## Parameters

- `entityName`: The name of an entity.
- `context`: The managed object context to use. Must not be  .

## See Also

- [var entitiesByName: [String : NSEntityDescription]](nsmanagedobjectmodel/entitiesbyname.md)
  The entities of the model, keyed by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/entity(forentityname:in:))*