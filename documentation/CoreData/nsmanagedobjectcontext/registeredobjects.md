# registeredObjects

**Framework**: Core Data  
**Kind**: property

The set of registered managed objects in the context.

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
var registeredObjects: Set<NSManagedObject> { get }
```

#### Discussion

A managed object context does not post key-value observing notifications when the return value of `registeredObjects` changes.

## See Also

- [var deletedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/deletedobjects.md)
  The set of objects that will be removed from their persistent store during the next save operation.
- [var insertedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/insertedobjects.md)
  The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [var updatedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/updatedobjects.md)
  The set of objects registered with the context that have uncommitted changes.
- [func fetch(NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]](nsmanagedobjectcontext/fetch(_:)-38ys1.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
- [func fetch<T>(NSFetchRequest<T>) throws -> [T]](nsmanagedobjectcontext/fetch(_:)-4xeoz.md)
  Returns an array of items of the specified type that meet the fetch request’s critieria.
- [func count(for: NSFetchRequest<any NSFetchRequestResult>) throws -> Int](nsmanagedobjectcontext/count(for:)-93zbm.md)
  Returns the number of objects the specified request fetches when it executes.
- [func registeredObject(for: NSManagedObjectID) -> NSManagedObject?](nsmanagedobjectcontext/registeredobject(for:).md)
  Returns an object that exists in the context.
- [func object(with: NSManagedObjectID) -> NSManagedObject](nsmanagedobjectcontext/object(with:).md)
  Returns either an existing object from the context or a fault that represents that object.
- [func existingObject(with: NSManagedObjectID) throws -> NSManagedObject](nsmanagedobjectcontext/existingobject(with:).md)
  Returns an existing object from either the context or the persistent store.
- [func count<T>(for: NSFetchRequest<T>) throws -> Int](nsmanagedobjectcontext/count(for:)-3r91z.md)
  Returns a count of the objects the specified request fetches when it executes.
- [func execute(NSPersistentStoreRequest) throws -> NSPersistentStoreResult](nsmanagedobjectcontext/execute(_:).md)
  Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [func refreshAllObjects()](nsmanagedobjectcontext/refreshallobjects.md)
  Refreshes all of the registered managed objects in the context.
- [var retainsRegisteredObjects: Bool](nsmanagedobjectcontext/retainsregisteredobjects.md)
  A Boolean value that indicates whether the context keeps strong references to all registered managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/registeredobjects)*