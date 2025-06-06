# NSSaveChangesRequest

**Framework**: Core Data  
**Kind**: class

An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSSaveChangesRequest
```

## Topics

### Initializing a Request
- [init(inserted: Set<NSManagedObject>?, updated: Set<NSManagedObject>?, deleted: Set<NSManagedObject>?, locked: Set<NSManagedObject>?)](nssavechangesrequest/init(inserted:updated:deleted:locked:).md)
  Initializes a save changes request with collections of given changes.
### Getting Information about a Request
- [var insertedObjects: Set<NSManagedObject>?](nssavechangesrequest/insertedobjects.md)
  The objects that were inserted into the calling context.
- [var updatedObjects: Set<NSManagedObject>?](nssavechangesrequest/updatedobjects.md)
  The objects that were modified in the calling context.
- [var deletedObjects: Set<NSManagedObject>?](nssavechangesrequest/deletedobjects.md)
  The objects that were deleted in the calling context.
- [var lockedObjects: Set<NSManagedObject>?](nssavechangesrequest/lockedobjects.md)
  The objects that were flagged for optimistic locking on the calling context.

## Relationships

### Inherits From
- [NSPersistentStoreRequest](nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)
  An object that enables an app’s contexts and the underlying persistent stores to work together.
- [class NSPersistentStore](nspersistentstore.md)
  The abstract base class for all Core Data persistent stores.
- [class NSPersistentStoreDescription](nspersistentstoredescription.md)
  A description object used to create and load a persistent store.
- [class NSPersistentStoreRequest](nspersistentstorerequest.md)
  Criteria used to retrieve data from or save data to a persistent store.
- [class NSPersistentStoreResult](nspersistentstoreresult.md)
  The abstract base class for results returned from a persistent store coordinator.
- [class NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)
  A concrete class used to represent the results of an asynchronous request.
- [class NSAtomicStore](nsatomicstore.md)
  An abstract superclass that you subclass to create a Core Data atomic store.
- [class NSAtomicStoreCacheNode](nsatomicstorecachenode.md)
  A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [class NSIncrementalStore](nsincrementalstore.md)
  An abstract superclass defining the API through which Core Data communicates with a store.
- [class NSIncrementalStoreNode](nsincrementalstorenode.md)
  A concrete class used to represent basic nodes in a Core Data incremental store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssavechangesrequest)*