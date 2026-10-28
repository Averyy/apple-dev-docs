# assign(_:to:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Specifies the store in which a newly inserted object will be saved.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func assign(_ object: Any, to store: NSPersistentStore)
```

```objc
- (void) assignObject:(id) object toPersistentStore:(NSPersistentStore *) store;
```

## Discussion

You can obtain a store from the persistent store coordinator, using for example [`persistentStore(for:)`](../nspersistentstorecoordinator/persistentstore%28for%29.md).

### Special Considerations

It is only necessary to use this method if the receiver’s persistent store coordinator manages multiple writable stores that have `object`‘s entity in their configuration. Maintaining configurations in the managed object model can eliminate the need for invoking this method directly in many situations. If the receiver’s persistent store coordinator manages only a single writable store, or if only one store has `object`’s entity in its model, `object` will automatically be assigned to that store.

## Parameters

- `object`: A managed object.
- `store`: A persistent store.

## See Also

### Related Documentation
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](./persistentstorecoordinator.md)
  The persistent store coordinator of the context.
### Handling managed objects
- [var shouldDeleteInaccessibleFaults: Bool](./shoulddeleteinaccessiblefaults.md)
  A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [var insertedObjects: Set<NSManagedObject>](./insertedobjects.md)
  The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [var updatedObjects: Set<NSManagedObject>](./updatedobjects.md)
  The set of objects registered with the context that have uncommitted changes.
- [var deletedObjects: Set<NSManagedObject>](./deletedobjects.md)
  The set of objects that will be removed from their persistent store during the next save operation.
- [func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID, triggeredByProperty: NSPropertyDescription?) -> Bool](./shouldhandleinaccessiblefault%28_,for,triggeredbyproperty%29.md)
  Creates a log of the inaccessible fault.
- [func insert(NSManagedObject)](./insert%28_%29.md)
  Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [func delete(NSManagedObject)](./delete%28_%29.md)
  Specifies an object that should be removed from its persistent store when changes are committed.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws](./obtainpermanentids%28for%29.md)
  Converts to permanent IDs the object IDs of the objects in a given array.
- [func detectConflicts(for: NSManagedObject)](./detectconflicts%28for%29.md)
  Marks an object for conflict detection.
- [func refresh(NSManagedObject, mergeChanges: Bool)](./refresh%28_,mergechanges%29.md)
  Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [func processPendingChanges()](./processpendingchanges%28%29.md)
  Forces the context to process changes to the object graph.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](./observevalue%28forkeypath,of,change,context%29.md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/assign(_:to:))*