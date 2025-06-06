# fetch(_:)

**Framework**: Core Data  
**Kind**: method

Returns an array of items of the specified type that meet the fetch request’s critieria.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst ?+
- macOS 10.4+
- tvOS 3.0+
- visionOS ?+
- watchOS 1.0+

## Declaration

```swift
func fetch<T>(_ request: NSFetchRequest<T>) throws -> [T] where T : NSFetchRequestResult
```

## Mentions

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)

#### Discussion

This method fetches objects from the context and the persistent stores that you associate with the context’s persistent store coordinator. The method registers any objects it retrieves from a store with the context.

Consider the following when fetching:

- If the fetch request doesn’t have a predicate, it returns all instances of the specified entity.
- The fetch results include any object in the context that’s an instance of the request’s entity, and that meets the request’s criteria, even if the context has yet to save the object to a persistent store.
- The fetch request evalutes the in-memory state of each object. Therefore, the fetch results include any unsaved objects with changes that cause them to meet the request’s criteria, even if their counterparts in the persistent store don’t. Conversely, the results don’t include unsaved objects with in-memory changes that mean they no longer meet the criteria, even if their store versions do.
- The fetch results don’t include deleted objects, even if the context has yet to save the deletion to the persistent store.

A fetch never changes realized objects, or those with pending changes, without developer intervention. If you fetch objects, modify them, and then execute a new fetch that includes a superset of those objects, you don’t receive new instances of those objects. Instead, you receive the existing objects with their current in-memory state.

## Parameters

- `request`: The fetch request that specifies the search criteria.

## See Also

- [func fetch(NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]](nsmanagedobjectcontext/fetch(_:)-38ys1.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
- [func count(for: NSFetchRequest<any NSFetchRequestResult>) throws -> Int](nsmanagedobjectcontext/count(for:)-93zbm.md)
  Returns the number of objects the specified request fetches when it executes.
- [func registeredObject(for: NSManagedObjectID) -> NSManagedObject?](nsmanagedobjectcontext/registeredobject(for:).md)
  Returns an object that exists in the context.
- [func object(with: NSManagedObjectID) -> NSManagedObject](nsmanagedobjectcontext/object(with:).md)
  Returns either an existing object from the context or a fault that represents that object.
- [func existingObject(with: NSManagedObjectID) throws -> NSManagedObject](nsmanagedobjectcontext/existingobject(with:).md)
  Returns an existing object from either the context or the persistent store.
- [var registeredObjects: Set<NSManagedObject>](nsmanagedobjectcontext/registeredobjects.md)
  The set of registered managed objects in the context.
- [func count<T>(for: NSFetchRequest<T>) throws -> Int](nsmanagedobjectcontext/count(for:)-3r91z.md)
  Returns a count of the objects the specified request fetches when it executes.
- [func execute(NSPersistentStoreRequest) throws -> NSPersistentStoreResult](nsmanagedobjectcontext/execute(_:).md)
  Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [func refreshAllObjects()](nsmanagedobjectcontext/refreshallobjects.md)
  Refreshes all of the registered managed objects in the context.
- [var retainsRegisteredObjects: Bool](nsmanagedobjectcontext/retainsregisteredobjects.md)
  A Boolean value that indicates whether the context keeps strong references to all registered managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/fetch(_:)-4xeoz)*