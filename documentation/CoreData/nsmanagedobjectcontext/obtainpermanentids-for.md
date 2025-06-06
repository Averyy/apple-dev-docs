# obtainPermanentIDs(for:)

**Framework**: Core Data  
**Kind**: method

Converts to permanent IDs the object IDs of the objects in a given array.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func obtainPermanentIDs(for objects: [NSManagedObject]) throws
```

#### Discussion

This method converts the object ID of each managed object in `objects` to a permanent ID. Although the object will have a permanent ID, it will still respond positively to [`isInserted`](nsmanagedobject/isinserted.md) until it is saved. Any object that already has a permanent ID is ignored.

Any object not already assigned to a store is assigned based on the same rules Core Data uses for assignment during a save operation (first writable store supporting the entity, and appropriate for the instance and its related items).

##### Special Considerations

This method results in a transaction with the underlying store which changes the file’s modification date.

In macOS, this results an additional consideration if you invoke this method on the managed object context associated with an instance of [`NSPersistentDocument`](https://developer.apple.com/documentation/AppKit/NSPersistentDocument). Instances of `NSDocument` need to know that they are in sync with the underlying content. To avoid problems, after invoking this method you must therefore update the document’s modification date (using [`fileModificationDate`](https://developer.apple.com/documentation/AppKit/NSDocument/fileModificationDate)).

## Parameters

- `objects`: An array of managed objects.

## See Also

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
- [func assign(Any, to: NSPersistentStore)](nsmanagedobjectcontext/assign(_:to:).md)
  Specifies the store in which a newly inserted object will be saved.
- [func detectConflicts(for: NSManagedObject)](nsmanagedobjectcontext/detectconflicts(for:).md)
  Marks an object for conflict detection.
- [func refresh(NSManagedObject, mergeChanges: Bool)](nsmanagedobjectcontext/refresh(_:mergechanges:).md)
  Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [func processPendingChanges()](nsmanagedobjectcontext/processpendingchanges.md)
  Forces the context to process changes to the object graph.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](nsmanagedobjectcontext/observevalue(forkeypath:of:change:context:).md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/obtainpermanentids(for:))*