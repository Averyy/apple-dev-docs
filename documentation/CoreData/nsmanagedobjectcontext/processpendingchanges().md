# processPendingChanges()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Forces the context to process changes to the object graph.

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
func processPendingChanges()
```

```objc
- (void) processPendingChanges;
```

## Discussion

This method causes changes to registered managed objects to be recorded with the undo manager.

In AppKit-based applications, this method is invoked automatically at least once during the event loop (at the end of the loop)—it may be called more often than that if the framework needs to coalesce your changes before doing something else. You can also invoke it manually to coalesce any pending unprocessed changes.

## See Also

### Related Documentation
- [func undo()](./undo%28%29.md)
  Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [var undoManager: UndoManager?](./undomanager.md)
  The object that provides undo support for the context.
- [func redo()](./redo%28%29.md)
  Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
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
- [func assign(Any, to: NSPersistentStore)](./assign%28_,to%29.md)
  Specifies the store in which a newly inserted object will be saved.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws](./obtainpermanentids%28for%29.md)
  Converts to permanent IDs the object IDs of the objects in a given array.
- [func detectConflicts(for: NSManagedObject)](./detectconflicts%28for%29.md)
  Marks an object for conflict detection.
- [func refresh(NSManagedObject, mergeChanges: Bool)](./refresh%28_,mergechanges%29.md)
  Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](./observevalue%28forkeypath,of,change,context%29.md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/processpendingchanges())*