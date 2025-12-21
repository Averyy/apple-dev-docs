# fetch(_:)

**Framework**: Core Data  
**Kind**: method

Returns an array of objects that meet the criteria of the specified fetch request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func fetch(_ request: NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]
```

#### Return Value

An array of objects that meet the criteria specified by `request` fetched from the receiver and from the persistent stores associated with the receiver’s persistent store coordinator. If an error occurs, returns `nil`. If no objects match the criteria specified by `request`, returns an empty array.

#### Discussion

Returned objects are registered with the receiver.

The following points are important to consider:

- If the fetch request has no predicate, then all instances of the specified entity are retrieved, modulo other criteria below.
- An object that meets the criteria specified by `request` (it is an instance of the entity specified by the request, and it matches the request’s predicate if there is one) and that has been inserted into a context but which is not yet saved to a persistent store, is retrieved if the fetch request is executed on that context.
- If an object in a context has been modified, a predicate is evaluated against its modified state, not against the current state in the persistent store. Therefore, if an object in a context has been modified such that it meets the fetch request’s criteria, the request retrieves it even if changes have not been saved to the store and the values in the store are such that it does not meet the criteria. Conversely, if an object in a context has been modified such that it does not match the fetch request, the fetch request will not retrieve it even if the version in the store does match.
- If an object has been deleted from the context, the fetch request does not retrieve it even if that deletion has not been saved to a store.

Objects that have been realized (populated, faults fired, “read from”, and so on) as well as pending updated, inserted, or deleted, are never changed by a fetch operation without developer intervention. If you fetch some objects, work with them, and then execute a new fetch that includes a superset of those objects, you do not get new instances or update data for the existing objects—you get the existing objects with their current in-memory state.

## Parameters

- `request`: A fetch request that specifies the search criteria for the fetch.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Predicate Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Core Data Snippets](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CoreDataSnippets/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008285)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/fetch(_:)-38ys1)*