# count(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a count of the objects the specified request fetches when it executes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 3.0+
- macOS 10.5+
- tvOS 3.0+
- visionOS
- watchOS 1.0+

## Declaration

```swift
nonisolated
func count<T>(for request: NSFetchRequest<T>) throws -> Int where T : NSFetchRequestResult
```

## See Also

### Registering and fetching objects
- [func fetch(NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]](./fetch%28_%29-38ys1.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
- [func fetch<T>(NSFetchRequest<T>) throws -> [T]](./fetch%28_%29-4xeoz.md)
  Returns an array of items of the specified type that meet the fetch request’s critieria.
- [func count(for: NSFetchRequest<any NSFetchRequestResult>) throws -> Int](./count%28for%29-93zbm.md)
  Returns the number of objects the specified request fetches when it executes.
- [func registeredObject(for: NSManagedObjectID) -> NSManagedObject?](./registeredobject%28for%29.md)
  Returns an object that exists in the context.
- [func object(with: NSManagedObjectID) -> NSManagedObject](./object%28with%29.md)
  Returns either an existing object from the context or a fault that represents that object.
- [func existingObject(with: NSManagedObjectID) throws -> NSManagedObject](./existingobject%28with%29.md)
  Returns an existing object from either the context or the persistent store.
- [var registeredObjects: Set<NSManagedObject>](./registeredobjects.md)
  The set of registered managed objects in the context.
- [func execute(NSPersistentStoreRequest) throws -> NSPersistentStoreResult](./execute%28_%29.md)
  Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [func refreshAllObjects()](./refreshallobjects%28%29.md)
  Refreshes all of the registered managed objects in the context.
- [var retainsRegisteredObjects: Bool](./retainsregisteredobjects.md)
  A Boolean value that indicates whether the context keeps strong references to all registered managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/count(for:)-3r91z)*