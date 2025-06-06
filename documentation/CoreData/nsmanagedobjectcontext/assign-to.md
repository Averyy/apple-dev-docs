# assign(_:to:)

**Framework**: Core Data  
**Kind**: method

Specifies the store in which a newly inserted object will be saved.

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
func assign(_ object: Any, to store: NSPersistentStore)
```

#### Discussion

You can obtain a store from the persistent store coordinator, using for example [`persistentStore(for:)`](nspersistentstorecoordinator/persistentstore(for:).md).

##### Special Considerations

It is only necessary to use this method if the receiver’s persistent store coordinator manages multiple writable stores that have `object`‘s entity in their configuration. Maintaining configurations in the managed object model can eliminate the need for invoking this method directly in many situations. If the receiver’s persistent store coordinator manages only a single writable store, or if only one store has `object`’s entity in its model, `object` will automatically be assigned to that store.

## Parameters

- `object`: A managed object.
- `store`: A persistent store.

## See Also

- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](nsmanagedobjectcontext/persistentstorecoordinator.md)
  The persistent store coordinator of the context.
- [var shouldDeleteInaccessibleFaults: Bool](nsmanagedobjectcontext/shoulddeleteinaccessiblefaults.md)
  A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [var insertedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/insertedobjects.md)
  The set of objects that have been inserted into the context but not yet saved in a persistent store.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/assign(_:to:))*