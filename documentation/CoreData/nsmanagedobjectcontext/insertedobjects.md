# insertedObjects

**Framework**: Core Data  
**Kind**: property

The set of objects that have been inserted into the context but not yet saved in a persistent store.

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
var insertedObjects: Set<NSManagedObject> { get }
```

#### Discussion

A managed object context does not post key-value observing notifications when the return value of `insertedObjects` changes—it does, however, post a [`NSManagedObjectContextObjectsDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506884-nsmanagedobjectcontextobjectsdid) notification when a change is made, and a [`NSManagedObjectContextWillSave`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506816-nsmanagedobjectcontextwillsave) and a [`NSManagedObjectContextDidSave`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506380-nsmanagedobjectcontextdidsave) notification before and after changes are committed respectively.

## See Also

- [var registeredObjects: Set<NSManagedObject>](nsmanagedobjectcontext/registeredobjects.md)
  The set of registered managed objects in the context.
- [var shouldDeleteInaccessibleFaults: Bool](nsmanagedobjectcontext/shoulddeleteinaccessiblefaults.md)
  A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [var updatedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/updatedobjects.md)
  The set of objects registered with the context that have uncommitted changes.
- [var deletedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/deletedobjects.md)
  The set of objects that will be removed from their persistent store during the next save operation.
- [func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID, triggeredByProperty: NSPropertyDescription?) -> Bool](nsmanagedobjectcontext/shouldhandleinaccessiblefault(_:for:triggeredbyproperty:).md)
  Creates a log of the inaccessible fault.
- [func insert(NSManagedObject)](nsmanagedobjectcontext/insert(_:).md)
  Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [func delete(NSManagedObject)](nsmanagedobjectcontext/delete(_:).md)
  Specifies an object that should be removed from its persistent store when changes are committed.
- [func assign(Any, to: NSPersistentStore)](nsmanagedobjectcontext/assign(_:to:).md)
  Specifies the store in which a newly inserted object will be saved.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws](nsmanagedobjectcontext/obtainpermanentids(for:).md)
  Converts to permanent IDs the object IDs of the objects in a given array.
- [func detectConflicts(for: NSManagedObject)](nsmanagedobjectcontext/detectconflicts(for:).md)
  Marks an object for conflict detection.
- [func refresh(NSManagedObject, mergeChanges: Bool)](nsmanagedobjectcontext/refresh(_:mergechanges:).md)
  Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [func processPendingChanges()](nsmanagedobjectcontext/processpendingchanges.md)
  Forces the context to process changes to the object graph.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](nsmanagedobjectcontext/observevalue(forkeypath:of:change:context:).md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/insertedobjects)*